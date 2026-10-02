import random

def bacbo(aposta):
    d1_jogador = random.randint(1, 6)
    d2_jogador = random.randint(1, 6)
    soma_jogador = d1_jogador + d2_jogador

    d1_casa = random.randint(1, 6)
    d2_casa = random.randint(1, 6)
    soma_casa = d1_casa + d2_casa
    
    if soma_jogador > soma_casa:
        vencedor = 'jogador'
    elif soma_casa > soma_jogador:
        vencedor = 'casa'
    else:
        vencedor = 'empate'
        
    resultado = (
        f"Jogador: [{d1_jogador}] + [{d2_jogador}] = {soma_jogador} | "
        f"Casa: [{d1_casa}] + [{d2_casa}] = {soma_casa} -> "
    )
    
    if aposta == vencedor:
        resultado += f"Deu {vencedor}! Voce GANHOU!"
    else:
        resultado += f"Deu {vencedor}! Nao foi dessa vez, mas voce sempre pode tentar de novo!"
        
    return resultado