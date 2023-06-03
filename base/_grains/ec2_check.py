import requests
from requests.structures import CaseInsensitiveDict


def ec2_check():

    # Instantiate grains dictionary
    grains = {}

    # Instantiate grains key cloud info
    grains['cloud_info'] = []

    # Resquest token
    url_token = "http://169.254.169.254/latest/api/token"
    headers1 = CaseInsensitiveDict()
    headers1["X-aws-ec2-metadata-token-ttl-seconds"] = "21600"
    headers1["Content-Length"] = "0"
    token = requests.put(url_token, headers=headers1).text

    # Get instance-id and instance_type date
    url_instanceid = "http://169.254.169.254/latest/meta-data/instance-id"
    url_instancetype = "http://169.254.169.254/latest/meta-data/instance-type"
    headers2 = CaseInsensitiveDict()
    headers2["X-aws-ec2-metadata-token"] = token
    instance_id = requests.get(url_instanceid, headers=headers2).text
    instance_type = requests.get(url_instancetype, headers=headers2).text

    grains['cloud_info'].append({'provider': 'Amazon'})
    grains['cloud_info'][0]['instance_id'] = instance_id
    grains['cloud_info'][0]['instance_type'] = instance_type
    return grains


if __name__ == '__main__':
    ec2_check()
