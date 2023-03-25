vetor = [84, -55, -30, -7, -98, -5, 55,  1, -84, -88, 35, -59, 70, 62, 61]


def MergeSort(vetor, inicio, fim):
    
    if (inicio < fim):
        meio = ((inicio+fim)/2)
        MergeSort(vetor, inicio, meio)
        MergeSort(vetor, meio+1, fim)
        Merge(vetor, inicio, meio, fim)
        
def Merge(vetor, esquerda, direita, meio, fim):
    
    vetor_auxiliar = []
    esquerda = vetor[:meio]
    direita = vetor[meio:]
    
    while (esquerda <= meio and direita <= fim):
        if (vetor[esquerda] < vetor[direita]):
            vetor_auxiliar.append(vetor[esquerda])
            esquerda += 1
        elif (vetor[direita] < vetor[esquerda]):
            vetor_auxiliar.append(vetor[direita])
            direita += 1
        if (esquerda == meio):
            vetor_auxiliar.append(direita)
        else:
            vetor_auxiliar.append(esquerda)
    vetor = vetor_auxiliar
    
tamanho_vetor = len(vetor)
meio = tamanho_vetor/2
    
MergeSort(vetor, 0, tamanho_vetor)

print(vetor)