#sistema_completo.py
import os

# REPOSITÓRIOS ===============================
Nomes = []
Enderecos = []
Telefones = []
Cpfs = []

def limpar_tela():
    os.system('cls')


def pausar():
    input('[ENTER] para continuar... ')


def cadastrar_cliente(nome, end, tel, cpf):
    Nomes.append(nome)
    Enderecos.append(end)
    Telefones.append(tel)
    Cpfs.append(cpf)
    print(f'{nome} cadastrado com sucesso!')


def exibir_clientes():
    if len(Nomes) == 0:
        print('Não existem clientes cadastrados!')
    
    else:
        for i in range(len(Nomes)):
            print(f'Nome:     {Nomes[i]}')
            print(f'Endereço: {Enderecos[i]}')
            print(f'Telefone: {Telefones[i]}')
            print(f'CPF:      {Cpfs[i]}')
            print('-'*30)


def pesquisar_cliente(cpf):
    if cpf in Cpfs: #o cpf tá no repositório?
        pos = Cpfs.index(cpf)
        print(f'Nome:     {Nomes[pos]}')
        print(f'Endereço: {Enderecos[pos]}')
        print(f'Telefone: {Telefones[pos]}')
        print(f'CPF:      {Cpfs[pos]}')
        return pos
        
    else:
        print('Cliente não encontrado!')
    

def editar_cliente(cpf):
    pos = False
    pos = pesquisar_cliente(cpf)
    if pos != False:
        print('Digite o novo valor ou [ENTER] para manter.')
        novo_nome = input('Novo nome: ')
        novo_end = input('Novo endereço: ')
        novo_tel = input('Novo telefone: ')
        novo_cpf = input('Novo cpf: ')
        
        alterados = []
        if len(novo_nome) > 0:
            Nomes[pos] = novo_nome
            alterados.append('Nome')
        
        if len(novo_end) > 0:
            Enderecos[pos] = novo_end
            alterados.append('Endereço')
        
        if len(novo_tel) > 0:
            Telefones[pos] = novo_tel
            alterados.append('Telefone')
        
        if len(novo_cpf) > 0:
            Cpfs[pos] = novo_cpf
            alterados.append('CPF')
    
        if len(alterados) > 0:
           print(f'{alterados} alterados.') 


def deletar_cliente(cpf):
    pos = False
    pos = pesquisar_cliente(cpf)
    if pos != False:
        print('ATENÇÃO ESTA AÇÃO NÃO PODE SER DESFEITA')
        print('Tem certeza que deseja excluir o cliente?')
        acao = input('Digite [confirmo] para excluir: ')
        if acao == 'confirmo':
            del(Nomes[pos])
            del(Enderecos[pos])
            del(Telefones[pos])
            del(Cpfs[pos])
            print('Cliente removido da base de dados.')
        
        else:
            print('Cliente não excluído')
        
    
# Programa principal ===================================
while True:
    limpar_tela()
    print('|=[ CADASTRO 1.0 ] =====================|')
    print('| [1]- Cadastrar Cliente                |')
    print('| [2]- Exibir                           |')
    print('| [3]- Pesquisar                        |')
    print('| [4]- Editar                           |')
    print('| [5]- Excluir                          |')
    print('| [0]- Sair                             |')
    print('|=======================================|')
    print('                           Design by MRG')
    op = int(input('> '))
    
    if op == 1:
        limpar_tela()
        
        print('CADASTRAR novo cliente')
        n = input('Nome: ')
        e = input('Endereço: ')
        t = input('Telefone: ')
        c = input('CPF: ')
        cadastrar_cliente(n, e, t, c)
        
        pausar()
    
    elif op == 2:
        limpar_tela()
        print('EXIBIR Clientes\n')
        exibir_clientes()
        pausar()
    
    elif op == 3:
        limpar_tela()
        print('PESQUISAR Cliente')
        
        c = input('CPF do cliente: ')
        pesquisar_cliente(c)
                
        pausar()
    
    elif op == 4:
        limpar_tela()
        print('EDITAR Cliente\n')
        
        buscado = input('CPF do cliente: ')
        editar_cliente(buscado)
        
        pausar()
    
    elif op == 5:
        limpar_tela()
        print('EXCLUIR Cliente')
        
        buscado = input('CPF do cliente: ')
        deletar_cliente(buscado)
        
        pausar()
    
    elif op == 0:
        limpar_tela()
        print('SAINDO...')
        break
    
    else:
        print('Opção inválida')
        pausar()
