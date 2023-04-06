# Ingenium
<img src="https://user-images.githubusercontent.com/63234184/230444864-207764ac-ad80-42db-94da-6121c34f0117.png">

A technical demonstration on Ingenium platform's NFT Certification minting application, using Ethereum's ERC721 based Solidity smart contract.
<br>Submission for the [hackUST2023](https://hackust.agorize.com/en/challenges/hackust-2023) hackathon powered by OKX.

## 💡 Description
The current demonstration focuses on the application where companies and event organizers could mint ERC721 based certifications and send it to respective individuals.

### 🤔 What can be done?
Using this application, you can create basic ERC721 based certifications with the given details:
* Program title (xxx Internship Program, xxx Hackathon 2023, etc.)
* Program organizer (Organizing company name)
* Start date
* End date
* Name (Name of the person in subject)
* Role (Role of the person in subject)

The minted ERC721 certificates can then be sent to different blockchain wallet addresses. Do note that each token is only able to be transferred once!

## 💻 Running The Code
### 🌏 Environment Setup
#### 1️⃣ Create an Infura account
An account should be created on [Infura](https://www.infura.io/), an API solution platform providing access to Ethereum and IPFS[^1] networks.
<br>After project creation, enter the ```projectId``` and ```projectSecret``` details in a .txt file, then place it on the directory: ```"./scripts/certificate_processing/infura_project_details.txt"```.

#### 2️⃣ Install Brownie
Follow the instructions on this [documentation](https://eth-brownie.readthedocs.io/en/stable/install.html). Brownie a popular Python-based development framework for Ethereum smart contracts.

#### 3️⃣ Install Ganache CLI
Follow the instructions on this [documentation](https://www.npmjs.com/package/ganache-cli). Ganache CLI (Command Line Interface) is a command-line tool that provides a local blockchain environment for Ethereum development and testing purposes.

<br>If you don't have [node.js](https://nodejs.org/en) installed on your system. Install it first.

#### 🤖 Commands
For the sake of simplicity, here are the list of commands:
1. ```pip install eth-brownie```
2. ```git clone https://github.com/yijisuk/Ingenium-tech-demo.git```
3. ```brownie compile```
4. ```ganache-cli --accounts 10 --defaultBalanceEther 1000``` create a local blockchain environment which hosts 10 accounts, individually funded with 1000ETH.
5. ```brownie run scripts/main.py``` to run the application Python script

## 📖 How it works
The executable functions of the progam are:
1. Deploy smart contract (make sure to run this function first before choosing other options)
2. Mint a NFT Certificate
3. Transfer a NFT Certificate to another addresses
4. Retrieve the data stored on a NFT Certificate from IPFS

### 🍀 Mint a NFT Certificate
With the input user data, the application deploys an ERC721-based certification and uploads it to IPFS.

### ✉️ Transfer a NFT Certificate to another addresses
The minted certificates will be provided as a list; from this list, the user could select a certificate then transfer it to other public wallet addresses.

### 👓 Retrieve the data stored on a NFT Certificate from IPFS
Select a NFT certificate, then the application retrieves the information stored in .json format from IPFS and prints it out.

## ⚡️ Future Works
The current demonstration focuses on the certificate issuer's perspective, where they mint NFT certifications and transfer to respective individuals. There are much more to work on this project:
- [x] Develop an application to generate certificate NFTs on a local blockchain testnet
- [ ] Deploy the contract on a Ethereum testnet for performance evaluation.
- [ ] Integrate with a blockchain wallet, add a login utility where different certificates are displayed for different logged-in users.
- [ ] Allow users to view other users' certificates through searching their public wallet address.

[^1]: IPFS, or InterPlanetary File System, is a decentralized and distributed file-sharing system designed to make the web faster, safer, and more open. In simple terms, it's like a combination of the World Wide Web and BitTorrent.
