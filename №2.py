print("Введите первый катет")
A=float(input())
print("Введите второй катет")
B=float(input())
C=(A**2+B**2)**(1/2)
S=(A*B)/2
P=A+B+C
S=str(S)
P=str(P)
print("Площадь треугольника="+S)
print("Периметр треугольника="+P)