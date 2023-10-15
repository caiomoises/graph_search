import numpy as np
import math
from classes import *

SIZE = 167

# Função para alocar uma matriz
def alocaMatriz():
    matriz = np.zeros((SIZE, SIZE), dtype=float)
    return matriz

# Função para carregar os dados das cidades do RN
def RN():
    todasCidades = getCidades("database/cidades.csv")
    todosLocais = getGps("database/coordenada.csv")

    data_items = []

    for cidade_info in todasCidades:
        cidade = Cidade(cidade_info.id, cidade_info.estado, cidade_info.cidade)
        for local_info in todosLocais:
            if cidade_info.id == local_info.id:
                gps = GPS(local_info.id, local_info.la, local_info.lo)
                data_item = DataItem(cidade, gps)
                data_items.append(data_item)

    return data_items

# Função para criar uma matriz (grafo)
def criarGrafo():
    matriz = alocaMatriz()
    return matriz

# Função para calcular distâncias e preencher o grafo
def calculaDistancia(matriz, informacoesRN, Distancia):
    for i in range(SIZE):
        for j in range(i + 1):
            if i == j:
                matriz[i][j] = -1
            else:
                dist = math.sqrt((informacoesRN[i].GPS.la - informacoesRN[j].GPS.la)**2 + (informacoesRN[i].GPS.lo - informacoesRN[j].GPS.lo)**2)

                if dist < Distancia:
                    matriz[i][j] = dist
                    matriz[j][i] = dist
                else:
                    matriz[i][j] = -1
                    matriz[j][i] = -1
    return matriz

# Função para imprimir a cidade com mais vizinhos
def printCidadeComMaisVizinhos(matriz, informacoesRN, Distancia):
    results = [0, 0]

    for i in range(SIZE):
        cont = 0

        for j in range(SIZE):
            if matriz[i][j] > 0:
                cont += 1

        if cont > results[1]:
            results[0] = i
            results[1] = cont

    if results[1] > 0:
        print(" %s tem %d vizinhas!!!\n" % (informacoesRN[results[0]].city.cidade, results[1]))


# Função para imprimir cidades sem vizinhos
def printCidadeSemVizinhos(matriz, informacoesRN, Distancia):
    for i in range(SIZE):
        has_neighbor = False

        for j in range(SIZE):
            if matriz[i][j] >= 0:
                has_neighbor = True
                break

        if not has_neighbor:
            print("\n\t %s tem 0 vizinhas!!!\n\n" % informacoesRN[i].city.cidade)
            break
    else:
        print("\n\t Não há cidades sem vizinhas!!!\n\n")

# Função para imprimir a distância necessária para todas serem vizinhas
def printDistTodasVizinhas(informacoesRN):
    maior = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if i != j:
                dist = math.sqrt((informacoesRN[i].GPS.la - informacoesRN[j].GPS.la)**2 + (informacoesRN[i].GPS.lo - informacoesRN[j].GPS.lo)**2)

                if dist > maior:
                    maior = dist

    print("\nÉ necessario que a distancia seja de %.5f para que todas sejam vizinhas!!!\n" % maior)

# Função para imprimir a distância necessária para nenhuma ser vizinha
def printDistMinTodasVizinhas(informacoesRN):
    maior = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if i != j:
                dist = math.sqrt((informacoesRN[i].GPS.la - informacoesRN[j].GPS.la)**2 + (informacoesRN[i].GPS.lo - informacoesRN[j].GPS.lo)**2)

                if dist > maior:
                    maior = dist

    print("\nA maior distância entre duas cidades vizinhas é: %.5f km\n" % maior)

# Função para imprimir a distância necessária para todas serem vizinhas
def printDistMaxNenhumVizinhas(informacoesRN):
    menor = 100

    for i in range(SIZE):
        for j in range(SIZE):
            if i != j:
                dist = math.sqrt((informacoesRN[i].GPS.la - informacoesRN[j].GPS.la)**2 + (informacoesRN[i].GPS.lo - informacoesRN[j].GPS.lo)**2)

                if dist < menor:
                    menor = dist

    print("\nA menor distância para que uma cidade tenha algum vizinho é: %.5f km\n" % menor)

# Função para imprimir a matriz do grafo
def printGrafoMatricial(matriz):
    for i in range(SIZE):
        print("\n")
        for j in range(SIZE):
            if matriz[i][j] == -1:
                print("%.0f\t" % matriz[i][j], end="")
            else:
                print("%.3f\t" % matriz[i][j], end="")

        print("\n\n")
