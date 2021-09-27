class Nodo():

    #contrutor do nodo, cada nodo contém a informação do nodo pai. 
    # Contém a informação da posição na matriz, através da tupla (x,y)
    #Os elementos da função heurística f(n) = g(n) + h(n)
    def __init__(self, pai=None, posicao=None):
        self.pai = pai
        self.posicao = posicao

        self.g = 0
        self.h = 0
        self.f = 0
    #função de comparação entre posições
    def __eq__(self, other):
        return self.posicao == other.posicao



def astar(labirinto, inicio, fim):
    linhas, colunas = len(labirinto), len(labirinto[0])
    visitados = [[False] * colunas for _ in range(linhas)]

    #inicializado os nodos com a posição deles na matriz
    #zerando os elementos da função heuristica
    nodo_inicial = Nodo(None, inicio)
    nodo_inicial.g = nodo_inicial.h = nodo_inicial.f = 0
    nodo_final = Nodo(None, fim)
    nodo_final.g = nodo_final.h = nodo_final.f = 0

    #criando a lista aberta e lista fechada
    lista_aberta = []
    lista_fechada = []

    #Adicionando o nodo incial na lista aberta
    lista_aberta.append(nodo_inicial)

    #faz o laço enquanto tiverem itens na lista aberta
    while len(lista_aberta) > 0:

        nodo_atual = lista_aberta[0]
        indice_atual = 0
        for indice, item in enumerate(lista_aberta):
            if item.f < nodo_atual.f:
                nodo_atual = item
                indice_atual = indice
        #tirando o nodo com o indice da lista aberta
        #inserindo na lista fechada
        lista_aberta.pop(indice_atual)
        lista_fechada.append(nodo_atual)

        #Quando encontra o nodo final
        #analisa o caminho percorrdo pegando do nodo final
        #ao nodo inicial e retornando a lista invertida
        if nodo_atual == nodo_final:
            caminho = []
            atual = nodo_atual
            while atual is not None:
                caminho.append(atual.posicao)
                visitados[atual.posicao[0]][atual.posicao[1]] = True
                atual = atual.pai
            print('Vetor de visitados: ')
            for i in visitados:
                print(i)
            return caminho[::-1] 

        #gerando os filhos a partir das adjacencias, caminhos possiveis
        filhos = []
        for nova_posicao in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #direções possiveis. CIMA, BAIXO, ESQUERDA, DIREITA

            #Pegando a posição do nodo
            posicao_nodo = (nodo_atual.posicao[0] + nova_posicao[0], nodo_atual.posicao[1] + nova_posicao[1])

            #verificando se a posição do nodo respeita os limites da matriz
            if posicao_nodo[0] > (len(labirinto) - 1) or posicao_nodo[0] < 0 or posicao_nodo[1] > (len(labirinto[len(labirinto)-1]) -1) or posicao_nodo[1] < 0:
                continue

            #Se encontrar uma posição diferente de 0, ou seja 1=>parede, continua
            #procurando um próximo nodo livre
            if labirinto[posicao_nodo[0]][posicao_nodo[1]] != 0:
                continue

            #criando um novo nodo, sendo o nodo qu já foi analisado sendo o 
            #pai e passando a posicao 
            nodo_novo = Nodo(nodo_atual, posicao_nodo)

          
            filhos.append(nodo_novo)

     
        for filho in filhos:

      
            for filho_fechado in lista_fechada:
                if filho == filho_fechado:
                    continue

            filho.g = nodo_atual.g + 1 #o nodo filho como g é a distancia do nodo até seu pai
                                      #Simplismente é feito a soma de um num acumulado de g
            filho.h = ((filho.posicao[0] - nodo_final.posicao[0]) ** 2) + ((filho.posicao[1] - nodo_final.posicao[1]) ** 2)
            #como heuristica aplicada, foi utilizado a distancia euclidiana: 
            # A Distância Euclidiana é definida como a soma da raiz quadrada da diferença entre x e y em suas respectivas dimensões.
            #Sendo uma linha reta até o destino
            filho.f = filho.g + filho.h # f(n) = g(n) + h(n)

            for i in range(len(lista_aberta)) :
                if filho == lista_aberta[i] and filho.g > lista_aberta[i].g:
                    continue
                if filho == lista_aberta[i] and filho.g < lista_aberta[i].g:
                    lista_aberta[i].g = filho.g 
                    lista_aberta[i].h = filho.h 
                    lista_aberta[i].pai = nodo_atual 
                    continue

          
            lista_aberta.append(filho)

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

    caminho = astar(labirinto, inicio, fim)
    print(caminho)

if __name__ == '__main__' :
    main()

    