# Proof of comphrehension. I wanted to learn and look at boto for python, and it seems pretty straightforward to use.

# Since it's a security risk to run sudos inside of a script, this script will require elevated privileges.
# install boto3
# configure the AWS ClI

import boto
from functools import partial
from itertools import filterfalse

def client_ec2_creator():
    client = boto3.client('ec2')
    return client

#creates any number of blank servers.
def ec2_host_creator(client, quantity_of_hosts, client_token, instance_type, TagSpecs):
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

def is_running(client_input, asset_id_input):
    response = client_input.describe_instances(
    Filters=[instance-state-name],
    InstanceIds=[asset_id_input]
    MaxResults=100)
    if 'running' in response:
        return True
    else:
        return False


def mass_instance_creator(image_input, instance_type, key_name, image_qty, key_pair_input):
    instances = ec2.create_instances(
                                     image_input,
                                     1,
                                     image_qty,
                                     instance_type,
                                     key_pair_input
                                    )



# if you wanted to mass create a large quantity of instances, you can do the following:

list_of_instances_to_create = ['Literally_anything']


def secret_key():
    # will try to store the keys in a secure manner at some point. Just know this can be programmatically done.


# use functools.partial to predefine the other fields
# Don't forget that your keypair will need to be secured, and named(this is to myself).

def instance_creator_from_list(list_of_instances_image_ids):
    fully_completed_except_for_image_id = partial(mass_instance_creator, image_qty=1, instance_type='t2.micro', key_pair_input=secret_key())
    for i in list_of_instances_image_ids:
        fully_completed_except_for_image_id(image_input=i)
    #now with just a few lines of code, several ec2 instances can be created.

def start_instance(client_input, asset_id):
    response = client_input.start_instances(asset_id)
    return 'started  ' + asset_id

#cool autostart script.
def auto_starter(client_input):
    current_list = available_instance_grabber()
    start_instance_partial = partial(start_instance, client_input=client_input)
    is_running_partial = partial(is_running, client_input=client_input)
    while True:
        start_instances = list(filterfalse(is_running_partial, current_list))
        for i in start_instances:
            start_instance_partial(i)
    