import json
import boto3
region = '<region>'
instances = ['<instance id>']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('Started instances: ' + str(instances))