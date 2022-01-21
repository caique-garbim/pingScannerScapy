#!/usr/bin/python

# Importa a biblioteca Sys e Scapy
import sys
from scapy.all import *

# Caso o usuario nao informar os 3 argumentos necessarios
if len(sys.argv) <= 3:
	print ("\n PING SCANNER - SCAPY \n")
	print (" [*] Modo de uso: ")
	print ("     Informe a rede sem o ultimo octeto, o host inicial (min: 1) e ")
	print ("     host final (max: 254).")
	print (" [*] Exemplo: ")
	print ("     python3 ping_scan_scapy.py 192.168.15 10 100")
else:
	# Verbose desativado (saida limpa)
	conf.verb = 0
	print ("\n PING SCANNER - SCAPY \n")

	# Soma +1 para fechar o range definido no arg 3
	sys.argv[3]=int(sys.argv[3])+1

	# Laço de repetiçao para criar o range da porta inicial-final. Converte os args em inteiros.
	for hosts in range(int(sys.argv[2]),int(sys.argv[3])):
		# Monta o IP alvo
		alvo = (str(sys.argv[1])+"."+str(hosts))
		# Define o IP destino conforme IP alvo. Converte em string
		pIP = IP(dst=str(alvo))
		# Monta o pacote ICMP (echo-request)
		pacote = pIP/ICMP()
		# Envia o pacote e salva resposta
		resp, noresp = sr(pacote,timeout=1)
		# Laço de repeticao que exibe somente os hosts que responderam (ativos)
		for resposta in resp:
			print (" [*] Host ativo: "+resposta[1][IP].src)
