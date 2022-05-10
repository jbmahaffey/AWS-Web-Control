#!/usr/bin/env python3

import boto3

def main(akey, skey, region):
    try:
        awsconn = boto3.client(
            service_name='ec2',
            region_name=region,
            aws_access_key_id=akey,
            aws_secret_access_key=skey
        )

        response = awsconn.describe_instances()

        dat = '' # Variable to save output so that it can be written to file
        for instance in response['Reservations']:
            for ec2instance in instance['Instances']:
                for i in ec2instance['Tags']:
                    dat += 'Tags: {}\n'.format(i['Value'])
                dat += 'Instance ID: {}\n'.format(ec2instance['InstanceId'])
                dat += 'Instance Type: {}\n'.format(ec2instance['InstanceType'])
                dat += 'AMI ID: {}\n'.format(ec2instance['ImageId'])
                dat += 'VPC ID: {}\n'.format(ec2instance['VpcId'])
                dat += 'Key Name: {}\n'.format(ec2instance['KeyName'])
                dat += 'Private IP Address: {}\n'.format(ec2instance['PrivateIpAddress'])
                for i in ec2instance['SecurityGroups']:
                    dat += 'Security Groups: {}\n'.format(i['GroupId'])
                dat += 'Subnet ID: {}\n\n'.format(ec2instance['SubnetId'])

        return dat

    except:
        return 'Unable to connect to AWS'