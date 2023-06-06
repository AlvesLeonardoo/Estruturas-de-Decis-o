medidas = input()
peso, sexo, altura = medidas.split()
peso, altura = float(peso), float(altura)
def ComoVaiSuaSaude(peso, sexo, altura):
    if sexo == 'M':
        PI = (72.7 * altura) - 58
    elif sexo == 'F':
        PI = (62.1 * altura) - 44.7
    else:
        return "Sem apontamento."
    IMC = peso / (altura * altura)
    dif_peso = abs(peso - PI)
    if dif_peso <= 0.05 * PI and 18.5 <= IMC < 25:
        return "Você tem uma saúde ótima!"
    elif dif_peso <= 0.1 * PI and 18.5 <= IMC < 25:
        return "Você tem uma saúde boa."
    elif peso < PI and IMC < 18.5:
        return "Atenção: Fique atento ao baixo peso!"
    elif dif_peso > 0.1 * PI and 25 <= IMC < 30:
        return "Cuidado: Medidas acima do padrão!"
    elif dif_peso > 0.1 * PI and IMC >= 30:
        return "Procure Ajuda: Excesso de medidas!"
    else:
        return "Sem apontamento."
print(ComoVaiSuaSaude(peso,sexo,altura))