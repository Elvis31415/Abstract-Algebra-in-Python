N = int(input("Enter a integer greater than 1: "))
lista = list(range(N))
lista.remove(0)
lista.remove(1)

# iterate throught the list
for number in lista:
    indice = lista.index(number) + 1
    # iterate throught all the elements of the list from the current element index forward
    for num in lista[indice:]:
        # eliminate all other elements whose remainder is zero when divide by the current number
        if num%number == 0:
            lista.remove(num)

print(lista)