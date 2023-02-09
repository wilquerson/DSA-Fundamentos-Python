def calcula_agua_diaria(peso, idade, sedentarismo, clima):
    # Recomendação de base é de 30 ml/kg
    base = peso * 30
    # Ajuste para idade
    if idade >= 65:
        base += 500
    # Ajuste para atividade física
    if not sedentarismo:
        base += 1000
    # Ajuste para clima
    if clima == "quente":
        base += 500
    return base / 1000

peso = float(input("Qual é o seu peso (em kg)? "))
idade = int(input("Qual é a sua idade (em anos)? "))
sedentarismo = input("Você é sedentário (s/n)? ") == "n"
clima = input("Como está o clima no momento (frio/morno/quente)? ")

agua_diaria = calcula_agua_diaria(peso, idade, sedentarismo, clima)
print("Você precisa beber, aproximadamente,", agua_diaria, "litros de água por dia.")
