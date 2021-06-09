from datetime import datetime, timedelta
class Datas:
    def __init__(self):
        self.hora_cadastro = datetime.today()

    def mes_cadastro(self):
        meses = ["Janeiro", "Fevereiro", "Março",
                 "Abril", "Maio", "Junho", "Julho",
                 "Agosto", "Setembro", "Outubro",
                 "Novembro", "Dezembro"]

        mes_cadastro = self.hora_cadastro.month
        return meses[mes_cadastro - 1]

    def semana_cadastro(self):
        dias_semana = ["Segunda", "Terça", "Quarta",
                 "Quinta", "Sexta", "Sabado", "Domingo"]
        semana = self.hora_cadastro.weekday()
        return dias_semana[semana+1]

    def formatar_data(self):
        dataFormatada = self.hora_cadastro.strftime("%d/%m/%Y %H:%M")
        return dataFormatada

    def __str__(self):
        return self.formatar_data()