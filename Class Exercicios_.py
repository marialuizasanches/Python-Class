class Cliente:
    def __init__(self, nome, ano_nascimento, sexo, saldo, endereco, ativo=True):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.sexo = sexo
        self.saldo = saldo
        self.endereco = endereco
        self.ativo = ativo

    def imprimir_valores(self):
        print("Nome:", self.nome)
        print("Ano de Nascimento:", self.ano_nascimento)
        print("Sexo:", self.sexo)
        print("Saldo:", self.saldo)
        print("Endereço:", self.endereco)
        print("Ativo:", "Sim" if self.ativo else "Não")
        print()

    def cliente_ativo(self):
        return self.ativo

    def imprimir_idade(self):
        idade = 2024 - self.ano_nascimento
        print("Idade:", idade)
        print()

    def saldo_positivo_negativo(self):
        if self.saldo >= 0:
            print("Saldo: Positivo")
        else:
            print("Saldo: Negativo")
        print()


cliente1 = Cliente("Gabriela", 1990, "Feminino", 1000, "Rua A, 123")
cliente2 = Cliente("Maria Luiza", 1985, "Feminino", -500, "Rua B, 456")
cliente3 = Cliente("Lucas", 2000, "Masculino", 200, "Rua C, 789", ativo=False)

print("Cliente 1:")
cliente1.imprimir_valores()
cliente1.imprimir_idade()
cliente1.saldo_positivo_negativo()

print("Cliente 2:")
cliente2.imprimir_valores()
cliente2.imprimir_idade()
cliente2.saldo_positivo_negativo()

print("Cliente 3:")
cliente3.imprimir_valores()
cliente3.imprimir_idade()
cliente3.saldo_positivo_negativo()


'''
CLASS EXERCICIOS:
'''


class Exercicios:
    def __init__(self, nomeAluno, numeroChamada):
        self.nomeAluno = nomeAluno
        self.numeroChamada = numeroChamada
        
    def exercicio1(self):
        nome = "Gabriel"
        idade = 25
        sexo = "Masculino"
        status = "Estudante"
        print("Exercício 1:")
        print("Nome:", nome)
        print("Idade:", idade)
        print("Sexo:", sexo)
        print("Status:", status)
        print()

    def exercicio2(self):
        nome = "Maria Luiza"
        idade = 30
        sexo = "Feminino"
        status = "Professora"
        print("Exercício 2:")
        print("Nome:", nome, "Idade:", idade, "Sexo:", sexo, "Status:", status)
        print()

    def exercicio3(self):
        nome = "Lucas"
        sobrenome = "Silva"
        nomeCompleto = nome + " " + sobrenome
        print("Exercício 3:")
        print("Nome Completo:", nomeCompleto)
        print()

    def exercicio4(self):
        nome1 = "Carlos"
        nome2 = "Ana"
        sobrenome1 = "Ferreira"
        sobrenome2 = "Oliveira"
        nomeCompleto1 = nome1 + " " + sobrenome1
        nomeCompleto2 = nome2 + " " + sobrenome2
        print("Exercício 4:")
        print("Nome Completo 1:", nomeCompleto1)
        print("Nome Completo 2:", nomeCompleto2)
        print()

    def exercicio5(self):
        alunos = ["Pedro", "Maria", "João", "Ana"]
        notas = [7.5, 8.0, 6.5, 9.0]
        print("Exercício 5:")
        print("Alunos:", alunos)
        print("Notas:", notas)
        print()

    def exercicio6(self):
        alunos = ["Pedro", "Maria", "João", "Ana"]
        notas = [7.5, 8.0, 6.5, 9.0]
        print("Exercício 6:")
        print("Alunos e suas notas:")
        for aluno, nota in zip(alunos, notas):
            print("Nome:", aluno, "- Nota:", nota)
        print()

    def exercicio7(self):
        num1 = 5
        num2 = 10
        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        divisao = num1 / num2
        print("Exercício 7:")
        print("Soma:", soma)
        print("Subtração:", subtracao)
        print("Multiplicação:", multiplicacao)
        print("Divisão:", divisao)
        print()


exercicio = Exercicios("Fulano", 1)
exercicio.exercicio1()
exercicio.exercicio2()
exercicio.exercicio3()
exercicio.exercicio4()
exercicio.exercicio5()
exercicio.exercicio6()
exercicio.exercicio7()

