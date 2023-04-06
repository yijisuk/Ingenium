import requests

from scripts.nft_processing.mint import mint
from scripts.certificate_processing.upload_ipfs import upload_ipfs
from scripts.constants.constants import Constants as C


def mint_nft_certificate():

    CONDITION_2 = (C.contract_address is not None) \
        and (C.contract_abi is not None) \
        and (C.projectId is not None) \
        and (C.projectSecret is not None)

    if CONDITION_2:

        while True:
            try:
                ipfs_url = upload_ipfs(
                    C.MAIN_IPFS_ENDPOINT, C.projectId, C.projectSecret)
                requests.get(ipfs_url)
                break

            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                print("There was an error on validating the IPFS URL.\n")

        token_id = mint(C.CHAIN_URL, C.DEMO_MAIN_ACC,
                        C.contract_address, C.contract_abi, ipfs_url)

        if token_id is not None:

            if token_id > C.max_token_id:
                C.max_token_id = token_id

            if C.transfer_executed and (C.max_token_id not in C.avail_certs_backup):
                C.avail_certs_backup.append(C.max_token_id)

            print(
                f"\nMinted new NFT Certificate with token ID {token_id}\n")
        else:
            print(f"\nThere was an error minting the NFT Certificate.\n")

    else:
        print(f"Please (1) deploy the contract first.\n")
