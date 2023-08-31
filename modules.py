from web3 import Web3
import json
import time
import random
import string
from config import *

# грузим abi
with open('abi.json') as file:
	abi_json = json.load(file)


# грузим приватники
with open('private_keys.txt', 'r') as file:
	lines = file.readlines()  # Read lines from the file
	# Remove newline characters from each line using list comprehension
	private_keys = [line.strip() for line in lines]
	if randomize_keys:
		random.shuffle(private_keys)



def get_name():
	# берем рандомное имя из файла
	if names_from_file:
		with open('names.txt', 'r') as file:
			lines = file.readlines()  # Read lines from the file
			# Remove newline characters from each line using list comprehension
			names_array = [line.strip() for line in lines]
			random_name = random.choice(names_array)
			return random_name
	# или генерируем длиной от 8 до 13 символов
	else:		
		min_length, max_length = 8, 13
		word_length = random.randint(min_length, max_length)
		random_word = ''.join(random.choice(string.ascii_letters) for _ in range(word_length))
		return random_word


def get_gas_price():
	mainnet_rpc = "https://eth.llamarpc.com/"
	w3 = Web3(Web3.HTTPProvider(mainnet_rpc))
	gas_price_wei = w3.eth.gas_price
	gas_price_gwei = w3.from_wei(gas_price_wei, 'gwei')
	print("Mainnet gas:", gas_price_gwei)
	return gas_price_gwei

def timer(total_secs):
	# Run until the timer reaches 0 
	while total_secs:
		mins, secs = divmod(total_secs, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		total_secs -= 1
	return
