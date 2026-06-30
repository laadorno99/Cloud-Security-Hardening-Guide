import boto3

def check_mfa_compliance():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']

    print(f"Checking {len(users)} IAM users for MFA compliance...\n")

    no_mfa = []
    for user in users:
        username = user['UserName']
        mfa_devices = iam.list_mfa_devices(UserName=username)['MFADevices']
        if len(mfa_devices) == 0:
            no_mfa.append(username)

    if no_mfa:
        print("⚠️  Users WITHOUT MFA enabled:")
        for u in no_mfa:
            print(f"  - {u}")
    else:
        print("✅ All users have MFA enabled.")

if __name__ == "__main__":
    check_mfa_compliance()
