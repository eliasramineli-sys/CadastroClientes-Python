# ==================================================
# PROJETO: VALIDAÇÃO DE CADASTRO DE CLIENTES
# ==================================================
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass

# MODELO DE DADOS
@dataclass(frozen=True)
class Cliente:
    nome: str
    idade: int
    salario: Decimal

# VALIDAÇÕES
def validar_nome(entrada: str) -> str:
    nome = entrada.strip()

    if len(nome) < 3:
        raise ValueError(
            "O nome deve ter pelo menos 3 caracteres."
        )

    return nome

def validar_idade(entrada: str) -> int:
    try:
        idade = int(entrada.strip())
    except ValueError:
        raise ValueError(
            "A idade deve ser um número inteiro válido."
        ) from None

    if not 18 <= idade <= 120:
        raise ValueError(
            "A idade deve estar entre 18 e 120 anos."
        )

    return idade

def validar_salario(entrada: str) -> Decimal:
    try:
        salario = Decimal(entrada.strip())
    except InvalidOperation:
        raise ValueError(
            "O salário deve ser um número válido."
        ) from None

    if not salario.is_finite() or salario <= 0:
        raise ValueError(
            "O salário deve ser um número finito e maior que zero."
        )

    return salario

# REGRA DE NEGÓCIO
def criar_cliente(
    nome: str,
    idade: str,
    salario: str
) -> Cliente:

    return Cliente(
        nome=validar_nome(nome),
        idade=validar_idade(idade),
        salario=validar_salario(salario)
    )

# INTERFACE DE TERMINAL
def executar_cadastro() -> None:
    print("===== CADASTRO DE CLIENTES =====")

    try:
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        salario = input("Digite seu salário mensal: ")

        cliente = criar_cliente(
            nome=nome,
            idade=idade,
            salario=salario
        )

    except ValueError as erro:
        print(f"\nCadastro rejeitado: {erro}")

    except (EOFError, KeyboardInterrupt):
        print("\nCadastro interrompido pelo usuário.")

    else:
        print("\n===== CADASTRO APROVADO =====")
        print(f"Nome: {cliente.nome}")
        print(f"Idade: {cliente.idade} anos")
        print(f"Salário mensal: R$ {cliente.salario:.2f}")
        print("Cadastro realizado com sucesso!")

    finally:
        print("\nProcessamento do cadastro finalizado.")

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    executar_cadastro()
