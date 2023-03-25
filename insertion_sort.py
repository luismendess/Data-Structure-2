vetor = [84, -55, -30, -7, -98, -5, 55,  1, -84, -88, 35, -59, 70, 62, 61]


def insertionSort(vetor):
    # solicita o tipo de ordenação do vetor
    opcao = input('Insira a ordem desejada:\n1-Crescente\n2-Decrescente\n=> ')

    if opcao == '1':
        for troca in range(1, len(vetor)):
            aux = vetor[troca]
            i = troca - 1

            while i >= 0 and aux < vetor[i]:
                vetor[i + 1] = vetor[i]
                i = i - 1

            vetor[i + 1] = aux
        print('O vetor organizado crescentemente fica:')
        print(vetor)

    elif opcao == '2':
        for troca in range(1, len(vetor)):
            aux = vetor[troca]
            i = troca - 1

            while i >= 0 and aux > vetor[i]:
                vetor[i + 1] = vetor[i]
                i = i - 1

            vetor[i + 1] = aux
        print('O vetor organizado decrescentemente fica:')
        print(vetor)

    else:
        print('Opção inválida!!')


insertionSort(vetor)
