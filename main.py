import requests
from cpf import Cpf
from Cnpj import Cnpj
from telefonesBr import telefonesBr
from datas import Datas
from acessoCep import buscarEndereco

cpf1 = Cpf("90221218017")
cnpj1 = Cnpj("40556154000189")
tel1 = telefonesBr("5527995134007")
cadastro1 = Datas()
cep1 = buscarEndereco("72318030")

# pip install requests - TERMINAL
#r = requests.get("https://viacep.com.br/ws/01001000/json/")
