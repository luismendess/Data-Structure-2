vetor = [84, -55, -30, -7, -98, -5, 55,  1, -84, -88, 35, -59, 70, 62, 61]

tamanho_vetor = len(vetor)


def bubbleSort(vetor, tamanho_vetor):

    opcao = input('Insira a ordem desejada:\n1-Crescente\n2-Decrescente\n=> ')

    if opcao == '1':
        trocou = True
        while(trocou):
            trocou = False
            for i in range(tamanho_vetor-1):
                if vetor[i] > vetor[i+1]:
                    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                    trocou = True
        print('O vetor organizado crescentemente fica:')
        print(vetor)

    elif opcao == '2':
        trocou = True
        while(trocou):
            trocou = False
            for i in range(tamanho_vetor-1):
                if vetor[i] < vetor[i+1]:
                    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                    trocou = True
        print('O vetor organizado decrescentemente fica:')
        print(vetor)

    else:
        print('Opção inválida!!')


bubbleSort(vetor, tamanho_vetor)
