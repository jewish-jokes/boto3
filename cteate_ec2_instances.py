import boto3

ec2 = boto3.resource('ec2')

instances = []

instances_amount = input("How many instances do you want?\n")

for i in range(int(instances_amount)):
    instances.append(ec2.create_instances(
        ImageId="ami-0c0d3776ef525d5dd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2-connect"
    ))

print(f"Created instances:\n {instances}")