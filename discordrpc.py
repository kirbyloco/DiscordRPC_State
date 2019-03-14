import pypresence

def menu():
	print('如要退出請輸入"exit"或按右上角X')
	a = input()
	if a == 'exit':
		exit()
	else:
		test()

rpc = pypresence.Presence(ClientID)
rpc.connect()
rpc.update(state="",
details="",
large_image="",
large_text="",
small_image="",
small_text="")

print('RPC已啟動請查看Discord遊戲狀態')
menu()

'''
rpc.update(state=format_state(data),
	details=format_details(data),
	start=format_start(data),
	large_image=format_large_image(data),
	large_text=format_large_text(data),
	small_image=format_small_image(data),
	small_text=format_small_text(data),
	party_size=format_party_size(data))'''