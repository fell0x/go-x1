from web3 import Web3, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware
import os

# Testnet's min trim price needs to be updated to 1 gwei
# This script will update the min trim price to 1 gwei.
# use the first validator's private key from ../evmcore/apply_fake_genesis.go

# Connect to local Ethereum node
w3 = Web3(HTTPProvider('http://localhost:8545'))

pk = os.environ.get('PRIVATE_KEY')  # add private key here
acct1 = w3.eth.account.from_key(pk)

w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acct1))

bytecode = '608060405234801561001057600080fd5b50600436106102765760003560e01c80637945ef9911610160578063ad7b3f7b116100d8578063c74dd6211161008c578063d9a7c1f911610071578063d9a7c1f914610517578063f2fde38b1461051f578063f8d5177e1461055257610276565b8063c74dd621146104f2578063d3f48dbe146104fa57610276565b8063b82b8427116100bd578063b82b8427146104c5578063bf25338b146104cd578063c5f530af146104ea57610276565b8063ad7b3f7b1461048b578063b6d9edd5146104a857610276565b80638da5cb5b1161012f5780638f32d59b116101145780638f32d59b1461045f57806394c3e9141461047b578063a77865151461048357610276565b80638da5cb5b146104115780638f078bfa1461044257610276565b80637945ef99146103b25780638129fc1c146103cf57806381ffcdf1146103d7578063866c4b17146103f457610276565b806338eca546116101f35780635a68f01a116101c25780636348ebb8116101a75780636348ebb814610385578063650acd66146103a2578063715018a6146103aa57610276565b80635a68f01a146103755780635e2308d21461037d57610276565b806338eca5461461032b5780633a3ef66c14610333578063433268671461033b578063455366a41461035857610276565b80632265f2841161024a5780632c8c36a51161022f5780632c8c36a5146102e95780632e84e8e6146102f15780632ee711321461030e57610276565b80632265f284146102c45780632bb9fe8d146102cc57610276565b8062cc7f831461027b57806302b769a1146102955780630d4955e3146102b45780630d7b2609146102bc575b600080fd5b61028361056f565b60408051918252519081900360200190f35b6102b2600480360360208110156102ab57600080fd5b5035610575565b005b610283610684565b61028361068a565b610283610690565b6102b2600480360360208110156102e257600080fd5b5035610696565b61028361075a565b6102b26004803603602081101561030757600080fd5b5035610760565b6102b26004803603602081101561032457600080fd5b503561086c565b610283610930565b610283610936565b6102b26004803603602081101561035157600080fd5b503561093c565b6102b26004803603602081101561036e57600080fd5b5035610a4b565b610283610b59565b610283610b5f565b6102b26004803603602081101561039b57600080fd5b5035610b65565b610283610c73565b6102b2610c79565b6102b2600480360360208110156103c857600080fd5b5035610d41565b6102b2610e6e565b6102b2600480360360208110156103ed57600080fd5b5035610f71565b6102b26004803603602081101561040a57600080fd5b503561108a565b6104196111a7565b6040805173ffffffffffffffffffffffffffffffffffffffff9092168252519081900360200190f35b6102b26004803603602081101561045857600080fd5b50356111c3565b6104676112cd565b604080519115158252519081900360200190f35b6102836112eb565b6102836112f1565b6102b2600480360360208110156104a157600080fd5b50356112f7565b6102b2600480360360208110156104be57600080fd5b5035611406565b61028361151e565b6102b2600480360360208110156104e357600080fd5b5035611524565b610283611632565b610283611638565b6102b26004803603602081101561051057600080fd5b503561163e565b61028361174a565b6102b26004803603602081101561053557600080fd5b503573ffffffffffffffffffffffffffffffffffffffff16611750565b6102b26004803603602081101561056857600080fd5b50356117b2565b60725481565b61057d6112cd565b6105ce576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b6001811015610624576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b6509184e72a00081111561067f576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b607555565b606d5481565b606c5481565b60675481565b61069e6112cd565b6106ef576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b60026106f9611876565b8161070057fe5b04811115610755576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606955565b60745481565b6107686112cd565b6107b9576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b606481101561080f576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b620f4240811115610867576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b607155565b6108746112cd565b6108c5576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b60026108cf611876565b816108d657fe5b0481111561092b576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606855565b60755481565b60735481565b6109446112cd565b610995576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b620f42408110156109ed576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b631dcd6500811115610a46576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b607355565b610a536112cd565b610aa4576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b62015180811015610afc576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b62278d00811115610b54576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606f55565b60715481565b606b5481565b610b6d6112cd565b610bbe576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b62015180811015610c16576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b620d2f00811115610c6e576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b607255565b606e5481565b610c816112cd565b610cd2576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b60335460405160009173ffffffffffffffffffffffffffffffffffffffff16907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0908390a3603380547fffffffffffffffffffffffff0000000000000000000000000000000000000000169055565b610d496112cd565b610d9a576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b6064610da4611876565b60050281610dae57fe5b04811015610e03576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b6002610e0d611876565b81610e1457fe5b04811115610e69576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606b55565b600054610100900460ff1680610e875750610e87611882565b80610e95575060005460ff16155b610ed05760405162461bcd60e51b815260040180806020018281038252602e815260200180611afe602e913960400191505060405180910390fd5b600054610100900460ff16158015610f3657600080547fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff909116610100171660011790555b610f3f33611888565b8015610f6e57600080547fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff1690555b50565b610f796112cd565b610fca576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b610fd2611876565b811015611026576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b61102e611876565b601f02811115611085576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606755565b6110926112cd565b6110e3576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b69152d02c7e14af6800000811015611142576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b6a084595161401484a0000008111156111a2576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606655565b60335473ffffffffffffffffffffffffffffffffffffffff1690565b6111cb6112cd565b61121c576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b6002811015611272576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b60648111156112c8576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606e55565b60335473ffffffffffffffffffffffffffffffffffffffff16331490565b606a5481565b60685481565b6112ff6112cd565b611350576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b62278d008110156113a8576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b630784ce00811115611401576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606d55565b61140e6112cd565b61145f576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b66b1a2bc2ec500008110156114bb576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b6801bc16d674ec800000811115611519576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b607055565b606f5481565b61152c6112cd565b61157d576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b620151808110156115d5576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b62278d0081111561162d576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606c55565b60665481565b60695481565b6116466112cd565b611697576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b60648110156116ed576040805162461bcd60e51b815260206004820152600f60248201527f746f6f20736d616c6c2076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b620d2f00811115611745576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b607455565b60705481565b6117586112cd565b6117a9576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b610f6e816119f7565b6117ba6112cd565b61180b576040805162461bcd60e51b815260206004820181905260248201527f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572604482015290519081900360640190fd5b6002611815611876565b8161181c57fe5b04811115611871576040805162461bcd60e51b815260206004820152600f60248201527f746f6f206c617267652076616c75650000000000000000000000000000000000604482015290519081900360640190fd5b606a55565b670de0b6b3a764000090565b303b1590565b600054610100900460ff16806118a157506118a1611882565b806118af575060005460ff16155b6118ea5760405162461bcd60e51b815260040180806020018281038252602e815260200180611afe602e913960400191505060405180910390fd5b600054610100900460ff1615801561195057600080547fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff909116610100171660011790555b603380547fffffffffffffffffffffffff00000000000000000000000000000000000000001673ffffffffffffffffffffffffffffffffffffffff84811691909117918290556040519116906000907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0908290a380156119f357600080547fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff1690555b5050565b73ffffffffffffffffffffffffffffffffffffffff8116611a495760405162461bcd60e51b8152600401808060200182810382526026815260200180611ad86026913960400191505060405180910390fd5b60335460405173ffffffffffffffffffffffffffffffffffffffff8084169216907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e090600090a3603380547fffffffffffffffffffffffff00000000000000000000000000000000000000001673ffffffffffffffffffffffffffffffffffffffff9290921691909117905556fe4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061646472657373436f6e747261637420696e7374616e63652068617320616c7265616479206265656e20696e697469616c697a6564a265627a7a7231582093b32e6f828b880151264a169a5c3b90c7026208db391fb98029286d18c5795164736f6c63430005110032'
abi = [
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "uint256",
                "name": "v",
                "type": "uint256"
            }
        ],
        "name": "updateMinTrimGasPrice",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
ConstantsManager = w3.eth.contract(
    abi=abi, bytecode=bytecode, address='0x6CA548f6DF5B540E72262E935b6Fe3e72cDd68C9')
tx_hash = ConstantsManager.functions.updateMinTrimGasPrice(
    1000000000).transact({'from': acct1.address})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)
