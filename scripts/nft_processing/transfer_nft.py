from brownie import accounts, web3
from web3 import Web3

import json
from scripts.constants.constants import *
from scripts.constants.constants import Constants as C


def transfer_nft(chain_url, main_account_pkey, contract_address, contract_abi, token_id, to_address):

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

    # Transfer the NFT
    try:
        tx_hash = deployed_contract.functions.transfer(
            to_address, token_id).transact({'from': dev.address})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    except ValueError as e:
        if "NFT is already transferred" in str(e):
            print("NFT is already transferred\n")
        
        elif "Only the original owner can transfer the NFT" in str(e):
            print("Only the original owner can transfer the NFT\n")

        return 0

    return 1
