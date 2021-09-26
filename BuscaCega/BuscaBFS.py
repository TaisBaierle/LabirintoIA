from collections import deque

def bfs(labirinto, inicio, fim):
    linhas, colunas = len(labirinto), len(labirinto[0]) #Pega as linhas e colunas da matriz
    if labirinto[inicio[0]][inicio[1]] !=0 or labirinto[fim[0]][fim[1]] !=0: #verifica se as coordenadas de entrada não são paredes
        return -1
    else:
        caminho = []
        #fila duplamente encadiada 
        queue = deque()
        #colocando as posições inicias no inicio da fila como uma tupla (x,y)
        queue.appendleft((inicio[0], inicio[1]))
        direcoes = [[0, 1], [0, -1], [1, 0], [-1, 0]]#vetor com as direções possíveis CIMA, BAIXO, ESQUERDA, DIREITA
        #vetor de visitados: Começando com todos os valores FALSE
        visitados = [[False] * colunas for _ in range(linhas)]

        while len(queue) != 0:
            #A operação pop() pode ser usada para remover o elemento do início
            coord = queue.pop() #pega a primeira coordenada
            visitados[coord[0]][coord[1]] = True #coloca como true na lista de visitados
            caminho.append(((coord[0]),coord[1])) #adiciona a lista no vetor de caminho

            if (coord[0],coord[1]) == fim: # se o final for encaontrado
                print('Vetor de visitados: ')
                for i in visitados:
                    print(i)
                return caminho
                #imprime o vetor de visitados mais o caminho percorrido

            for dir in direcoes: #pego as direções do vetor de direções possiveis
                novaLinha, novaColuna = coord[0]+dir[0], coord[1]+dir[1]#crio uma nova linha e uma nova coluna em cima dos valores das coordenadas avaliadas
                if (novaLinha < 0 or novaLinha >= linhas or novaColuna < 0 or novaColuna >= colunas or labirinto[novaLinha][novaColuna] == 1 or visitados[novaLinha][novaColuna]): 
                    continue# faz com que volte para o inicio da instrução de laço
                #faz uma validação geral para que não estrapole alguns limites, como por exemplo: As novas linhas e colunas não forem menores que 0, isso por que o indice -1
                #é fora do limite da matriz, a nova linha e nova coluna não podem ser maiores que a linha e coluna da matriz, ou já tenha sido visitado, ele volta e continua procurando
                queue.appendleft((novaLinha, novaColuna)) #coloca na fila a nova linha e coluna, e o laço se repete, até a fila ficar vazia
  

def main() :

    labirinto = [[0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
                [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1, 1, 0, 0]]

    for i in labirinto :
        print(i)

    print("Entre com a posicao inicial :")
    inicio = tuple(map(int, input().split()))

    print("Entre com a posição final :")
    fim = tuple(map(int, input().split()))

    caminho = bfs(labirinto, inicio, fim)
    if caminho == -1:
        print("Saída ou entrada não são possíveis")
    else:
        print(caminho)

if __name__ == '__main__' :
    main()

    