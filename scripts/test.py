from brownie import accounts, web3
from web3 import Web3

from scripts.nft_processing.deploy import deploy

def main():
    CHAIN_URL = "http://localhost:8545"
    DEMO_MAIN_ACC = "0xfbd1651f09d02dbf0630da707801ec3cfd64410ab7110fbb65551dd5ae600adc"
    contract_address, contract_abi, deployed_network, _ = deploy(CHAIN_URL, DEMO_MAIN_ACC)

    dev = accounts.add(DEMO_MAIN_ACC)

    deployed_contract = web3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    print("details:")
    # print(deployed_contract.functions.test().call())
    print(deployed_contract.functions.accessMintedNFTs().call())