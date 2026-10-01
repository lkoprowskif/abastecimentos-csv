#Passo 2 - Etapa 1
import csv
import json

total_gasto = 0
total_litros = 0
quantidade_abastecimentos = 0

with open("abastecimentos.csv", "r") as arquivo:
    reader = csv.DictReader(arquivo, delimiter=";")

    for linha in reader:
        litros = float(linha["litros"])
        valor_litro = float(linha["valor_litro"])

        total_gasto += litros * valor_litro
        total_litros += litros
        quantidade_abastecimentos += 1

#Passo 2 - Etapa 2

placa = input("Digite a placa: ")
combustivel = input("Digite o combustível: ")
litros = float(input("Digite a quantidade de litros: "))
valor_litro = float(input("Digite o valor por litro: "))

with open("abastecimentos.csv", "a") as arquivo:
    writer = csv.writer(arquivo, delimiter=";")
    writer.writerow([placa, combustivel, litros, valor_litro])

#Passo 3 - Etapa 1

status_frota = {
    "empresa": "LogiTech Mobility",
    "total_veiculos": 6,
    "sistema_ativo": True,
    "combustiveis_permitidos": ["Gasolina", "Etanol", "Diesel"]
}

with open("config_frota.json", "w") as arquivo:
    json.dump(status_frota, arquivo, indent=4)



