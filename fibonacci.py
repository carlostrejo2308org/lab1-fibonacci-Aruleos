def fibonacciCiclo(n):
    print("Ciclo: ")
    count = 0
    n1 = 0
    n2 = 1

    if n == 0:
        print("Numero: ", n)
        print(n)   
        exit

    if n == 1:
        print("Numero: ", n)
        print(n-1)
        print(n)
        exit

    while count < n+1 and n > 1:
        print (n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

def fibonacciRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacciRec(n-1) + fibonacciRec(n-2)

n = int(input("Numero?: " ))
fibonacciCiclo (n)
serie = fibonacciRec(n)
print("Recursivo:")
print(serie)
