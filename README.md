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

## Roadmap

- [ ] Add Azure-specific hardening steps.
- [ ] Create automated security scripts (Python).
- [ ] Include a section on incident response.

---
*Maintained by Lara Adorno | Cybersecurity Student*
