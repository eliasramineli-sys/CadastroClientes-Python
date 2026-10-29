import unittest
from decimal import Decimal

from desafio_cadastro import Cliente, criar_cliente, validar_idade, validar_nome, validar_salario


class TestCadastro(unittest.TestCase):
    def test_nome_valido(self):
        self.assertEqual(validar_nome("  Carlos  "), "Carlos")

    def test_nome_curto(self):
        with self.assertRaises(ValueError):
            validar_nome("  Al ")

    def test_idade_limites(self):
        self.assertEqual(validar_idade("18"), 18)
        self.assertEqual(validar_idade("120"), 120)

    def test_idade_invalida(self):
        for entrada in ("abc", "17", "121", "20.5"):
            with self.subTest(entrada=entrada), self.assertRaises(ValueError):
                validar_idade(entrada)

    def test_salario_valido(self):
        self.assertEqual(validar_salario("2500.50"), Decimal("2500.50"))

    def test_salario_invalido(self):
        for entrada in ("abc", "0", "-5", "NaN", "Infinity", "-Infinity"):
            with self.subTest(entrada=entrada), self.assertRaises(ValueError):
                validar_salario(entrada)

    def test_criar_cliente(self):
        cliente = criar_cliente("  Carlos ", "28", "3000.25")
        self.assertEqual(cliente, Cliente("Carlos", 28, Decimal("3000.25")))


if __name__ == "__main__":
    unittest.main()
