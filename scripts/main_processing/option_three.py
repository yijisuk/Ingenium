from scripts.nft_processing.transfer_nft import transfer_nft
from scripts.constants.constants import Constants as C


def transfer_nft_certificate():

    CONDITION_3 = (C.contract_address is not None) \
        and (C.contract_abi is not None) \
        and (C.accounts is not None) \
        and (C.max_token_id > 0)

    if CONDITION_3:

        if C.transfer_executed == 0:
            if len(C.avail_certs_backup) > 0:
                avail_certs = C.avail_certs_backup
            else:
                avail_certs = [i for i in range(1, C.max_token_id + 1)]

            C.transfer_executed = 1

        else:
            avail_certs = C.avail_certs_backup

        if len(C.transferred_certs_backup) > 0:
            transferred_certs = C.transferred_certs_backup
        else:
            transferred_certs = []

        print(f"\nMax Token ID is currently {C.max_token_id}.\n")

        # Check if there are certificates available for transfer.
        if len(avail_certs) > 0:
            certificates_transferrable = 1
            print("Transferrable certificates: ")
            print(f"{str(avail_certs)[1:-1]}\n")

        else:
            certificates_transferrable = 0
            print("There are no transferrable certificates.\n")

        # Display the transferred certificates.
        if len(transferred_certs) == C.max_token_id:
            print("All certificates are transferred.\n")

        elif len(transferred_certs) > 0:
            print("Transferred certificates: ")
            print(f"{str(transferred_certs)[1:-1]}\n")

        if certificates_transferrable:

            while True:
                call_token_id = int(input("Enter Token ID to retrieve: "))

                if (call_token_id <= 0) or (call_token_id > C.max_token_id):
                    print(
                        "Token ID does not exist. Please enter a valid Token ID.\n")

                else:
                    break

            print("\nHere are the list of available accounts: \n")
            for i, acc in enumerate(C.accounts):
                print(f"{i} | {acc}")
            print("\n")

            while True:
                to_address_idx = int(
                    input("Enter account number to transfer to: "))

                if (to_address_idx < 0) or (to_address_idx >= len(C.accounts) - 1):
                    print(
                        "Account does not exist. Please enter a valid account.\n")

                else:
                    break

            to_address = C.accounts[to_address_idx]

            transfer_result = transfer_nft(
                C.CHAIN_URL, C.DEMO_MAIN_ACC, C.contract_address, C.contract_abi, call_token_id, to_address)

            if transfer_result:
                avail_certs.remove(call_token_id)
                transferred_certs.append(call_token_id)
                print(
                    f"Successfully transferred NFT Certificate with Token ID {call_token_id} to {to_address}\n")

            if len(avail_certs) != len(C.avail_certs_backup):
                C.avail_certs_backup = avail_certs

            if len(transferred_certs) != len(C.transferred_certs_backup):
                C.transferred_certs_backup = transferred_certs

    else:
        print(f"Please (1) deploy the contract and (2) mint an NFT first.\n")
