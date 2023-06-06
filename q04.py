n = int(input())
def banner(n):
    if (n >=0):
        if (n%2)==0:
            print('| | | | | | | | | |')
        else:
            print('- - - - - - - - - -')
    else:
        if(n%2):
            print('= = = = = = = = = = ')
        else:
            print('. . . . . . . . . .')
banner(n)