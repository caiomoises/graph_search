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
    todasCidades = Cidade("bancoDeDados/cidades.csv")
    todosLocais = GPS("bancoDeDados/coordenada.csv")

    d = DataItem(todasCidades, todosLocais)

    cidadesDoRN = [None] * 167

    k = 0

    for i in range(5570):
        if d[i].city.estado == "RN":
            cidadesDoRN[k] = d[i]
            k += 1

    return cidadesDoRN

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

    print("\n\t\t %s\t tem %d vizinhas!!!\n\n" % (informacoesRN[results[0]].city.cidade, results[1]))

# Função para imprimir cidades sem vizinhos
def printCidadeSemVizinhos(matriz, informacoesRN, Distancias):
    for i in range(SIZE):
        has_neighbor = False

        for j in range(SIZE):
            if matriz[i][j] >= 0:
                has_neighbor = True
                break

        if not has_neighbor:
            print("\n\t %s e tem 0 vizinhas!!!\n\n" % informacoesRN[i].city.cidade)
            break
    else:
        print("\n\t Nao ha cidades sem vizinhas!!!\n\n")

# Função para imprimir a distância necessária para todas serem vizinhas
def printDistTodasVizinhas(informacoesRN):
    maior = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if i != j:
                dist = math.sqrt((informacoesRN[i].GPS.la - informacoesRN[j].GPS.la)**2 + (informacoesRN[i].GPS.lo - informacoesRN[j].GPS.lo)**2)

                if dist > maior:
                    maior = dist

    print("\nEh necessario que a distancia seja de %.5f para que todas sejam vizinhas!!!\n" % maior)

# Função para imprimir a distância necessária para nenhuma ser vizinha
def printDistMinTodasVizinhas(informacoesRN):
    maior = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if i != j:
                dist = math.sqrt((informacoesRN[i].GPS.la - informacoesRN[j].GPS.la)**2 + (informacoesRN[i].GPS.lo - informacoesRN[j].GPS.lo)**2)

                if dist > maior:
                    maior = dist

    print("\nEh necessario que a distancia seja de %.5f para que nenhuma seja vizinhas!!!\n" % maior)

# Função para imprimir a distância necessária para todas serem vizinhas
def printDistMaxNenhumVizinhas(informacoesRN):
    menor = 100

    for i in range(SIZE):
        for j in range(SIZE):
            if i != j:
                dist = math.sqrt((informacoesRN[i].GPS.la - informacoesRN[j].GPS.la)**2 + (informacoesRN[i].GPS.lo - informacoesRN[j].GPS.lo)**2)

                if dist < menor:
                    menor = dist

    print("\nEh necessaria que a distancia seja de %.5f para que todas sejam vizinhas!!!\n\n" % menor)

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
