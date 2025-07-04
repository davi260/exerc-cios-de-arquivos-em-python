# Questão 10. Desenvolva um programa que funcione como um gerador de boletim. O usuário deve
# digitar o nome do aluno e três notas. Os dados devem ser gravados em um arquivo chamado
# boletim.csv. Depois, o programa deve ler esse arquivo e calcular a média de cada aluno, indicando
# sua situação: Aprovado (média ≥ 7), Em exame (entre 5 e 6.9) ou Reprovado (média < 5)
arquivo = open('boletim.csv', 'a+')
arquivo.seek(0)
nome =  input("Digite o nome do Aluno: ")
n1,n2,n3 = input("Agora digite as notas do aluno com espaço entre elas: ").split()
n1 =float(n1)
n2 =float(n2)
n3 =float(n3)

if (n1 <0 or n1>10) or (n2 <0 or n2>10) or (n3 <0 or n3>10):
    print("Notas inválidas!! As notas devem ser entre 0 e 10")
else:
# Gravar no arquivo no formato correto (sem espaço depois da vírgula!)
    arquivo.write(f"{nome},{n1},{n2},{n3}\n")
    arquivo.flush()
    arquivo.seek(0)
    situacao=''
    for linha in arquivo:
        dados = linha.strip().split(',')
        media = (float(dados[1]) + float(dados[2]) + float(dados[3]))/3
        print(f"{dados} {media:.2f}")