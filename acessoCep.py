import requests


class buscarEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.validador_cep(cep):
            self.cep = cep
        else:
            raise ValueError("-= CEP inválido!! -=")

    def validador_cep(self, cep):
        if (len(cep) == 8):
            return True
        else:
            return False

    def __str__(self):
        bairro, cidade, uf = self.acessaViaCep()
        cep = f"{self.cep[:4]}-{self.cep[4:]}"
        end = f"CEP: {cep}, Bairro: {bairro}, Cidade: {cidade}, UF: {uf}"
        return end

    def acessaViaCep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return {
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        }