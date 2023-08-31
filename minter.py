from web3 import Web3
import requests
import datetime
from termcolor import cprint
import time
import json
import random
import sys
import traceback
import string
from eth_account import Account as EthereumAccount

from config import *
from modules import *

def mint_name(private_key):
	web3 = Web3(Web3.HTTPProvider(zksync_rpc))
	account = EthereumAccount.from_key(private_key)
	my_address = account.address
	print(my_address)
	now = datetime.datetime.now()
	now_dt = now.strftime("%d-%m-%Y %H:%M")
	contract = web3.eth.contract(Web3.to_checksum_address(contract_address), abi=abi_json)
	gas_price = int(web3.eth.gas_price*1.05)

	name = get_name()
	value = 0
	owner = my_address
	yearCount = 1


	# создание транзакции
	contract_txn = contract.functions.register(name, owner, yearCount).build_transaction({
		'from': my_address,
		'value': value, 
		'gasPrice': gas_price, 
		'nonce': web3.eth.get_transaction_count(my_address),
		})
	

	# Установка газлимита
	estimate = web3.eth.estimate_gas(contract_txn)
	gas_limit = estimate
	contract_txn['gas'] = gas_limit

	signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key)
	txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
	txn_text = txn_hash.hex()
	# берем из конфига txn explorer
	txn_explorer = 'https://explorer.zksync.io/tx/'
	cprint(f"\n{now_dt} {my_address} | УСПЕШНО tx {txn_explorer}{txn_text}", 'green')


counter = 0
for private_key in private_keys:
	# проверка, выполнен ли заказ по количеству или нет
	if counter == counter_finish:
		break

	try:
		# Ожидание низкой цены газа
		while True:
			gas_price = get_gas_price()
			if gas_price <= good_gas:  # если цена газа ниже или равна 20 Gwei
				break  # выходим из цикла ожидания   
			timer(20) # если газ выше нужного значения, то ждем 20 секунд

		# транзакция		
		mint_name(private_key)
		counter = counter + 1
		# сообщение
		message = f'zns.network mint success {counter} / {counter_finish}'
		print(message)

	# обработчик ошибок
	except Exception as e:
		traceback.print_exc()
		print('error:', str(e))
	#  переходим к следующей итерации с паузой
	timer(random.randint(timer_start*60, timer_end*60))
				
