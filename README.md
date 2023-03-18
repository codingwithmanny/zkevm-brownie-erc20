# Example Brownie ERC20 Token Contract For Polygon zkEVM Testnet

The following is an example of ERC20 Token Contract configured to be deployed to Polygon zkEVM Testnet.

---

## Requirements

Take note of the python version as the latest version of python, at the time of this repository, isn't working with brownie.

- Python v3.9.5
- Brownie v1.19.3

---

## Configuration

Steps needed before hand to deploy the contract the zkEVM Testnet.

### Add zkEVM Testnet Network

Add the network support in brownie.

```bash
brownie networks add Polygon polygon-zkevm-test host="https://rpc.public.zkevm-test.net" name="zkEVM Testnet" chainid=1442 explorer="https://explorer.public.zkevm-test.net";

# Expected Output
# Brownie v1.19.3 - Python development framework for Ethereum
# 
# SUCCESS: A new network 'zkEVM Testnet' has been added
#   └─zkEVM Testnet
#     ├─id: polygon-zkevm-test
#     ├─chainid: 1442
#     ├─explorer: https://explorer.public.zkevm-test.net
#     └─host: https://rpc.public.zkevm-test.net
```

Verify the network has been successfully added.

```bash
brownie networks list true;

# Expected Output:
# ...
# 
# Polygon
#   ├─Mainnet (Infura)
#   │ ├─id: polygon-main
#   │ ├─chainid: 137
#   │ ├─explorer: https://api.polygonscan.com/api
#   │ ├─host: https://polygon-mainnet.infura.io/v3/$WEB3_INFURA_PROJECT_ID
#   │ └─multicall2: 0xc8E51042792d7405184DfCa245F2d27B94D013b6
#   ├─Mumbai Testnet (Infura)
#   │ ├─id: polygon-test
#   │ ├─chainid: 80001
#   │ ├─explorer: https://api-testnet.polygonscan.com/api
#   │ ├─host: https://polygon-mumbai.infura.io/v3/$WEB3_INFURA_PROJECT_ID
#   │ └─multicall2: 0x6842E0412AC1c00464dc48961330156a07268d14
#   └─zkEVM Testnet
#     ├─id: polygon-zkevm-test
#     ├─chainid: 1442
#     ├─explorer: https://explorer.public.zkevm-test.net
#     └─host: https://rpc.public.zkevm-test.net
```

### Add Wallet To Brownie

```bash
brownie accounts new <YOUR-CHOSEN-ID-NAME>;

# Expected Output:
# Brownie v1.19.3 - Python development framework for Ethereum
#
# Enter the private key you wish to add: <YOUR-WALLET-PRIVATE-KEY>
# Enter the password to encrypt this account with: <YOUR-NEW-PASSWORD>
# SUCCESS: A new account '0xYourConfirmedWalletAddress' has been generated with the id '<YOUR-CHOSEN-ID-NAME>'
```

Verify that the wallet has been added in brownie.

```bash
brownie accounts list

# Expected Output:
# Brownie v1.19.3 - Python development framework for Ethereum
# 
# Found 1 account:
#  └─<YOUR-CHOSEN-ID-NAME>: 0xYourConfirmedWalletAddress
```

---

## Deployment

Make sure to do the configuration section before proceeding with this next step.

```bash
# FROM: ./zkevm-brownier-erc20

brownie run token.py --network polygon-zkevm-test

# Expected Output:
# Brownie v1.19.3 - Python development framework for Ethereum
#
# Compiling contracts...
#   Solc version: 0.6.12
#   Optimizer: Enabled  Runs: 200
#   EVM Version: Istanbul
# Generating build data...
#  - SafeMath
#  - Token
#
# ZkevmBrownieErc20Project is the active project.
# 
# Running 'scripts/token.py::main'...
# Enter password for "testingwithmanny": 
# Transaction sent: 0x7fd0218b9f2963b54440df90e5480d42c537361788eb845f2eefed45376b80c9
#   Gas price: 1.113493533 gwei   Gas limit: 577595   Nonce: 2
#   Token.constructor confirmed   Block: 152186   Gas used: 521489 (90.29%)
#   Token deployed at: 0xd23D6ec4BF2EA11A6d5a6eFB25ad1AAa6765fe66
```
