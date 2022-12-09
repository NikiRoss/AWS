import boto3
import os

# Set the AWS access and secret keys
AWS_ACCESS_KEY = os.environ["ACCESS_KEY_ID"]
AWS_SECRET_KEY = os.environ["SECRET_ACCESS_KEY"] 

print(AWS_ACCESS_KEY)


# Set the region and create an EC2 client
EC2_REGION = "eu-west-2"
ec2_client = boto3.client(
    "ec2",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=EC2_REGION
)

# Set the instance parameters
instance_type = "t2.micro" # Free tier eligible instance type
image_id = "ami-04706e771f950937f" # Amazon Linux AMI ID
key_name = "niki_gpt_instance" # The name of the key pair to use for the instance
security_groups = ["sg-08f565f88dbddadd7"] # The ID of the security group to use for the instance

# Create the instance
response = ec2_client.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_groups,
    MinCount=1,
    MaxCount=1
)

# Get the instance ID of the new instance
instance_id = response["Instances"][0]["InstanceId"]

# Wait for the instance to enter the running state
waiter = ec2_client.get_waiter("instance_running")
waiter.wait(InstanceIds=[instance_id])

# Print the instance ID
print(f"Instance created with ID: {instance_id}")