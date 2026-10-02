import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1210

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("--- BAC BO ---")

while True:
    acao = input("\nEu sei que voce quer jogar, mas preciso que me confirme (S para Sim / N para Sair): ").strip().upper()
    
    if acao == 'N':
        print("\nQue pena...\nQuem sabe se voce nao poderia ter ganhado um trocado :/ \nAte a proxima!")
        break
        
    elif acao == 'S':
        aposta = input("\nFaca sua aposta (jogador, casa ou empate): ").strip().lower()
        
        client_socket.sendto(aposta.encode('utf-8'), (SERVER_HOST, SERVER_PORT))

        response, server_address = client_socket.recvfrom(2048)
        print(f"\nResultado: {response.decode('utf-8')}")
        
    else:
        print("Comando invalido! Digite apenas S ou N.")

client_socket.close()