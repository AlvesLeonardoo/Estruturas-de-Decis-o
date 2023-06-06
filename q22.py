simbolo = input()
def Alfabeto(simbolo):
    if not simbolo.isalpha():
        return "Não está no alfabeto"
    elif simbolo.lower() in 'aeiou':
        return "Vogal"
    else:
        return "Consoante"
print(Alfabeto(simbolo))