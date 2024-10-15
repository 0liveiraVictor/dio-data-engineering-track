<h1>
  <a href="https://www.dio.me/">
    <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png">
  </a>
  <span>
    Desafio 2 – Aperfeiçoando o Sistema Bancário [<a href="main.py"><em>Banking System</em> - <em>Version</em> 1.1.0</a>]
  </span>
</h1>   

## Objetivo Geral

- Separar a codificação existente na versão 1.0.0 de saque, depósito e extrato em funções bem definidas; 
- Implementar novas funcionalidades no sistema, criando duas novas funções: cadastrar usuário cliente e cadastrar conta bancária;
- Estabelecer um limite de 10 transações diárias para uma conta bancária (limite total);
- Adicionar serviço de exibição de mensagem informativa de excessão ao número de transações permitidas diariamente (caso o limite seja atingido);
- Exibir no extrato a data e hora de todas as transações;

## Desafio de Projeto da DIO

Precisamos deixar nosso desafio com o código mais modularizado. Para isso vamos criar funções para as operações já existentes na versão 1.0.0: sacar, depositar e visualizar histórico (extrato). Além disso, para a versão 1.1.0 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com um usuário pré-existente). 

###  Função Saque:

A função de saque deve receber os argumentos apenas por nome (*keyword only*). Sugestão de argumentos: saldo, valor, extrato, limite, numero de saques, limite de saques. Sugestão de retorno: saldo e extrato.

###  Função Depósito:

A função de depósito deve receber os argumentos apenas por posição (*positional only*). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

###  Função Extrato:

A função extrato deve receber os argumentos por posição e nome (*positional* e *keyword only*). Argumentos posicionais: saldo; argumentos nomeados: extrato.

###  Função Criar Usuário:

O programa deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma *string* com o formato: logradouro, nº - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.

###  Função Criar Conta:

O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

> Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

## Ferramentas Utilizadas

[![Python](https://img.shields.io/badge/Python-111?style=for-the-badge&logo=python&logoColor=3772A2)](https://docs.python.org/3/)
