desenho = input()
arg1, arg2, forma = desenho.split()
arg1, arg2 = int(arg1), int(arg2)
def area(arg1, arg2, forma):
    arg1,arg2 = int(arg1), int(arg2)
    if forma == "retangulo":
        area_retangulo = arg1 * arg2
        print(f"O retangulo tem {area_retangulo} de area")
    elif forma == "losango":
        area_losango = (arg1 * arg2) // 2
        print(f"O losango tem {area_losango} de area")
    elif forma == "triangulo":
        area_triangulo = (arg1 * arg2) // 2
        print(f"O triangulo tem {area_triangulo} de area")
    elif forma == "circulo":
        area_circulo = arg2 * arg1 ** 2
        print(f"O circulo tem {area_circulo} de area")
    else:
        print("Forma geométrica inválida")
