#!/usr/bin/env bash
# Pre-push audit — spec §14.
# Scans EVERY commit, not just the working tree: a value removed in a later
# commit is still readable in an earlier one.
set -uo pipefail

findings=0

report() {
  echo "FINDING: $1"
  findings=$((findings + 1))
}

# Every value ever committed passes through a diff, so the patch text of all
# commits is a complete view of history -- and it covers commit messages too,
# which a tree-only scan misses.
#
# Revisions are deliberately NOT passed as arguments: `git grep <pattern> $revs`
# hands the newline-separated rev list to git as one revision and fails with
# "unable to resolve revision", so every check silently errors instead of
# searching. A gate that reports without checking is worse than no gate.
history=$(git log --all -p --no-color 2>/dev/null)
if [ -z "$history" ]; then
  echo "audit: no commits to check"
  exit 0
fi

scan() {   # $1 = extended regex, $2 = message to report
  if printf '%s' "$history" | grep -qE "$1"; then
    report "$2"
  fi
}

# 1. Commit identity on every commit.
bad_identity=$(git log --all --format='%ae%n%ce' | sort -u | grep -v 'users.noreply.github.com$' || true)
if [ -n "$bad_identity" ]; then
  report "commit identity is not a GitHub noreply address: $(echo "$bad_identity" | tr '\n' ' ')"
fi

# 2. Credentials.
#
# Every pattern below is written with a bracketed character so the literal
# does not appear in this file -- otherwise each check would match its own
# source and the audit would fail permanently on its own repository. The
# bracket is a one-character class, so 'A[K]IA' matches exactly 'AKIA'.
scan 'A[K]IA[0-9A-Z]{16}|A[S]IA[0-9A-Z]{16}' "AWS credential shape found in history"
scan 'gh[p]_[A-Za-z0-9]{30,}|github[_]pat_[A-Za-z0-9_]{20,}' "GitHub token found in history"
scan 'nv[a]pi-[A-Za-z0-9_-]{20,}' "NVIDIA credential found in history"
scan 'ey[J][A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.' "JWT found in history"
scan '[-]{5}BEGIN [A-Z ]*PRIVATE KEY' "private key block found in history"

# 3. Local paths and machine detail.
scan '/Users/[a-zA-Z0-9._-]+/|/home/[a-zA-Z0-9._-]+/|/private/tmp/' "local absolute path found in history"

# 4. Local infrastructure.
scan 'github[-]alt|id[_]rsa|id[_]ed25519' "local SSH infrastructure detail found in history"

# 5. Stray files.
if git log --all --name-only --format='' | sort -u | grep -qiE '(^|/)(\.env|\.DS_Store)$|\.(pem|key|p12)$'; then
  report "sensitive or stray file committed"
fi

if [ "$findings" -eq 0 ]; then
  echo "audit: clean — safe to push"
  exit 0
fi

cat <<'EOF'

Fix by amending or rewriting the offending commits BEFORE pushing.
A follow-up commit that deletes the value does not clear it — the earlier
commit still exposes it. Nothing has leaked until the push, so rewriting
unpushed history is free and is the correct fix.
EOF
exit 1
