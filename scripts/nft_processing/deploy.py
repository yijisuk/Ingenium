from brownie import CertificateGenerator, accounts, network, config, web3
from web3 import Web3

from scripts.constants.constants import *
from scripts.constants.constants import Constants as C


def deploy(chain_url, main_account_pkey):

    # Access to chain and retrieve available public keys and main private key
    w3 = Web3(Web3.HTTPProvider(chain_url))
    public_keys = w3.eth.accounts

    dev = accounts.add(main_account_pkey)
    deployed_network = network.show_active()

    # Check balance
    balance = dev.balance()
    if balance < web3.toWei(C.ETH_MIN, "ether"):
        raise ValueError("There is not enough balance to deploy contract")

    # Deploy contract
    contract = CertificateGenerator.deploy({"from": dev})
    contract_address = contract.address

    deployed_contract = web3.eth.contract(
        address=contract_address,
        abi=CertificateGenerator.abi
    )

    return [contract_address, deployed_contract.abi, deployed_network, public_keys[1:]]