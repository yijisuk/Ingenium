from brownie import accounts, web3
from web3 import Web3

from scripts.constants.constants import *
from scripts.constants.constants import Constants as C

def mint(chain_url, main_account_pkey, contract_address, contract_abi, data):

    # Access to chain and retrieve private key
    w3 = Web3(Web3.HTTPProvider(chain_url))
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

    # Mint the NFT
    tx_hash = deployed_contract.functions.mint(data, dev.address).transact({'from': dev.address})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Print information about the new NFT and return the token ID
    token_id = int.from_bytes(receipt['logs'][0]['topics'][3], byteorder='big')

    return token_id