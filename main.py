from grafo import *

def main():
    G = criarGrafo()
    
    InfosRN = RN()
    D = [0.05, 0.1, 0.15, 0.20, 0.25]

    for i in range(5):
        print(f"\n--- A cidade do RN com mais vizinhas com base na distancia de {D[i]:.2f} eh a seguinte. ---\n")
        printCidadeComMaisVizinhos(calculaDistancia(G, InfosRN, D[i]), InfosRN, D[i])

if __name__ == "__main__":
    main()
