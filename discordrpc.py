import pypresence
import toml
import os
configfile = os.path.join('.','config.toml')

try:
	config = toml.load(configfile)
	print('成功載入' + configfile)
except:
	print(f"無法載入{configfile}")
	input()

def menu():
	print('如要退出請輸入"exit"或按右上角X')
	a = input()
	if a == 'exit':
		exit()
	else:
		menu()

def rpc():
	rpc = pypresence.Presence(config['rpcid']['id'])
	rpc.connect()
	rpc.update(state=config['contect']['state'],
	details=config['contect']['details'],
	large_image=config['contect']['large_image'],
	large_text=config['contect']['large_text'],
	small_image=config['contect']['small_image'],
	small_text=config['contect']['small_text'])

rpc()
print('RPC已啟動請查看Discord遊戲狀態')
menu()