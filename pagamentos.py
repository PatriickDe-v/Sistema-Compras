print('======= LOJA STRASSBURGER ========')
preço = float(input('Preço das compras:R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Selecione uma das opções acima: '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = preço / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Em quantas parcelas: '))
    parcela = total / totparc
    print(
        f'Sua compra será parcela em {totparc}x de R${parcela:.2f} COM JUROS.')
print(f'Sua compra de R${preço:.2f} vai custar no final R${total:.2f}')
