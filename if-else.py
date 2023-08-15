#Exemplos de uso if/else

#Identifica triângulo
print("Insira os valores dos lados, o maior primeiro")
a = int(input("Lado a:"))
b = int(input("Lado b:"))
c = int(input("Lado c:"))
if a < b+c:
    print("É um triângulo.")
else:
    print("Não é triângulo.")

#Qual número é maior
d = int(input("Primeiro número:"))
e = int(input("Segundo número:"))
f = int(input("Terceiro número:"))
print("O maior número é")
if d > e:
    if d > f:
        print(d)
    else:
        print(f)
else:
    if e > f:
        print(e)
    else:
        print(f)

#Verifica se o número é primo
num = int(input("Insira um número:"))
primo = True
for possivel_divisor in range(2, num//2 + 1):
    if num % possivel_divisor == 0:
        primo = False
if primo:
    print("É primo.")
else:
    print("Não é primo")

#Elif
x = int(input("Primeiro número:"))
y = int(input("Segundo número:"))
op = input("Operador (+, -, *, /):")
if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)
else:
    print("Operador desconhecido.")