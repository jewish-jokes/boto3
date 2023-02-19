import boto3
from retrieve_ec2_instances import retrieve_running_instances

instances_ids = []
retrieve_running_instances(instances_ids)

ec2_client = boto3.client("ec2")
response = ec2_client.terminate_instances(InstanceIds=instances_ids)
print(response)