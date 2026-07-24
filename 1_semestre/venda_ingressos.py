''' ATIVIDADE PROPOSTA:
Fazer um código para um sistema de vendas de ingresso.
Requisitos:
O sistema só tem 500 ingressos disponíveis
É preciso fazer o cadastro do comprador lendo Nome e CPF
Só é possível vender se houver a quantidade que o cliente deseja comprar.
É preciso mostrar na tela do menu, quantos ingressos estão disponíveis para venda.
O sistema precisa ter apenas as opções:
1. Vender ingresso
2. Exibir vendas
0. Sair '''

''' MEUS COMENTÁRIOS:
COMO TODA A ATIVIDADE EU SEMPRE BUSCO REALIZAR A PROPOSTA, E IMPLEMENTAR MAIS ALGUMAS FUNÇÕES DENTRO SISTEMA
ME FAZENDO CADA VEZ APRENDER E ME FORÇAR A USAR MINHA CRIATIVIDADE.
A PROPOSTA FOI SIMPLES E OBJETIVA DE CRIAÇÃO DE UM MENU, COM VENDA E EXIBIÇÃO.
EU TENTEI IR ALÉM ADICIONANDO: [FUNÇÕES DE ADM (MUDANÇA DE SENHA, MUDANÇA DE VALOR DE INGRESSO, RESUMO DE COMPRA MAIS DETALHADO)]
E VOU SEGUINDO ATUALIZANDO CADA VEZ DA MELHOR MANEIRA POSSÍVEL, ATÉ  RECEBER UMA NOVA ATIVIDADE PARA DESENVOLVER...
'''
#TESTE DE COMMIT

#EM DESENVOLVIMENTO

import os
#LISTAS
Nomes =[] 
Cpfs = []
Ingressos_vend = []
Vendas = []

#CONDICIONAIS
inteira = 40
meia = (inteira / 2)
ingressos = 500
senha_adm = 'brasilhexa'

#FUNCOES
def limpar_tela():
    os.system('cls')

def pausar():
    input('PRESSIONE [ENTER] PARA CONTINUAR...')

def pesquisar_cliente(cpf):
    if cpf in Cpfs:
        pos = Cpfs.index(cpf)
        print((f'Nome: {Nomes[pos]}'))
        print((f'CPF: {Cpfs[pos]}'))
        print((f'Ingressos Comprados: {Ingressos_vend[pos]}'))
        print((f'Valor: R${Vendas[pos]}'))
        return pos

    else:
        print('CLIENTE NÃO ENCONTRADO! ')

# MENU PRINCIPAL
while True:
    limpar_tela()
    print('========== VENDAS DE INGRESSOS =========')
    print('| [1] - VENDER INGRESSOS               |')
    print('| [2] - EXIBIR TODAS AS VENDAS         |')
    print('| [3] - PESQUISAR CLIENTE              |')
    print('| [4] - AREA DO ADM                    |')
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
        print('=======================================')
        while True:
            quant = int(input('\n| QUANTIDADE DE INGRESSOS: > '))
            if quant < 0 or quant > ingressos:
                print('| QUANTIDADE FORA DO LIMITE! COMPRA NÃO REGISTRADA ')
                print(f'| {ingressos} DISPONÍVEIS - CADASTRE A VENDA NOVAMENTE.')
                pausar()          
            else:
                print('\n====== VALORES DA SESSÃO =======')
                print(f'| [1] - VENDER INTEIRA: R${inteira}  |'),
                print(f'| [2] - VENDER MEIA: R${meia}    |')
                print(f'| [3] - GRATUIDADE')
                print('=================================\n')
                op = int(input('QUAL TIPO DE VENDA?: > '))
                if op == 1:
                    print('\n============================')
                    calculo = quant * inteira
                    Compras.append(calculo)
                    Ingressos.append(quant)
                    print(f'COMPRA DE R${calculo} CONFIRMADA!')
                    print(f'TOTAL ATÉ O MOMENTO: R${sum(Compras)}')      
                    print('============================')                     
                elif op == 2:
                    print('\n============================')
                    calculo = quant * meia
                    Compras.append(calculo)
                    Ingressos.append(quant)
                    print(f'COMPRA DE R${calculo} CONFIRMADA!') 
                    print(f'TOTAL ATÉ O MOMENTO: R${sum(Compras)}')  
                    print('============================\n')
                elif op == 3:
                    print('\n============================')
                    Ingressos.append(quant)
                    print('COMPRA GRATUIDADE CONFIRMADA!')   
                    print(f'TOTAL ATÉ O MOMENTO: R${sum(Compras)}')  
                    print('============================\n')
                comprar_mais = int(input('\n[1] - PARA VENDER MAIS // [0] - PARA FINALIZAR: > '))
                limpar_tela()
                if comprar_mais == 0:
                    ingressos = ingressos - sum(Ingressos)
                    Nomes.append(nome)
                    Cpfs.append(cpf)
                    Ingressos_vend.append(sum(Ingressos))
                    Vendas.append(sum(Compras))
                    print('============== RESUMO DA COMPRA ===============')
                    print(f'\nVENDA PARA {nome} REGISTRADA COM SUCESSO!')
                    print(f'RESUMO: {sum(Ingressos)} INGRESSOS - TOTAL R${sum(Compras)}')
                    print('================================================\n')
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
                print(f'Quantidade de ingressos comprados: {Ingressos_vend[i]}')
                print(f'VALOR TOTAL DA COMPRA: R${Vendas[i]}')
                print('=======================')
            pausar()

    elif op == 3:
        limpar_tela()
        print('==== PESQUISAR CLIENTE ====')
        cpf = input('CPF DO CLIENTE: ')
        pesquisar_cliente(cpf)
        pausar()

    elif op == 4:
        senha = input('DIGITE A SENHA DO ADM: ')
        if senha != senha_adm:
            print('ACESSO NEGADO! SENHA INCORRETA')
            pausar()
        else:
            limpar_tela()
            print('========== AREA DO ADM ===========')
            print(' [1] - ALTERAR VALORES DA SESSÃO |')
            print(' [2] - ALTERAR SENHA DO ADM      |')
            print(' [3] - PESQUISA DE VENDA DET.    |')
            print(' [0] - VOLTAR AO MENU            |')
            print('==================================\n')
            op = int(input('ESCOLHA UMA OPÇÃO: > '))
            if op == 1:
                limpar_tela()
                print('====== VALORES DA SESSÃO =======')
                print(f'| VALOR INTEIRA: R${inteira}  |'),
                print(f'| VALOR MEIA: R${meia}   |')
                print('==================================\n')
                print('DESEJA FAZER ALTERAÇÃO NO VALOR DA INTEIRA?')
                op = input('s/n: ')
                if op == 'n':
                    print('OK, VALORES MANTIDOS! ')
                    pausar()
                elif op == 's':
                    novo_valor = int(input('NOVO VALOR DA INTEIRA R$:'))
                    inteira = novo_valor
                    meia = inteira / 2
                    print(f'VALOR DA INTEIRA ATUALIZADO PARA R${inteira}')
                    pausar()
            elif op == 2:
                while True:
                    print('======== ALTERAR SENHA ==========\n')
                    atual = input('DIGITE A SENHA ATUAL: ')
                    if atual != senha_adm:
                        print('SENHA INCORRETA! TENTE NOVAMETE')
                    else:
                        nova_senha = input('DIGITE A NOVA SENHA: ')
                        confirme_senha = input('CONFRIME A SENHA: ')
                        if confirme_senha != nova_senha:
                            print('AS SENHAS NÃO COINCIDEM!')
                        else:
                            print('SENHA ALTERADA COM SUCESSO! RETORNANDO AO MENU.')
                            pausar()
                            senha_adm = nova_senha
                            break
            elif op == 3:
                print('EM MANUTENÇÃO!!')
                pausar()
            else:
                print('OPÇÃO INVÁLIDA! ESCOLHA UMA OPÇÃO VÁLIDA.')
                pausar()
    elif op == 0:
        print('Saindo do sistema, até logo!')
        break
    else:
        print('OPÇÃO INVÁLIDA! ESCOLHA UMA OPÇÃO VÁLIDA')


