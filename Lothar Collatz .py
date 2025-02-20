#toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
c0 = int(input("Introduce un numero entero: "))
pasos = 0
#si es par, evalúa un nuevo c0 como c0 ÷ 2;
while c0 >= 0:
    if c0 % 2 == 0:
        c0 /= 2
        print(c0)
#de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
    else:
        c0 = 3 * c0 + 1
        print(c0)
    pasos += 1 
    if c0 == 1:
        break
print ("pasos = ", pasos)

#si c0 ≠ 1, salta al punto 2.
