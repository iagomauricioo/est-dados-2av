lista_de_produtos = []
fila_pedidos_de_compra = []
pilha_registro_de_vendas = []


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

            break
        case 2:

            break
        case 3:

            break
        case 4:

            break
        case 5:

            break
        case 6:

            break
        case 7:
            print('Encerrando...')
            break