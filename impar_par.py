maior_impar = 0
menor_impar = 0
maior_par = 0
menor_par = 0
total_impar = 0
total_par = 0

for impar in range(1, 50, 2):
    notas_impar = float(input(f"Você está digitando a nota dos alunos IMPARES \n Por favor, insira a nota do aluno {impar}:" ))
    total_impar = total_impar + notas_impar
    if notas_impar > maior_impar and (notas_impar <= 10):
        maior_impar = notas_impar
        menor_impar = maior_impar
    if notas_impar < menor_impar:
        menor_impar = notas_impar


input("\n Alunos IMPARES adicionados, agora iremos adicionar os aluno PARES. Clique em Enter para iniciar \n")

for par in range(2, 51, 2):
    notas_par = float(input(f"Você está digitando a nota dos alunos PARES \n Por favor, insira a nota do aluno {par}:"))
    total_par = total_par + notas_par
    if notas_par > maior_par and (notas_par <= 10):
        maior_par = notas_par
        menor_par = maior_par
    if notas_par < menor_par:
        menor_par = notas_par
input('\n Alunos PARES adcionados, clique Enter para ver o resultado')

medias_impar = total_impar / 25
medias_par = total_par / 25

print(f'A maior nota impar foi: {maior_impar}')
print(f'A menor nota impar foi: {menor_impar}')
print(f'A media de notas impares foi: {medias_impar}')
print(f'A maior nota par foi: {maior_par}')
print(f'A menor nota par foi: {menor_par}')
print(f'A media de notas pares foi: {medias_par}')
