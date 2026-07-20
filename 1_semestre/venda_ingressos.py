import os

Nomes =[] 
Cpfs = []
Ingressos_vend = []
Vendas = []

inteira = 40
meia = inteira / 2
ingressos = 500
senha_adm = 'brasilhexa'

def limpar_tela():
    os.system('cls')

def pausar():
    input('PRESSIONE [ENTER] PARA CONTINUAR...')

while True:
    limpar_tela()
    print('========== VENDAS DE INGRESSOS =========')
    print('| [1] - VENDER INGRESSOS               |')
    print('| [2] - EXIBIR TODAS AS VENDAS         |')
    print('| [3] - ALTERAR VALOR DA SESSÃO        |')
    print('| [0] - SAIR                           |')
    print('========================================')
    op = int(input('>: '))
    if op == 1:
        Compras = []
        Ingressos = []
        limpar_tela()
        print('========= VENDER  INGRESSOS ==========')
        print(f'|          INGRESSOS DISPONIVEIS: {ingressos} |')
        nome = input('| NOME: ')
        cpf = int(input('| CPF: '))
        while True:
            quant = int(input('| QUANTIDADE DE INGRESSOS: '))
            if quant < 0 or quant > ingressos:
                print('| QUANTIDADE FORA DO LIMITE! COMPRA NÃO REGISTRADA ')
                print(f'| {ingressos} DISPONÍVEIS - CADASTRE A VENDA NOVAMENTE.')
                pausar()          
            else:
                print('====== VALORES DA SESSÃO =======')
                print(f'| [1] - VENDER INTEIRA: R${inteira}  |'),
                print(f'| [2] - VENDER MEIA: R${meia}    |')
                print(f'| [3] - GRATUIDADE\n')
                op = int(input('QUAL TIPO DE VENDA?: \n'))
                if op == 1:
                    calculo = op * inteira
                    Compras.append(calculo)
                    print(f'COMPRA DE R${calculo} CONFIRMADA!')
                    print(f'TOTAL ATÉ O MOMENTO: R${sum(Compras)}')                           
                elif op == 2:
                    calculo = quant * meia
                    Compras.append(calculo)
                    print(f'COMPRA DE R${calculo} CONFIRMADA!') 
                    print(f'TOTAL ATÉ O MOMENTO: R${sum(Compras)}')  
                elif op == 3:
                    Vendas.append(0)
                    print('COMPRA GRATUIDADE CONFIRMADA!')   
                    print(f'TOTAL ATÉ O MOMENTO: R${sum(Compras)}')  
                comprar_mais = int(input('[1] - PARA VENDER MAIS // [0] - PARA FINALIZAR: > '))
                if comprar_mais == 0:
                    ingressos = ingressos - quant
                    Nomes.append(nome)
                    Cpfs.append(cpf)
                    Ingressos.append(quant)
                    print(f'VENDA PARA {nome} REGISTRADA COM SUCESSO!')
                    print(f'RESUMO: {quant} INGRESSOS - TOTAL R${calculo}\n')
                    pausar()
                    break
                elif comprar_mais == 1:
                    pausar()

                else:
                    print('OPÇÃO INVÁLIDA!!')

    elif op == 2:
        limpar_tela()
        print('====== EXIBIR VENDAS =======')
        if len(Cpfs) == 0:
            print('NENHUMA VENDA ATÉ O MOMENTO!\n')
            pausar()
        else:
            for i in range(len(Cpfs)):
                print(f'NOME: {Nomes[i]}')
                print(f'CPF: {Cpfs[i]}')
                print(f'Quantidade de ingressos comprados: {Ingressos[i]}')
                print(f'VALOR TOTAL DA COMPRA: R${Vendas[i]}')
                print('=======================')
            pausar()
    elif op == 3:
        senha = input('DIGITE A SENHA DO ADM: ')
        if senha != senha_adm:
            print('ACESSO NEGADO! SENHA INCORRETA')
            pausar()
        else:
            limpar_tela()
            print('====== VALORES DA SESSÃO =======')
            print(f'| VALOR INTEIRA: R${inteira}  |'),
            print(f'| VALOR MEIA: R${meia}  |\n')
            print('DESEJA FAZER ALTERAÇÃO NO VALOR DA INTEIRA?')
            op = input('s/n: ')
            if op == 'n':
                print('OK, VALORES MANTIDOS! ')
                pausar()
            elif op == 's':
                inteira = int(input('NOVO VALOR DA INTEIRA R$:'))
                print(f'VALOR DA INTEIRA ATUALIZADO PARA R${inteira}')
                pausar()


    elif op == 0:
        print('Saindo do sistema, até logo!')
        break
    else:
        print('OPÇÃO INVÁLIDA! ESCOLHA UMA OPÇÃO VÁLIDA')


