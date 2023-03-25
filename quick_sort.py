def Particiona(vetor, inicio, fim):

    pivo = vetor[inicio]
    esquerda = inicio
    direita = fim

    while (esquerda < direita):
        while (vetor[esquerda] <= pivo and esquerda <= fim):
            esquerda += 1
        while (vetor[direita] > pivo and direita >= inicio):
            direita -= 1
        if (esquerda < direita):
            vetor[esquerda], vetor[direita] = vetor[direita], vetor[esquerda]

        vetor[direita], vetor[inicio] = vetor[inicio], vetor[direita]

    return direita


def QuickSort(vetor, inicio, fim):
    
    if (inicio < fim):
        pivo = Particiona(vetor, inicio, fim)
        QuickSort(vetor, inicio, pivo-1)
        QuickSort(vetor, pivo+1, fim)


vetor = [84, -55, -30, -7, -98, -5, 55,  1, -84, -88, 35, -59, 70, 62, 61]

tamanho_vetor = len(vetor)

QuickSort(vetor, 1, tamanho_vetor)
print(vetor)
