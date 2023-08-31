contract_address = '0xCBE2093030F485adAaf5b61deb4D9cA8ADEAE509'

# уровень газа с которым сравниваем
good_gas = 15

# временные интервалы для sleep между кошельками
timer_start = 30 # минут
timer_end = 50 # минут

# на скольки итерациях остановиться, если делать на все приватники, то напишите тут хоть 1000000
counter_finish = 100
# rpc сети
zksync_rpc = 'https://mainnet.era.zksync.io'

# миксуем приватники, если да, то True, если нет то False
randomize_keys = True
# если нужно брать из файла, то пишем True, если генерация рандомных символово, то False
names_from_file = True