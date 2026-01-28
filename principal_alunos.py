from pacman import *
import time

def obtem_direecao(ponto1, ponto2):
    theta = math.atan2(ponto1[1] - ponto2[1], ponto1[0] - ponto2[0])
    dir_x = math.cos(theta)
    dir_y = math.sin(theta)
    return dir_x, dir_y
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
def atualiza_pontos(estado_jogo):
    t.penup()
    x = estado_jogo['pacman']['objeto'].xcor() 
    y = estado_jogo['pacman']['objeto'].ycor()
    index = offset((x,y))
    if estado_jogo['mapa'][index] == 1:
        estado_jogo['score'] += 1
        estado_jogo['mapa'][index] = 7
        x, y = calcula_x_y_from_index(index)
        estado_jogo['marcador'].goto(x + 10,y + 10)
        estado_jogo['marcador'].dot(2,'blue')
        update_board(estado_jogo)   
def atualiza_mapa(estado_jogo, x, y, elemento):
    index = offset((x,y))
    while estado_jogo['mapa'][index] in [BLINKY_OBJECT, PINKY_OBJECT, INKY_OBJECT, CLYDE_OBJECT]:
        index += 1
    estado_jogo['mapa'][index] = elemento
def actualiza_posicao_pacman_fantasma(estado_jogo):
    x = estado_jogo['pacman']['objeto'].xcor() 
    y = estado_jogo['pacman']['objeto'].ycor()
    atualiza_mapa(estado_jogo, x, y, PACMAN_OBJECT)
    for ghost_id, ghost in estado_jogo['fantasmas'].items():
        x = ghost['objeto'].xcor()
        y = ghost['objeto'].ycor()
        atualiza_mapa(estado_jogo, x, y, ghost_id)

def pacman_cima(estado_jogo):
    estado_jogo['pacman']['direcao_atual']=DIRECOES_POSSIVEIS[0]
    pass    
def pacman_baixo(estado_jogo):
    estado_jogo['pacman']['direcao_atual']=DIRECOES_POSSIVEIS[1]
    pass
def pacman_direita(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = DIRECOES_POSSIVEIS[2]
    pass
def pacman_esquerda(estado_jogo):
    estado_jogo['pacman']['direcao_atual']=DIRECOES_POSSIVEIS[3]
    pass

def movimenta_clyde(estado_jogo):
    scatter_distance_threshold = 50
    scatter_corner_index = 0
    pacman_pos = estado_jogo['pacman']['objeto'].pos()
    clyde_pos = estado_jogo['fantasmas'][CLYDE_OBJECT]['objeto'].pos()
    clyde_x,clyde_y = clyde_pos
    pacman_x,pacman_y = pacman_pos
    dist_pacman = calculate_distance(pacman_pos,clyde_pos)
    movs = []
    if dist_pacman > scatter_distance_threshold:
        if abs(pacman_x - clyde_x) > abs(pacman_y - clyde_y):
            movs.append((5, 0) if pacman_x > clyde_x else (-5, 0))
            movs.append((0, 5) if pacman_y > clyde_y else (0, -5))
        else:
            movs.append((0, 5) if pacman_y > clyde_y else (0, -5))
            movs.append((5, 0) if pacman_x > clyde_x else (-5, 0))

        for direcao in DIRECOES_POSSIVEIS:
            if direcao not in movs:
                movs.append(direcao)

        for direcao in movs:
            nova_pos = (clyde_x + direcao[0], clyde_y + direcao[1])
            if movimento_valido(nova_pos, estado_jogo):
                estado_jogo['fantasmas'][CLYDE_OBJECT]['direcao_atual'] = direcao
                return direcao
    else:

        if abs(pacman_x - clyde_x) > abs(pacman_y - clyde_y):
            movs.append((5, 0) if pacman_x < clyde_x else (-5, 0))
            movs.append((0, 5) if pacman_y < clyde_y else (0, -5))
        else:
            movs.append((0, 5) if pacman_y < clyde_y else (0, -5))
            movs.append((5, 0) if pacman_x < clyde_x else (-5, 0))

        for direcao in DIRECOES_POSSIVEIS:
            if direcao not in movs:
                movs.append(direcao)

        for direcao in movs:
            nova_pos = (clyde_x + direcao[0], clyde_y + direcao[1])
            if movimento_valido(nova_pos, estado_jogo):
                estado_jogo['fantasmas'][CLYDE_OBJECT]['direcao_atual'] = direcao
                return direcao

    estado_jogo['fantasmas'][CLYDE_OBJECT]['direcao_atual'] = (0, 0)
    return (0, 0)
def movimenta_pinky(estado_jogo):
    pinky_pos = estado_jogo['fantasmas'][PINKY_OBJECT]['objeto'].pos()
    pacman_pos = estado_jogo['pacman']['objeto'].pos()
    
    pacman_x, pacman_y = pacman_pos
    pinky_x, pinky_y = pinky_pos
    
    movs = []

    if abs(pacman_x - pinky_x) > abs(pacman_y - pinky_y):
        movs.append((5, 0) if pacman_x > pinky_x else (-5, 0))
        movs.append((0, 5) if pacman_y > pinky_y else (0, -5))
    else:
        movs.append((0, 5) if pacman_y > pinky_y else (0, -5))
        movs.append((5, 0) if pacman_x > pinky_x else (-5, 0))

    for direcao in DIRECOES_POSSIVEIS:
        if direcao not in movs:
            movs.append(direcao)

    for direcao in movs:
        nova_pos = (pinky_x + direcao[0], pinky_y + direcao[1])
        if movimento_valido(nova_pos, estado_jogo):
            estado_jogo['fantasmas'][PINKY_OBJECT]['direcao_atual'] = direcao
            return direcao
        

    estado_jogo['fantasmas'][PINKY_OBJECT]['direcao_atual'] = (0, 0)
    return (0, 0)
def movimenta_inky(estado_jogo):
    estado_jogo['fantasmas'][INKY_OBJECT]['direcao_atual']
    inky = random.choice(DIRECOES_POSSIVEIS)
    return inky
    pass
def movimenta_blinky(estado_jogo):
    estado_jogo['fantasmas'][BLINKY_OBJECT]['direcao_atual']
    Blinky = random.choice(DIRECOES_POSSIVEIS)
    return Blinky
    pass

def perdeu_jogo(estado_jogo):
    pacman_ = estado_jogo['pacman']['objeto']
    for ghost_id, ghost in estado_jogo['fantasmas'].items():
        if ha_colisao(pacman_, ghost['objeto']):
            terminar_jogo(estado_jogo)
            pass
def vence_jogo(estado_jogo):
    pontuacao = estado_jogo['score']
    if pontuacao==155: #155 é o numero total de pontos 
        terminar_jogo(estado_jogo)
        print('Venceste!!!')

def guarda_jogo(estado_jogo):
    actualiza_posicao_pacman_fantasma(estado_jogo)
    arquivo=open('save.txt','w')
    arquivo.write(f"{estado_jogo['score']}\n")
    for i in range(0, len(estado_jogo['mapa']), 20):
        str_mapa = ""
        for elemento in estado_jogo['mapa'][i:i+20]:
            str_mapa += str(elemento) + ","
        str_mapa = str_mapa[:-1]
        arquivo.write(str_mapa + "\n")
    return True
def carrega_jogo(estado_jogo, nome_ficheiro):
    mp_save=open(nome_ficheiro,"r")
    if nome_ficheiro=='save.txt': 
        linha=mp_save.readline() 
        score_salvo = int(linha)
        if score_salvo != 0:
            estado_jogo['score'] = score_salvo
    mapa_og = mp_save.read()
    mapa_og = mapa_og.replace(",", " ")
    mapa_og = mapa_og.split()
    mapa=[]
    for i in mapa_og:
        mapa.append(int(i[0]))
    mp_save.close()
    estado_jogo['mapa']=mapa

if __name__ == '__main__':
    funcoes_jogador = {'pacman_cima': pacman_cima, 'pacman_baixo': pacman_baixo, 'pacman_esquerda': pacman_esquerda, 'pacman_direita': pacman_direita, 'guarda_jogo' : guarda_jogo, 'carrega_jogo' : carrega_jogo}    
    funcoes_fantasmas = {BLINKY_OBJECT : movimenta_blinky, PINKY_OBJECT : movimenta_pinky, INKY_OBJECT : movimenta_inky, CLYDE_OBJECT : movimenta_clyde}

  ##dicionario com as funcoes de movimento dos jogadores

    nome_ficheiro = input('Pretende carregar um mapa (Enter para carregar o mapa default/ "save" para abrir o mapa do ultimo save): ')
    if nome_ficheiro == "save":
        nome_ficheiro = 'save.txt'
    else:
        nome_ficheiro = 'mapa_inicial.txt'
        
    #funções de inicio do jogo
    estado_jogo = init_state()
    carrega_jogo(estado_jogo, nome_ficheiro)    
    setup(estado_jogo, True, funcoes_jogador,funcoes_fantasmas)
    t.hideturtle()
    #inicia_jogo(estado_jogo)

    #Ate o jogador perder nao executa isso---> quando perder executa isso 
    while not perdeu_jogo(estado_jogo):
        if estado_jogo['mapa'] is not None:
            estado_jogo['janela'].update() #actualiza a janela
            movimenta_objectos(estado_jogo)
            atualiza_pontos(estado_jogo)
            vence_jogo(estado_jogo)
            time.sleep(0.05)