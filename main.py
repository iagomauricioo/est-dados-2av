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
    print('5. Registrar uma nova vendda')
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
            tamanho_estoque = len(estoque_de_produtos)
            produto = input("Produto que será adicionado ao estoque: ")
            estoque_de_produtos.append(produto)
            if tamanho_estoque < len(estoque_de_produtos):
                clear_console()
                print("\nProduto adicionado com sucesso!\n")
        case 2:
            tamanho_estoque = len(estoque_de_produtos)
            clear_console()
            for i, produto in enumerate(estoque_de_produtos):
                print(f"Produto {i}: {produto}")

            print("Qual produto deseja remover? (digite o nome)")
            produto_removido = input("R: ")
            if produto_removido in estoque_de_produtos:
                indice = estoque_de_produtos.index(produto_removido)
                estoque_de_produtos.pop(indice)
                clear_console()
            else:
                clear_console()
                print(f"Produto {produto_removido} não encontrado no estoque.")
        case 3:
            pedido = input("Seu pedido: ")
            pedidos_de_compra.enqueue(pedido)
            clear_console()
            print("\nPedido registrado!\n")
            
        case 4:
            estoque_remover = pedidos_de_compra[0]
            pedidos_de_compra.dequeue()
            estoque_de_produtos.pop(estoque_remover)
            print("Pedido processado. Estoque atualizado.")
        case 5:
            venda = input("")
            vendas.push()
        case 6:
            input()
        case 7:
            print('Encerrando...')
            break