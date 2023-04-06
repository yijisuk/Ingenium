from scripts.nft_processing.deploy import deploy
from scripts.certificate_processing.infura_acc import infura_acc
from scripts.constants.constants import Constants as C


def deploy_smart_contract():

    C.contract_address, C.contract_abi, C.deployed_network, C.accounts = deploy(
        C.CHAIN_URL, C.DEMO_MAIN_ACC)

    CONDITION_1 = (C.contract_address is not None) \
        and (C.deployed_network is not None)

    if CONDITION_1:

        C.projectId, C.projectSecret = infura_acc()
        print(
            f"Contract deployed at {C.contract_address} on {C.deployed_network}\n")
    else:
        print(f"There was an error deploying the contract.\n")
