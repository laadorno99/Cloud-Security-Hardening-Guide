# Cloud Security Hardening Guide

This project provides a step-by-step technical checklist to secure cloud environments (AWS/Azure).

## Core Security Principles

- **Principle of Least Privilege (IAM):** Ensure users only have the access they absolutely need.
- **Encryption:** Implement encryption at rest and in transit for all data.
- **Multi-Factor Authentication (MFA):** Mandatory for all user accounts and root access.

## Practical Steps for AWS Hardening

1. **Enable CloudTrail:** To log all API calls for auditing.
2. **Disable Root User Access:** Create an IAM user for daily tasks.
3. **Use Security Groups:** Restrict inbound/outbound traffic to specific IPs only.

## Technical Gotchas & Lessons Learned

- **The IAM Lockout Risk:** When applying the `BlockAllExceptMFA` policy, always verify that your current administrative IAM User already has an active MFA device configured. Applying a blanket "Deny" policy without verifying this first can permanently lock you out of your own AWS console session.
- **The Password Edge Case:** I initially forgot to include `iam:ChangePassword` in the policy exceptions. Without it, a user with an expired password and no MFA configured would be completely locked out — unable to even change their password to then set up MFA. This taught me to think through edge cases, not just the "happy path".
  
## Roadmap

- [ ] Add Azure-specific hardening steps.
- [x] Create automated security scripts (Python).
- [ ] Include a section on incident response.

---
*Check `aws-security-policy.json` in the main directory for a practical implementation of the Least Privilege principle.*

## Automated MFA Compliance Checker

`check_mfa_compliance.py` is a Python script that connects to AWS via boto3 and audits all IAM users, flagging any account that does not have MFA enabled. This automates a check that would otherwise have to be done manually in the AWS console.

### How to run

1. Install dependencies: `pip install boto3`
2. Configure your AWS credentials: `aws configure`
3. Run the script: `python check_mfa_compliance.py`

The script requires the IAM permissions `iam:ListUsers` and `iam:ListMFADevices`.

*Maintained by Lara Adorno | Cybersecurity Student*
