"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

"""

A = int(input("Informe um valor para A: "))
B = int(input("Informe um valor para B: "))
C = int(input("Informe um valor para C: "))
D = int(input("Informe um valor para D: "))

diferença = (A * B) - (C * D)
print (f"A diferença do produto de A e B pelo produto de C e D é: {diferença}")