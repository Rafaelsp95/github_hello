from decimal import Decimal

salario = float(input('Digite o seu salário desse mês:'))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

conta_internet = float(input('\nDigite o valor da conta de internet: '))
conta_luz = float(input('Digite o valor da conta de luz: '))
cartao_credito = float(input('Digite o valor da conta de cartão de crédito: '))

total_despesas = conta_luz + conta_internet + cartao_credito
print('\nAs despesas desse mês ficou no total de R$',total_despesas, 'reais.')

if salario >= total_despesas:
    print('Vai ser possível pagar as contas em', meses[4],'.')
else:
    print('Não vai ser possível pagar as contas em', meses[4],'.')

dinheiro_sobrado = salario - total_despesas
print('\nRestou uma quantia de R$', dinheiro_sobrado, 'reais para você gastar como quiser. Compre bitcoin utilizando ao menos 20% do salário que sobrar, que equivale a R$', dinheiro_sobrado * 0.2, 'reais neste mês!')

total_despesas = Decimal('0.1')
dinheiro_sobrado = Decimal('0.1')


