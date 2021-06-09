from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.validador_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError('=- CPF inválido!! -=')

    def validador_cpf(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("=- Quantidade de caracteres inválida!! -=")

    def formatar_cpf(self):
        part1 = self.cpf[:3]
        part2 = self.cpf[3:6]
        part3 = self.cpf[6:9]
        part4 = self.cpf[9:]
        return f"{part1}.{part2}.{part3}.{part4}"

    def __str__(self):
        return self.formatar_cpf()