import boto3

# Set the AWS access and secret keys
AWS_ACCESS_KEY = "AKIAUGNW4XQYCD4GFXHV"
AWS_SECRET_KEY = "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"

EC2_REGION = "eu-west-2"
# create a new EC2 client
ec2 = boto3.client(
    "ec2",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=EC2_REGION
)

# get the list of security groups
response = ec2.describe_security_groups()

# print the security group IDs and their VPCs
for group in response['SecurityGroups']:
    group_id = group['GroupId']
    vpc_id = group['VpcId']
    print(f"Security group ID: {group_id}, VPC ID: {vpc_id}")

# get the list of key pairs
key_pair_response = ec2.describe_key_pairs()

if not key_pair_response:
    response = ec2.create_key_pair(KeyName="niki_key")
    
# print the key pair names
for key_pair in key_pair_response['KeyPairs']:
    key_name = key_pair['KeyName']
    print(f"Key pair name: {key_name}")