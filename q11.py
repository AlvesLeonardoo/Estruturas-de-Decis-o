poder = input()
powerA, powerB = poder.split()
powerA, powerB = int(powerA), int(powerB)
def riscu(powerA, powerB):
    if powerA > powerB:
        print('Jogador A vence')
    elif powerA < powerB:
        print('Jogador B vence')
    else:
        print('Dois jogadores igualmente fracos')
riscu(powerA,powerB)