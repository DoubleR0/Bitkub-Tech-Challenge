""" Detective """
from etherscan import Etherscan
eth = Etherscan('K7ST5DC6VP2Z5ZVWWD1IB3JDB5AHIEV274', net="ropsten")

alldata = eth.get_erc20_token_transfer_events_by_address('0xEcA19B1a87442b0c25801B809bf567A6ca87B1da', 0, 999999999, 'asc')

Tx = {}
transacion = []
lenTA = 0
for data in alldata:
    if data['tokenSymbol'] == "BKTC":
        Tx.update({'hash': data["hash"]})
        Tx.update({'from': data["from"]})
        Tx.update({'to': data["to"]})
        Tx.update({'value': data["value"]})
        transacion.append(Tx)
        Tx = {}

lenTF = len(transacion)
print(transacion)
