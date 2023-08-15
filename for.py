#Uso geral da função for
for i in [1, 2, 3, 4]:
    print(i)

for i in range(5):
    print(i)

#Printa os números, contando de 2 em 2, até 10
for i in range(0, 10, 2):
    print(i)

#Conta ao contrário
for i in range(10, 0, -1):
    print(i)

#Progressão não-aritmética
for i in range(5):
    print(2**i)

#Somatório
total = 0
for item in [20, 52, 67, 49, 15, 22]:
    total += item
print(total)

somatorioMatematico = 0
for i in range(1, 101):
    somatorioMatematico += i
print(somatorioMatematico)

#Fatorial de 5
fatorial = 1
for i in range(2, 5+1):
    fatorial *= i
print(fatorial)

#Aninhamento de for
for i in range(1, 11):
    print("Tabuada de:", i)
    for j in range(1, 11):
        print(i*j)