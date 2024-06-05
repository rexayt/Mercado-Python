from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('='*70)
    print(' Bem-vindo(a) '.center(70, '='))
    print(' Geek Shop '.center(70, '='))
    print('='*70, end='\n\n')

    print('Selecione uma opção abaixo:')
    opcao: int = int(input('1 - Cadastrar produto \n2 - Listar produtos\n3 - Comprar Produto\n4 - Visualizar carrinho\n5 - Fechar pedido\n6 - Sair do sistema\nResposta: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!\n')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    print()
    print('Cadastro de produto'.center(70,'='))
    print('-'*70)

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos'.center(70,'='))
        for produto in produtos:
            print(f'{produto}')
            print('-'*70)
    else:
        print('Sem produtos cadastrados.\n')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Produtos disponíveis'.center(70, '='))
        for produto in produtos:
            print(produto)
            print('-'*70)
            sleep(1)
        codigo: int = int(input('Informe o código do produto que deseja adicionar ao carrinho: '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O pdoruto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print()
        print('-'*70)
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-'*70)
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print()
        print('-'*70)
        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-'*70)
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)

    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()