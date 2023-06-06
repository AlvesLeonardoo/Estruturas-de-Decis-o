idade = input()
ageA, ageB = idade.split()
ageA, ageB = int(ageA), int(ageB)
def older (ageA, ageB):
    if ageA > ageB:
        print ('A')
    elif ageA< ageB:
        print ("B")
    else:
        print('Maybe twins')
older(ageA, ageB)
