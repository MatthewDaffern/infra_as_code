# Proof of comphrehension. I wanted to learn and look at boto for python, and it seems pretty straightforward to use.

# Since it's a security risk to run sudos inside of a script, this script will require elevated privileges.
# install boto3
# configure the AWS ClI


import boto
import subprocess

def client_ec2_creator():
    client = boto3.client('ec2')
    return client

#creates any number of blank servers.
def ec2_creator(client, quantity_of_hosts, client_token, instance_type, TagSpecs):
    command = client.allocate_hosts('off', 
                                    'us-west-1', 
                                    client_token, 
                                    instance_type, 
                                    quantity_of_hosts, 
                                    TagSpecs, 
                                    'off')


def volume_attacher(client, Device_input, InstanceId_input, VolumeId_input):
    command = client.attach_volume(
                                    Device_input,
                                    InstanceId_input,
                                    VolumeId_input,
                                    False
                                )

# now, I can take a list of instance_IDs and run over them.
# here is a list.

def available_instance_grabber():
    interface = boto3.resource('ec2')
    instances = interface.instances
    qty = list()
    for i in instances:
        qty.append(i.id)
    return id

def mass_start