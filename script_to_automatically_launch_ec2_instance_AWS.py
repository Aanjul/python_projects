# For refrence https://github.com/DiptoChakrabarty/Useful-Python-scripts-collection/blob/master/EC2-launcher/ec2.py


import boto3,os
from dotenv import load_dotenv
load_dotenv()

#Load env variables
access_key= os.getenv("ACCESS_KEY")
secret_key= os.getenv("SECRET_KEY")
ami= os.getenv("AMI")
region= os.getenv("REGION")
zone= os.getenv("ZONE")
type= os.getenv("TYPE")
subnet = os.getenv("SUBNET")

client = boto3.client(service_name='ec2', region_name=region, aws_access_key_id=  access_key,aws_secret_access_key= secret_key)


# Create ec2 resource
ec2 = boto3.resource('ec2', region_name=region, aws_access_key_id= access_key,aws_secret_access_key=  secret_key)
# create an instance
instance = ec2.create_instances(
	ImageId = ami,
	MinCount = 1,
	MaxCount = 1,
	InstanceType = type,
	KeyName = key_name,
	SubnetId = subnet)
	
instance.wait_until_running()
print("Instance Up and Running")