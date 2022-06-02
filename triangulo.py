def get_type_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if((a+b)>c and (a+c)>b and (c+b)>a):
        if(a == b and b == c):
            print("los Lados son de un triangulo Equilatero")
        elif(a == b or a == c or b == c):
            print("los Lados son de un triangulo Isosceles")
        else:
            print("los Lados son de un triangulo escaleno")
    else:
        print("No es posible construir el triangulo con esos lados")

   

def main():
    sides = [100,2,3]
    get_type_triangle(sides)
    
if __name__ == "__main__":
    main()
