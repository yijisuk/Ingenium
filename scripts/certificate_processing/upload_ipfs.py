import requests
import json

from scripts.certificate_processing.generate_json import generate_json


def upload_ipfs(endpoint, projectId, projectSecret):

    ### GENERATE CERTIFICATE ###
    certificate = generate_json()
    certificate_json = json.dumps(certificate)

    payload = {
        'content': certificate_json.encode()
    }

    ### ADD FILE TO IPFS AND RETURN THE URL ###
    response = requests.post(endpoint + '/api/v0/add',
                             files=payload, auth=(projectId, projectSecret))
    response_contents = response.text

    try:
        response_dict = json.loads(response_contents)

    except json.JSONDecodeError:
        print("ERROR: Invalid response from Infura IPFS API.")
    
    ipfs_url = f"https://ipfs.io/ipfs/{response_dict['Hash']}"

    return ipfs_url
