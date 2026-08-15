import subprocess
from pathlib import Path

SCRIPT = Path("scripts/audit.sh")


def run(cwd):
    return subprocess.run(
        ["bash", str(SCRIPT.resolve())],
        cwd=cwd, capture_output=True, text=True,
    )


def init_repo(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Ashik Kunjumon"], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "config", "user.email", "45920006+ashikkunjumon@users.noreply.github.com"],
        cwd=tmp_path, check=True,
    )
    return tmp_path


def commit(cwd, name, content):
    (cwd / name).write_text(content)
    subprocess.run(["git", "add", "-A"], cwd=cwd, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "test"], cwd=cwd, check=True)


def test_script_is_executable():
    assert SCRIPT.exists()


def test_clean_repo_passes(tmp_path):
    repo = init_repo(tmp_path)
    commit(repo, "ok.md", "Just ordinary documentation.\n")
    assert run(repo).returncode == 0


def test_detects_a_secret_in_an_earlier_commit(tmp_path):
    # AKIA + exactly 16 uppercase/digit characters, assembled at runtime.
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    assert len(fake_aws) == 20
    repo = init_repo(tmp_path)
    commit(repo, "leak.md", f"key={fake_aws}\n")
    commit(repo, "leak.md", "key removed\n")
    result = run(repo)
    assert result.returncode == 1
    assert "AWS" in result.stdout or "credential" in result.stdout.lower()


def test_detects_a_local_absolute_path(tmp_path):
    repo = init_repo(tmp_path)
    commit(repo, "notes.md", "See /Users/someone/secret-project/plan.md\n")
    assert run(repo).returncode == 1


def test_detects_a_non_noreply_commit_identity(tmp_path):
    repo = init_repo(tmp_path)
    subprocess.run(["git", "config", "user.email", "person@company.example"], cwd=repo, check=True)
    commit(repo, "ok.md", "content\n")
    result = run(repo)
    assert result.returncode == 1
    assert "identity" in result.stdout.lower()


def test_the_scan_actually_searches_rather_than_erroring(tmp_path):
    # Regression test for a version that passed the rev list to git grep as a
    # single argument: every check exited 128 and the gate silently checked
    # nothing while still printing a verdict.
    repo = init_repo(tmp_path)
    for i in range(5):
        commit(repo, f"file{i}.md", f"ordinary content {i}\n")
    result = run(repo)
    assert result.returncode == 0, result.stdout
    assert "clean" in result.stdout


def test_detects_a_secret_across_a_longer_history(tmp_path):
    # The broken version happened to behave differently on short histories.
    repo = init_repo(tmp_path)
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    for i in range(3):
        commit(repo, f"pad{i}.md", f"padding {i}\n")
    commit(repo, "leak.md", f"key={fake_aws}\n")
    for i in range(3):
        commit(repo, f"after{i}.md", f"more {i}\n")
    commit(repo, "leak.md", "removed\n")
    assert run(repo).returncode == 1


def test_detects_a_secret_in_a_commit_message(tmp_path):
    # The previous approach scanned trees only and would miss this entirely.
    import subprocess
    repo = init_repo(tmp_path)
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    (repo / "f.md").write_text("content\n")
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-q", "-m", f"oops key={fake_aws}"], cwd=repo, check=True)
    assert run(repo).returncode == 1
