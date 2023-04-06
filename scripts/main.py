from scripts.main_processing.option_one import deploy_smart_contract
from scripts.main_processing.option_two import mint_nft_certificate
from scripts.main_processing.option_three import transfer_nft_certificate
from scripts.main_processing.option_four import retrieve_nft_certificate_details
from scripts.main_processing.operations import start_program, exit_program

from scripts.constants.constants import Constants as C


def main():

    start_program()

    while True:
        print("Select options: \
              \n(1) Deploy smart contract \
              \n(2) Mint NFT Certificate \
              \n(3) Transfer NFT Certificate \
              \n(4) Retrieve NFT Certificate Details \
              \n(5) End program\n")

        option = int(input("Enter option: "))

        ### (1) Deploy smart contract ###
        if option == 1:
            deploy_smart_contract()

        ### (2) Mint NFT Certificate ###
        elif option == 2:
            mint_nft_certificate()

        ### (3) Transfer NFT Certificate ###
        elif option == 3:
            transfer_nft_certificate()

        ### (4) Retrieve NFT Certificate Details ###
        elif option == 4:
            retrieve_nft_certificate_details()

        ### (5) End program ###
        elif option == 5:

            exit_program()
            break

        ### Invalid input ###
        else:
            print("Invalid option. Please try again.\n")
