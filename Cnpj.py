from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.validador_cnpj(documento):
            self.cpnj = documento
        else:
            raise ValueError('=- CNPJ invalido!! -=')

    def validador_cnpj(self, documento):
        if len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError('=- Quantidade de digitos invalido!! -=')

    def formatar_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cpnj)

    def __str__(self):
        return self.formatar_cnpj()