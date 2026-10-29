# Cadastro de Clientes — Python

Aplicação de terminal em Python para validar informações de clientes com regras de negócio, mensagens claras de erro e tratamento de exceções.

## Funcionalidades

- Nome com ao menos três caracteres após remoção de espaços nas extremidades
- Idade inteira entre 18 e 120 anos
- Salário positivo e finito usando `decimal.Decimal`
- Modelo de dados imutável com `@dataclass(frozen=True)`
- Tratamento de entradas inválidas e interrupções de terminal
- Separação entre validação, regra de negócio e interação com o usuário

## Executar

Requisito: Python 3.10 ou superior. Não há dependências de terceiros.

```bash
python desafio_cadastro.py
```

Digite nome, idade e salário quando solicitado. Para valores decimais, utilize ponto como separador (por exemplo, `2500.50`).

## Testes

```bash
python -m unittest discover -s tests -v
```

## Estrutura

```text
CadastroClientes-Python/
├── desafio_cadastro.py
├── tests/
│   └── test_cadastro.py
├── .gitignore
└── README.md
```

## Tecnologias

Python, `dataclasses`, `decimal` e `unittest` (biblioteca padrão).

## Sobre

Projeto de estudo e portfólio voltado à prática de validação de dados, funções, exceções e organização de código em Python.
