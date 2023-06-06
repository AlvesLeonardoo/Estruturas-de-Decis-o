desenho = input()
arg1, arg2, forma = desenho.split()
arg1, arg2 = int(arg1), int(arg2)
def area(arg1,arg2,forma):
    if forma == 'losango':
        area_losango = arg1 * arg2 // 2
        print(f'O {forma} tem {area_losango} de area')
    elif forma == 'retangulo':
        area_retangulo = arg1*arg2
        print(f'O {forma} tem {area_retangulo} de area')
    elif forma == 'triangulo':
        area_triangulo = arg1*arg2 // 2
        print(f'O {forma} tem {area_triangulo} de area')
    else:
        print('Digite valore válidos')
(area(arg1,arg2,forma))