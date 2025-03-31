nome = input('Insira seu nome aqui: ')

while True:


    print('')
    print(f'Bem vindo ao menu {nome}!!!')
    print('')
    print('')
    print('Opção 1: Calcular sua média')
    print('Opção 2: Somar notas')
    print('Opção 3: Fazer a área de um retângulo')
    print('Opção 4: Fazer a área de um triângulo')
    print('Opção 5: Sair')
    print('')
    opcao = int(input(f'{nome}, informe a opção desejada: '))

    

    if(opcao==1):
        print('')
        n1 = float(input('Insira sua nota 1: '))
        n2 = float(input('Insira sua nota 2: '))
        n3 = float(input('Insira sua nota 3: '))
        n4 = float(input('Insira sua nota 4: '))
        media = (n1+n2+n3+n4)/4
        if(media>=6):
            print('')
            print(f'Parabéns, {nome} sua média é {media}, você está aprovado')
        elif(media<6):
            print('')
            print(f'Sua média é {media}, você está reprovado, estude mais {nome}!')


    elif(opcao==2):
        print('')
        n1 = float(input('Insira sua nota 1: '))
        n2 = float(input('Insira sua nota 2: '))
        n3 = float(input('Insira sua nota 3: '))
        n4 = float(input('Insira sua nota 4: '))
        soma = n1+n2+n3+n4
        print('')
        print(f'{nome}, a soma das notas é {soma}')


    elif(opcao==3):
        print('')
        base = float(input('Informe o valor da base do retângulo: '))
        altura = float(input('Informe o valor da altura do retângulo: '))
        areaR = base*altura
        print('')
        print(f'{nome}, o valor da área do retângulo é {areaR}')

    

    elif(opcao==4):
        print('')
        base = float(input('Informe o valor da base do triângulo: '))
        altura = float(input('Informe o valor da altura do triângulo: '))
        areaT = (base*altura)/2
        print('')
        print(f'{nome}, o valor da área do triângulo é {areaT}')


    elif(opcao==5):
        print('')
        print(f'Certo, você quer sair, tchau {nome}!')
        print('Saindo...')
        print('')
        print('Fim, obrigado por usar o menu de cálculo!')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        break

    else:
        print('')
        print('')
        print('')
        print('Opção inválida, tente novamente')
        print('')
        print('')
        print('')
        print('')
        print('')
