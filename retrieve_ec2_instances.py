import boto3

def retrieve_running_instances(instances_ids):
    ec2 = boto3.client('ec2')
    my_ec2=ec2.describe_instances(
        Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ])
    for ec2_instance in my_ec2['Reservations']:
        for ec2_id in ec2_instance['Instances']:
            instances_ids.append(ec2_id['InstanceId'])


