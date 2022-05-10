#!/usr/bin/env python3

import boto3

def stopEC2(akey, skey, region):
    try:
        awsconn = boto3.resource(
            service_name='ec2',
            region_name=region,
            aws_access_key_id=akey,
            aws_secret_access_key=skey
        )

        for instance in awsconn.instances.all():
            if instance.state['Name'] == 'running':
                instance.stop()
                return 'Instances Successfully Stopped'
            else:
                return 'Instances not running'
    except:
        return 'Unable to connect to AWS'