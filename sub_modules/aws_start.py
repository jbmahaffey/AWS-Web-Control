#!/usr/bin/env python3

import boto3

def startEC2(akey, skey, region):
    try:
        awsconn = boto3.resource(
            service_name='ec2',
            region_name=region,
            aws_access_key_id=akey,
            aws_secret_access_key=skey
        )

        for instance in awsconn.instances.all():
            if instance.state['Name'] == 'stopped':
                instance.start()
                return 'Instances Successfully Started'
            else:
                return 'Instances Already Running'
                
    except:
        return 'Unable to connect to AWS'