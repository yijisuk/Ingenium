import requests
import json


def retrieve_json(content_hash, endpoint, projectId, projectSecret):

    ### READ FILE WITH HASH ###
    params = {
        'arg': content_hash
    }
    response = requests.post(endpoint + '/api/v0/cat',
                             params=params, auth=(projectId, projectSecret))

    response_contents = response.text

    try:
        response_dict = json.loads(response_contents)

    except json.JSONDecodeError:
        print("ERROR: Invalid response from Infura IPFS API.")

    return response_dict
