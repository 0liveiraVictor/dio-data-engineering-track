from datetime import datetime


'''
    initial system print
'''
def initial_system_print():
    print("================ BANKING SYSTEM ================", end="")


'''
    final system print
'''
def final_system_print():
    print("================================================")
    print("\n\n>>> Obrigado por usar o BANKING SYSTEM. Até logo!\n")


'''
    get datetime (date: "DD/MM/AAAA" / time: "HH:mm:ss")
'''
def get_datetime():
    transaction_datetime = datetime.now()
    transaction_datetime_str = transaction_datetime.strftime("%d/%m/%Y — %H:%M:%S")
    return transaction_datetime_str


'''
    get specific user
'''
def get_user(ssn, bank_users):
    filtered_user = [user for user in bank_users if user["ssn"] == ssn] # list can be empty or with one element (len iqual 0 or 1, respectively)
    if len(filtered_user) == 1: # user exist
        user_dict = filtered_user[0]
        return user_dict
    else: # user not exist
        return None


'''
    create account
'''
def create_account(BANK_AGENCY, bank_account_index, bank_users, bank_accounts):
    while True:
        ssn = input("\nDigite o CPF do usuário cadastrado no BANKING SYSTEM (somente números): ")
        if ssn.isdigit():
            break
        else:
            print("\n✖ - Operação não permitida. Por favor, insira apenas números.")
    user = get_user(ssn, bank_users)
    if user is None:
        print("\n✖ Usuário não possui cadastro no BANKING SYSTEM. Faça seu cadastro!", end="")
        return  bank_account_index, bank_accounts
    else:
        account_dict = { "agency": BANK_AGENCY, "account_number": f"{bank_account_index}", "username": user["name"] }
        bank_accounts.append(account_dict)
        print("\n✔ - Conta criada com sucesso. Seja bem-vindo(a) ao BANKING SYSTEM!", end="")
        bank_account_index += 1
        return  bank_account_index, bank_accounts 


'''
    create user
'''
def create_user(bank_users):
    while True:
        ssn = input("\nDigite o CPF do usuário (somente números): ")
        if ssn.isdigit():
            break
        else:
            print("\n✖ - Operação não permitida. Por favor, insira apenas números.")
    user = get_user(ssn, bank_users)
    if user:
        print("\n✖ Usuário já cadastrado no BANKING SYSTEM.", end="")
        return bank_users
    else:
        name = input("Digite o nome completo do usuário: ")
        date_of_birth = input("Digite a data de nascimento (dd/mm/aaaa): ")
        street = input("Digite o logradouro (rua, avenida, praça e etc.): ")
        number = input("Digite o número do imóvel: ")
        district = input("Digite o bairro: ")
        city = input("Digite a cidade: ")
        state = input("Digite a sigla do estado (RJ, SP e etc.): ")
        address = f"{street}, {number} - {district} - {city}/{state}"
        user_dict = { "name": name, "date_of_birth": date_of_birth, "ssn": ssn, "address": address }
        bank_users.append(user_dict)
        print("\n✔ - Usuário cadastrado no BANKING SYSTEM com sucesso.", end="")
        return bank_users


'''
    get transactions extract
'''
def get_bank_statement(extract):
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
            print(f"Saldo Pós-Transação: {element['bank_balance']}")
            print(f"Data/Horário de Transação: {element['transaction_datetime']}\n")
            print("-----------------------------------------------")
    print("_______________________________________________")
    

'''
    make withdrawal
'''
def execute_withdrawal(total_transactions, TRANSACTIONS_LIMIT, withdrawal_number, WITHDRAWAL_LIMIT, BANK_WITHDRAWAL_LIMIT, bank_balance, extract):
    if total_transactions < TRANSACTIONS_LIMIT:
        if withdrawal_number >= WITHDRAWAL_LIMIT:          
            print("\n✖ - Operação não permitida. O limite de saques diários foi excedido.", end="")
            return total_transactions, withdrawal_number, bank_balance, extract
        else:
            while True:
                amount_withdrawn = float(input("\nInforme o valor a ser sacado: R$ "))
                if amount_withdrawn > 0:
                    if amount_withdrawn > BANK_WITHDRAWAL_LIMIT:
                        print(f"\n✖ - Operação não permitida. Valor de saque excedeu o limite máximo (máx. R$ {BANK_WITHDRAWAL_LIMIT:.2f}). Tente novamente.")
                    else:
                        if amount_withdrawn > bank_balance:
                            if bank_balance > 0:
                                print(f"\n✖ - Operação não permitida. Você não possui saldo suficiente (saldo atual: R$ {bank_balance:.2f}). Tente outro valor para saque.")
                            else:
                                print(f"\n✖ - Operação não permitida. Você não possui saldo suficiente (saldo atual: R$ {bank_balance:.2f}).", end="")
                                return total_transactions, withdrawal_number, bank_balance, extract
                        else:
                            transaction_datetime = get_datetime()
                            bank_balance -= amount_withdrawn
                            withdrawal_number += 1
                            total_transactions += 1
                            extract_dict = { "op": "2", "value": f"{amount_withdrawn:.2f}", "bank_balance": f"{bank_balance:.2f}", "transaction_datetime": transaction_datetime }
                            extract.append(extract_dict)
                            print(f"\n✔ - Saque de R$ {amount_withdrawn:.2f} realizado com sucesso.", end="")
                            return total_transactions, withdrawal_number, bank_balance, extract
                else:
                    print("\n✖ - Operação inválida. Verifique novamente o valor informado e tente novamente.")
    else:
        print("\n✖ - Operação não permitida. O número de transações permitidas diariamente foi excedido.", end="")
        return total_transactions, withdrawal_number, bank_balance, extract


'''
    make deposit
'''
def execute_deposit(total_transactions, TRANSACTIONS_LIMIT, bank_balance, extract):
    if total_transactions < TRANSACTIONS_LIMIT:
        while True:
            deposit_amount = float(input("\nInforme o valor a ser depositado: R$ "))
            if deposit_amount > 0:
                transaction_datetime = get_datetime()
                bank_balance += deposit_amount
                total_transactions += 1
                extract_dict = { "op": "1", "value": f"{deposit_amount:.2f}", "bank_balance": f"{bank_balance:.2f}", "transaction_datetime": transaction_datetime }
                extract.append(extract_dict)
                print(f"\n✔ - Depósito de R$ {deposit_amount:.2f} realizado com sucesso.", end="")
                return total_transactions, bank_balance, extract
            else:
                print("\n✖ - Operação inválida. Verifique novamente o valor informado e tente novamente.")
    else:
        print("\n✖ - Operação não permitida. O número de transações permitidas diariamente foi excedido.", end="")
        return total_transactions, bank_balance, extract


'''
    get menu options
'''
def get_menu_options():
    menu_options = """

Selecione uma opção válida para a operação bancária:

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Criar Usuário
    [5] - Criar Conta
    [0] - Sair

    >  """
    return menu_options


'''
    get global variables function
'''
def get_global_variables():
    BANK_AGENCY = "0001"
    bank_account_index = 1
    WITHDRAWAL_LIMIT = 3
    withdrawal_number = 0
    total_transactions = 0
    TRANSACTIONS_LIMIT = 10
    bank_balance = 0
    BANK_WITHDRAWAL_LIMIT = 500 # withdrawal limit value in R$
    extract = [] # bank statement list
    bank_users = []
    bank_accounts = []
    return BANK_AGENCY, bank_account_index, WITHDRAWAL_LIMIT, withdrawal_number, total_transactions, TRANSACTIONS_LIMIT, bank_balance, BANK_WITHDRAWAL_LIMIT, extract, bank_users, bank_accounts


'''
    main function
'''
def main():
    BANK_AGENCY, bank_account_index, WITHDRAWAL_LIMIT, withdrawal_number, total_transactions, TRANSACTIONS_LIMIT, bank_balance, BANK_WITHDRAWAL_LIMIT, extract, bank_users, bank_accounts = get_global_variables()
    menu_options = get_menu_options()
    initial_system_print()
    while True:
        option = input(menu_options)
        if option == "0":
            print("")
            break
        elif option == "1":
            total_transactions, bank_balance, extract = execute_deposit(total_transactions, TRANSACTIONS_LIMIT, bank_balance, extract)
        elif option == "2":
            total_transactions, withdrawal_number, bank_balance, extract = execute_withdrawal(total_transactions, TRANSACTIONS_LIMIT, withdrawal_number, WITHDRAWAL_LIMIT, BANK_WITHDRAWAL_LIMIT, bank_balance, extract)
        elif option == "3":
            get_bank_statement(extract)
        elif option == "4":
            bank_users = create_user(bank_users)
        elif option == "5":
            bank_account_index, bank_accounts = create_account(BANK_AGENCY, bank_account_index, bank_users, bank_accounts)
    final_system_print()


if __name__ == "__main__":
    main()
