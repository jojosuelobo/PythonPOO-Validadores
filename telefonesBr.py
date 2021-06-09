import re

class telefonesBr:
    def __init__(self, num):
        if self.validar_telefone(num):
            self.numero = num
        else:
            raise ValueError("-= Numero Invalido!! -=")

    def validar_telefone(self, num):
        padrao = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resp = re.findall(padrao, num)
        if resp:
            return True
        else:
            return False

    def formatar_num(self):
        mask = f'+{self.numero[:2]}({self.numero[2:4]}){self.numero[4:8]}-{self.numero[8:]}'
        return mask

    def __str__(self):
        return self.formatar_num()