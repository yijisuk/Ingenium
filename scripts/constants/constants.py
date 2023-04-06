class Constants:

    contract_address, contract_abi, deployed_network, accounts = None, None, None, None
    projectId, projectSecret = None, None
    ipfs_url = None
    max_token_id = -1
    avail_certs_backup, transferred_certs_backup, transfer_executed, certificates_transferrable = [], [], 0, 0

    MAIN_IPFS_ENDPOINT = "https://ipfs.infura.io:5001"
    CHAIN_URL = "http://localhost:8545"
    DEMO_MAIN_ACC = "0x61f9a53075fc1c36ee257bbb54584c80b820f2408dac92cfc6b058242bdffd0e"
    ETH_MIN = "0.05"