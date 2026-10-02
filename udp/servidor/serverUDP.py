import socket
from bacbo import bacbo

HOST = '127.0.0.1'
PORT = 1210

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("Rodando...")

while True:
    message, client_address = server_socket.recvfrom(2048)
    aposta = message.decode('utf-8').strip().lower()
    
    opcoes = ['jogador', 'casa', 'empate']
    
    if aposta not in opcoes:
        resposta = "Aposta invalida! Digite apenas: jogador, casa ou empate."
    else:
        resposta = bacbo(aposta)
        
    server_socket.sendto(resposta.encode('utf-8'), client_address)