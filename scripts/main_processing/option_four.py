import json

from scripts.nft_processing.retrieve_uri import retrieve_uri
from scripts.certificate_processing.retrieve_json import retrieve_json
from scripts.constants.constants import Constants as C


def retrieve_nft_certificate_details():

    CONDITION_4 = (C.contract_address is not None) \
        and (C.contract_abi is not None) \
        and (C.projectId is not None) \
        and (C.projectSecret is not None) \
        and (C.max_token_id > 0)

    if CONDITION_4:

        print(f"Max Token ID is currently {C.max_token_id}\n")

        while True:
            call_token_id = int(input("Enter Token ID to retrieve: "))

            if (call_token_id <= 0) or (call_token_id > C.max_token_id):
                print(
                    "Token ID does not exist. Please enter a valid Token ID.\n")

            else:
                break

        uri = retrieve_uri(C.CHAIN_URL, C.DEMO_MAIN_ACC,
                           C.contract_address, C.contract_abi, call_token_id)

        hash = uri.replace("https://ipfs.io/ipfs/", "")
        response_json = retrieve_json(
            hash, C.MAIN_IPFS_ENDPOINT, C.projectId, C.projectSecret)
        response_vis = json.dumps(response_json, indent=4)

        print(f"\nRetrieved IPFS data: \n{response_vis}\n")

    else:
        print(f"Please (1) deploy the contract and (2) mint an NFT first.\n")
