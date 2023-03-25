def selectionSort(vetor, tamanho_vetor):

    opcao = input('Insira a ordem desejada:\n1-Crescente\n2-Decrescente\n=> ')

    if opcao == '1':
        for posicao in range(tamanho_vetor):
            menor_indexador = posicao

            for i in range(posicao + 1, tamanho_vetor):

                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if vetor[i] < vetor[menor_indexador]:
                    menor_indexador = i

            # put min at the correct position
            (vetor[posicao], vetor[menor_indexador]) = (
                vetor[menor_indexador], vetor[posicao])
        print('Vetor organizado crescentemente: ')

    elif opcao == '2':
        for posicao in range(tamanho_vetor):
            menor_indexador = posicao

            for i in range(posicao + 1, tamanho_vetor):

                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if vetor[i] > vetor[menor_indexador]:
                    menor_indexador = i

            # put min at the correct position
            (vetor[posicao], vetor[menor_indexador]) = (
                vetor[menor_indexador], vetor[posicao])
        print('Vetor organizado decrescentemente: ')

    else:
        print('Opção inválida!!')


vetor = [84, -55, -30, -7, -98, -5, 55,  1, -84, -88, 35, -59, 70, 62, 61]

tamanho_vetor = len(vetor)

selectionSort(vetor, tamanho_vetor)

print(vetor)
