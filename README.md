# Blockchain Concepts with Smart Contracts using Solidity and Web3.py ![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white) ![Solidity](https://img.shields.io/badge/Solidity-%23363636.svg?style=for-the-badge&logo=solidity&logoColor=white) ![Chainlink](https://img.shields.io/badge/Chainlink-375BD2?style=for-the-badge&logo=Chainlink&logoColor=white)

## Notes

### Smart Contracts - Nick Szabo

Smart contracts are self executing sets of Instructions, without 3rd parties.

Smart Contracts are written in code. Etherium does that.

### Oracles

Oracles bring data to blockchain or allows computation outside the blockchain environment.

Smart Contracts = Decentralized Applications = Dapps

Chainlink - Decentralized modular oracle network that allows to bring data to smart contracts.

### Advantages of Smart Contracts

- Decentralized
- Transparent
- Speed
- Immutable
- Remove Counterparty Risk
- Allow for trust minimized agreements
- Hybrid smart contracts combine on and of-chain.

### DAOs

Decentralized Autonomous Organizations are the applications that live in the smart contracts. Similar to traditional orgs. Used for governance.

### 🦊 Metamask - An ethereum wallet

### Testnets

Free for testing smart contracts.

### Mainnet

Mainnet costs money and considered live

### Faucet

Is an application that gives us free test tokens, like free test rinkeby ethereum.

### Block Explorer

Etherscan is a block explorer. An application that allows us to “view” transactions that happen on a blockchain.

### Gas

Gas is a unit of computational measure. The more computation a transaction uses the more “gas” you have to pay for.

Every transaction that happens on-chain pays a “gas fee” to node operators.

The amount of “gas” used and how much you pay depends on how “computationally expensive” your transaction is .

Sending ETH to address would be “cheaper:” than sending ETH to 1000 addresses. 

Gas Price: How much it costs per unit of gas

Gas Limit: Max amount of gas in a transaction

Transaction fee: Gas Used * Gas Price

example, 21000 gas @ 1 GWEI per gas = 21000 GWEI

### Hash

A unique fixed length string, meant to identify a piece of data. They are created by placing said data into a “hash function”.

Eth uses **Keccak-256 (SHA 3)** algorithm.

[Blockchain Demo](https://andersbrownworth.com/blockchain/)

Mines have to solve a problem inorder to create a block. For example, in this site’s example, the hash should be started from 4 zeroes. For that, the nonce is solved in such a way where the hash brings 4 zeros.

### Block

A block contains a list of transactions mined together.

Its distributed as many independent users are running the blockchain software which then compares each other’s blockchain.

### Genesis Block

First block in a blockchain. Its prev block value is 0.

Block in blockchain Consists of:- 

- Block number
- Nonce
- Data
- Prev
- Hash

### Mining

The process of finding the “solution” to the blockchain “problem”.

In our example, the “problem” was to find a hash that starts with four zeros. **(algo used = SHA256)**

Nodes get paid for mining blocks.

### Nonce

Number used once. It is used to find the solution to the blockchain problem. 

In eth, It’s also used to define the transaction number for an account/address.

## How Transactions occur

By using Public and Private Keys

### Private Key

Only known to the key holder, it’s used to “sign” transactions.

### Public Key

Key which is made out of private key by Elliptic Curve Digital Signature Algorithm(ECDSA) in ETH.

### How the address is created

Private Key —> Public Key —> Address (in Hexadecimel)

### Node

A single instance in a decentralized network. (one of the Peer A, Peer B and Peer C running those blockchain software)

Blockchains are resilient. If any node goes down, since there are so many independent nodes running and the requirement is only one node should run at all times.

Blockchain nodes keep lists of the transactions that occur.

Blockchain can run decentralized database and with ETH it can run decentralized Computation

### Consensus

Consists of Proof of Work and Proof of State. It is the mechanism used to agree on the state of a blockchain.

ETH and bitcoin use Nakamoto Consensus.

## Proof of Work

When we press that mine button, means we are showing proof of work. If any node’s blockchain differs and that is ignored, that’s called consensus.

Consensus broken of two pieces:

- Chain Selection
- Sybil Resistance - proof of work.

### Sybil Resistance

ETH and Bitcoin uses sybil resistance mechanism.

It finds out who is the block author node who mined, and the other nodes verify it.

It prevents users to make fake nodes and blockchains.

PoW(Proof of Work) and PoS(Proof of Stake) comes under SR.

### PoW

Mining comes under PoW. Computational Expensive activity.

**Block Time -** It is the time taken by block to publish. If Block time is more, the problem is hard, if it is less, the problem is easy.

### Chain Selection

How to know that which blockchain is the real blockchain or true blockchain.

Nakamoto consensus which is the combination of the proof of work and the longest chainrule. (most number of blocks)

### Block Confirmations

Number of block confirmations are defined as number of blocks that are added after our transaction block.

Therefore, if your transaction has 13 block confirmations (see above graphic), then there have been 12 blocks mined since the block was mined that included your transaction.

Gas fee is obtained by the miners in PoW and by the validators in PoS.

Solving the problem is highly competitive as the one who solves it first gets Tx. fee as well as block reward given by protocol/blockchain. ( halving reward → block reward cut in half for some period of time.)

## Attacks

### Sybil Attack

When a user creates whole bunch of pseudo-anonymous accounts to inflience the network. Really difficult in ETH BTC.

### 51% Attack

In *ETH Classic* there was a rule that if blockchain is 51% matched in Longest chain rule, its good to go. The intruders then could fork the network and bring it to their network and make that 51%. Now they have the power to influence the network as they have the longest chain.

### Drawbacks of PoW

- Uses a lot of energy

To overcome this drawback, many companies are now using Proof of Stake (PoS). ETH 2.0 will have Proof of Stake. 

### Proof of Stake

ETH 2.0, Avalanche, Polygon use PoS. Different sybil resistance mechanism.

Proof of Stake nodes put up collateral as a sybil resistance mechanism.

For example, ETH 2.0 will put some ETHs as a proof of stake. If they misbehave, they are going to lose those ETHs.

Here miners (that were in PoW) are called Validators. They validate other nodes. Nodes are randomly chosen to propose a new block.

### Randomness

ETH 2.0 uses RANDAO which collectively chooses the random number.

### Advantages

- Uses much less energy
- Scalable unlike highly variable gas prices
- Sharding - a blockchain of blockchain - it can increase number of blocks significantly and controls gas price.

### Drawback

Slightly away from decentralization - You need to pay a stake(cost) to participate.

## Layers in Blockchain

- Layer 1: Base Layer blockchain implementation
    - BTC
    - ETH
    - Avalanche
- Layer 2: Any application built on top of layer 1 or blockchain
    - Chainlink
    - Arbitram
    - Optimism
    
    Both Arbitram and Optimism solve scalability issues are called rollups. They roll up their txs. into ETH, which makes shards. They derive their security from Layer 1 and they send their txs. to layer 1.
    
    Side chains derive their security from their own protocols unlike rollups.
    

## Smart Contract and Solidity

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {
    // This will get initialized to 0
    uint256 favoriteNumber;

    struct People {
     uint256 favoriteNumber;
     string name;
    }
    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    People public person = People({favoriteNumber: 2, name: "Pranav"});

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // view, pure functions do not led to transactions, they are just for viewing.
    // pure is used when we do some math.
    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }

}
```

### Storage Factory - How to deploy user defined contracts in Blockchain out of a contract:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "./SimpleStorage.sol";

contract StorageFactory{

    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        // Address
        // ABI - application binary interface
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
    }
    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256) {
        return SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).retrieve();
    }

}
```

### ABI

ABI =  Application Binary Interface

The ABI tells solidity and other programming languages how it can interact with another contract.

Interfaces compile down to ABI.

Anytime you want to interact with an already deployed smart contract you will need an ABI.  

## Fund Me application on Solidity

```solidity
// SPDX-License-Identifier: MIT

pragma solidity >= 0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe{
    using SafeMathChainlink for uint256;

    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;

    constructor() public{
        owner = msg.sender; 
    }

    function fund() public payable{
        // $50
        uint256 minimumUSD = 50 * (10 * 18);
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!");

        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
        // what the ETH -> USD conversion rate.

    }

    function getVersion() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer);
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUSD;
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function withdraw() payable onlyOwner public{        
        msg.sender.transfer(address(this).balance);
        
        for (uint256 funderIndex=0; funderIndex < funders.length; funderIndex++){
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        
        funders = new address[](0);
    }

}
```

### Ganache is a simulated blockchain

### Introduction to [Web3.py](http://Web3.py)

[web3.py](http://web3.py) helps deploying smart contracts from local development to blockchain. We can use ganache to test our contract. Then we can finally deploy it on Rinkeby or Mainnet via Infuria.

```python
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
```

## Tests

Testing can be classified in 3 categories:

- Arranging
- Acting
- Asserting
