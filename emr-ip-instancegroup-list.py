import boto3

def get_instance_ips(cluster_id):
    emr = boto3.client('emr', region_name='your_region_name')

    # Get cluster details
    response = emr.describe_cluster(ClusterId=cluster_id)
    instance_groups = response['Cluster']['InstanceGroups']

    emr_ips_list = []

    # Loop through instance groups
    for group in instance_groups:
        instance_group_id = group['Id']
        instance_group_type = group['InstanceGroupType']

        # Get instances for the instance group
        instances_response = emr.list_instances(ClusterId=cluster_id, InstanceGroupId=instance_group_id)
        instances = instances_response['Instances']

        # Loop through instances
        for instance in instances:
            instance_id = instance['Ec2InstanceId']

            # Get instance details
            ec2 = boto3.client('ec2', region_name='your_region_name')
            ec2_response = ec2.describe_instances(InstanceIds=[instance_id])
            ec2_instance = ec2_response['Reservations'][0]['Instances'][0]

            # Get IP address
            ip_address = ec2_instance['PrivateIpAddress']

            # Append IP address to the list
            emr_ips_list.append(ip_address)

    return emr_ips_list

if __name__ == "__main__":
    cluster_id = input("Enter EMR Cluster ID: ")
    ips = get_instance_ips(cluster_id)
    print("List of IPs:")
    for ip in ips:
        print(ip)
    print("Total count of IPs:", len(ips))
