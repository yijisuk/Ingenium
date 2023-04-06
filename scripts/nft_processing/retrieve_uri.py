from brownie import accounts, web3
from web3 import Web3

from scripts.constants.constants import *
from scripts.constants.constants import Constants as C

def retrieve_uri(chain_url, main_account_pkey, contract_address, contract_abi, token_id):

    # Access to chain and retrieve private key
    # w3 = Web3(Web3.HTTPProvider(chain_url))

    dev = accounts.add(main_account_pkey)

    # Check balance
    balance = dev.balance()
    if balance < web3.toWei(C.ETH_MIN, "ether"):
        raise ValueError("There is not enough balance to deploy contract")

    # Create a contract instance
    deployed_contract = web3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    # Get the stored URI and return it
    data = deployed_contract.functions.tokenURI(token_id).call()

    return data
