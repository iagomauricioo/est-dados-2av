import os


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])

    def __iter__(self):
        return iter(self.items)  
    
    def see_stack(self):
        for i, item in enumerate(self.items):
            print(f"{i + 1}º {item}")


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def see_queue(self):
        for i, item in enumerate(self):
            print(f"{i + 1}º {item}")


def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print("Sistema operacional não suportado. Não é possível limpar o console.")


estoque_de_produtos = []
pedidos_de_compra = Queue()
vendas = Stack()

while True:
    print('----------------------------------//----------------------------------')
    print('1. Adicionar um novo produto ao estoque')
    print('2. Remover um produto do estoque')
    print('3. Registrar um novo pedido de comprar')
    print('4. Processar um pedido de compra, removendo o produto do estoque')
    print('5. Registrar uma nova venda')
    print('6. Desfazer a última venda realizada, recolocando o produto no estoque')
    print('7. Encerrar programa')
    print('----------------------------------//----------------------------------')
    resposta = 0
    try:
        resposta = int(input('R: '))
    except ValueError:
        print('Digite apenas números (inteiros)')

    match resposta:
        case 1:
            produto = input("Produto que será adicionado ao estoque: ")
            estoque_de_produtos.append(produto)
            clear_console()
            print("\nProduto adicionado com sucesso!\n")

        case 2:
            clear_console()
            print("Produtos no estoque:")
            for i, produto in enumerate(estoque_de_produtos):
                print(f"{i+1}. {produto}")
            if estoque_de_produtos:
                try:
                    indice = int(
                        input("Digite o número do produto que deseja remover: ")) - 1
                    if 0 <= indice < len(estoque_de_produtos):
                        produto_removido = estoque_de_produtos.pop(indice)
                        clear_console()
                        print(f"Produto '{produto_removido}' removido do estoque.")
                    else:
                        print("Índice fora do intervalo válido.")
                except ValueError:
                    print("Digite um número válido.")
            else:
                print("Estoque vazio. Não há produtos para remover.")

        case 3:
            pedido = input("Informe o produto que deseja comprar: ")
            pedidos_de_compra.enqueue(pedido)
            clear_console()
            print(f"Pedido de '{pedido}' registrado.")

        case 4:
            clear_console()
            if not pedidos_de_compra.is_empty():
                produto_comprado = pedidos_de_compra.dequeue()
                if produto_comprado in estoque_de_produtos:
                    estoque_de_produtos.remove(produto_comprado)
                    print(
                        f"Pedido de compra para '{produto_comprado}' processado. Produto removido do estoque.")
                else:
                    print(f"Produto '{produto_comprado}' não encontrado no estoque.")
            else:
                print("Não há pedidos de compra para processar.")

        case 5:
            venda = input("Informe o produto vendido: ")
            if venda in estoque_de_produtos:
                vendas.push(venda)
                estoque_de_produtos.remove(venda)
                clear_console()
                print(f"Venda registrada para '{venda}'. Produto removido do estoque.")
            else:
                print("Produto não encontrado no estoque.")

        case 6:
            clear_console()
            if not vendas.isEmpty():
                produto_devolvido = vendas.pop()
                estoque_de_produtos.append(produto_devolvido)
                print(
                    f"Última venda de '{produto_devolvido}' desfeita. Produto devolvido ao estoque.")
            else:
                print("Não há vendas para desfazer.")

        case 7:
            print('Encerrando...')
            break
