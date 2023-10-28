from datetime import date
import time

print('''  ____       _      _____   _____   _____   ___   __  __   _____ 
 |  _ \     / \    |_   _| | ____| |_   _| |_ _| |  \/  | | ____|
 | | | |   / _ \     | |   |  _|     | |    | |  | |\/| | |  _|  
 | |_| |  / ___ \    | |   | |___    | |    | |  | |  | | | |___ 
 |____/  /_/   \_\   |_|   |_____|   |_|   |___| |_|  |_| |_____|
                                                                 
	''')
print('AGUARDE...')
time.sleep(5)


xprozy = date.today().year

xprozy2 = int(input('EM QUE ANO VOCE NASCEU? :'))

xprozy3 = xprozy - xprozy2

if xprozy3 <= 14:
	print('voce e muito novo volte mais tarde!')
	print(input('aguarde a idade certa ok! >>click enter para finalizar.'))
	print('''DESENVOLVIDO POR:
[!]ZIIP
[!]INSTAGRAM: @ziip_019]
[!]GIT HUB: https://github.com/ziippk''')
	exit()

print('voce tem {} anos'.format(xprozy3))

print('voce foi aprovado!')
print('''DESENVOLVIDO POR:
[!]ZIIP
[!]INSTAGRAM: @ziip_019]
[!]GIT HUB: https://github.com/ziippk''')
