import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def check_mfa_compliance():
    try:
        iam = boto3.client('iam')
        users = iam.list_users()['Users']
    except NoCredentialsError:
        print("❌ AWS credentials not found. Run 'aws configure' first.")
        return
    except ClientError as e:
        print(f"❌ AWS error: {e}")
        return

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
