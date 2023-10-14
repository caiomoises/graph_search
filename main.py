from grafo import *
import random

if __name__ == "__main__":
    G = criarGrafo()
    InfosBrasil = RN()

    while True:
        D = [random.uniform(0.05, 1) for _ in range(1)]
        print("\tMENU")
        print("1 - GRAFO MATRICIAL")
        print("2 - CIDADE SEM VIZINHOS")
        print("3 - CIDADE COM VIZINHOS")
        print("4 - DISTANCIA MÁXIMO ENTRE VIZINHOS")
        print("5 - DISTANCIA MINIMO ENTRE VIZINHOS")
        print("6 - SAIR")

        op = input('Escolha uma das opções: ')

        if op == '1':
            for i in range(1):
                printGrafoMatricial(calculaDistancia(G, InfosBrasil, D[i]))
        
        if op == '2':
            for i in range(1):
                print(f'\nA cidade com menos vizinhos a uma distância de {D}km: ')
                printCidadeSemVizinhos(calculaDistancia(G, InfosBrasil, D[i]), InfosBrasil, D)
        
        if op == '3':
            for i in range(1):
                print(f'\nA cidade com mais vizinhos a uma distância de {D}km: ')
                printCidadeComMaisVizinhos(calculaDistancia(G, InfosBrasil, D[i]), InfosBrasil, D[i])
        
        if op == '4':
            printDistMinTodasVizinhas(InfosBrasil)
        
        if op == '5':
            printDistMaxNenhumVizinhas(InfosBrasil)
        
        if op == '6':
            print('Até mais!')
            break