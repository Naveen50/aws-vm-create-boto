import boto3
ec2 = boto3.resource('ec2')


# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-0ad620533c8392bb3',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='neeeew'
 )