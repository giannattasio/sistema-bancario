menu = """"
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o Valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação negada! Informe um valor válido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do Saque:"))

        saldo_insuf = valor > saldo
        limite_insuf = valor > limite
        saques_insuf = numero_saques == LIMITE_SAQUE

        if saldo_insuf:
            print("Transação Negada, saldo insuficiente!")
        elif limite_insuf:
            print("Valor do saque excede limite!")
        elif saques_insuf:
            print("Você atingiu o limite de saques diarios!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação negada, informe um valor válido")

    elif opcao == "3":
        print("________ EXTRATO ________")
        print(
            "Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("Obrigado pela preferência, até logo!")
        break

    else:
        print("Opção invalida! Tente novamente")
