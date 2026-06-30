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
- [ ] Create automated security scripts (Python).
- [ ] Include a section on incident response.

---
*Check `aws-security-policy.json` in the main directory for a practical implementation of the Least Privilege principle.*

*Maintained by Lara Adorno | Cybersecurity Student*
