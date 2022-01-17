from typing import Callable
from solcx import compile_standard, install_solc
import json
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]},
            },
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to rinkeby
w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/ba5dc926e8c1459eb85dda1521f33b88")
)
chain_id = 4
my_address = "0xb0a047E246656327079c92adEd60d3F97DE2DDF6"
private_key = os.getenv("PRIVATE_KEY")
print(private_key)

# create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get latest transaction
nonce = w3.eth.getTransactionCount(my_address)
# 1. Build a transaction
# 2. Sign the transaction
# 3. Send the transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
sign_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send the signed txn
print("Deploying contract...")
tx_hash = w3.eth.send_raw_transaction(sign_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!!!")

# Working with a contract, you always need
# Contract Address
# Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# Two ways to interact
# Call
# Transact

# print(simple_storage.functions.store(14).call())
# print(simple_storage.functions.retrieve().call())
print("Updating Contract...")
store_tx = simple_storage.functions.store(783).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
signed_store_tx = w3.eth.account.sign_transaction(store_tx, private_key=private_key)
tx_store_send = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_store_rec = w3.eth.wait_for_transaction_receipt(tx_store_send)
print("Contract updated!!!")
print("Retrieving the updated contract...")
print(simple_storage.functions.retrieve().call())
