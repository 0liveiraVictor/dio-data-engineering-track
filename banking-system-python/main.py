menu_options = """

Selecione uma opção válida para a operação bancária:

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair

>  """

WITHDRAWAL_LIMIT = 3
withdrawal_number = 0
bank_balance = 0
bank_withdrawal_limit = 500
extract = []

print("================ BANKING SYSTEM ================", end="")
while True:
    option = input(menu_options)

    if option == "0":
        print("")
        break
    
    elif option == "1":
        deposit_amount = float(input("\nInforme o valor a ser depositado: R$ "))
        if deposit_amount > 0:
            bank_balance += deposit_amount
            extract_dict = { "op": "1", "value": f"{deposit_amount:.2f}", "bank_balance": f"{bank_balance:.2f}" }
            extract.append(extract_dict)
            print(f"\n✔ - Depósito de R$ {deposit_amount:.2f} realizado com sucesso.", end="")
        else:
            print("\n✖ - Operação inválida. Verifique novamente o valor informado e tente novamente.", end="")
    
    elif option == "2":
        is_withdrawal_limit_exceeded = withdrawal_number >= WITHDRAWAL_LIMIT
        if is_withdrawal_limit_exceeded:             
            print("\n✖ - Operação não permitida! O limite de saques diários foi excedido.", end="")
        else:
            amount_withdrawn = float(input("\nInforme o valor a ser sacado: R$ "))
            if amount_withdrawn > 0:
                is_bank_withdrawal_limit_exceeded = amount_withdrawn > bank_withdrawal_limit
                if is_bank_withdrawal_limit_exceeded:
                    print(f"\n✖ - Operação não permitida! Valor do limite de saque excedido (máx. R$ {bank_withdrawal_limit:.2f}).", end="")
                else:
                    is_balance_exceeded = amount_withdrawn > bank_balance
                    if is_balance_exceeded:
                        print(f"\n✖ - Operação não permitida! Você não possui saldo suficiente (saldo atual: R$ {bank_balance:.2f}).", end="")
                    else:
                        bank_balance -= amount_withdrawn
                        extract_dict = { "op": "2", "value": f"{amount_withdrawn:.2f}", "bank_balance": f"{bank_balance:.2f}" }
                        extract.append(extract_dict)
                        withdrawal_number += 1
                        print(f"\n✔ - Saque de R$ {amount_withdrawn:.2f} realizado com sucesso.", end="")
            else:
                print("\n✖ - Operação inválida. Verifique novamente o valor informado e tente novamente.", end="")

    elif option == "3":
        print("\n_______________ BANK STATEMENT ________________\n")
        print("-----------------------------------------------")
        if len(extract) == 0:
            print("\nNão houve transações financeiras.\n")
            print("-----------------------------------------------")
        else:
            for element in extract:
                op_str = "Depósito" if element["op"] == "1" else "Saque"
                print(f"\nTipo de Operação: {op_str}")
                print(f"Valor de Transação: {element['value']}")
                print(f"Saldo Pós-Transação: {element['bank_balance']}\n")
                print("-----------------------------------------------")
        print("_______________________________________________")

    else:
        print("\n✖ - Operação inválida. Verifique novamente as opções permitidas abaixo.", end="")

print("================================================")
print("\n\n>>> Obrigado por usar o BANKING SYSTEM. Até logo!\n")
