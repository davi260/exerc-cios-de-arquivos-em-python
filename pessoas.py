# Abrir o arquivo em modo leitura
arquivo = open('pessoas (1).csv', 'r+', encoding='utf-8')

linhas = arquivo.readlines()

# Fechar o arquivo depois da leitura
arquivo.close()

# Pegar o cabeçalho (1ª linha) e as demais linhas de dados
cabecalho = linhas[0].strip().split(',')
dados = linhas[1:]

# Questão 2. Elabore um programa que leia o arquivo chamado pessoas.csv, contendo dados de
# várias pessoas, incluindo a cidade onde moram. O programa deve solicitar ao usuário que digite o
# nome de uma cidade e, em seguida, listar na tela todas as pessoas que residem nesta cidade.
#-----PESSOAS QUE MORAM EM UMA CIDADE----
def questao_2():
    # Solicitar ao usuário uma cidade
    cidade_busca = input("Digite o nome da cidade: ").strip().lower()

    # Procurar e exibir as pessoas da cidade informada
    print(f"\nPessoas que moram em {cidade_busca}:\n")

    encontrou = False
    for linha in dados:
        pessoa = linha.strip().split(',')
        cidade = pessoa[3].strip().lower()
        if cidade == cidade_busca:
            encontrou = True
            print(f"Nome: {pessoa[0]}, Sexo: {pessoa[1]}, Idade: {pessoa[2]}, Estado: {pessoa[4]}, Time: {pessoa[5]}, Renda: {pessoa[6]}, Esporte: {pessoa[7]}")

    if not encontrou:
        print("Nenhuma pessoa encontrada nessa cidade.")


# Questão 3. Desenvolva um programa que leia um arquivo pessoas.csv contendo nomes e os
# clubes para os quais cada pessoa torce. O programa deverá contar quantas pessoas torcem para
# cada clube e exibir os resultados em ordem decrescente, do clube com mais torcedores para o que
# tem menos.
#-----QUANTIDADE DE TORCEDORES----
def questao_3():
    times=[]
    for linha in dados:
        pessoa = linha.strip().split(',')
        time = pessoa[5].strip().lower()
        times.append(time)

    sem_repeticoes = list(set(times))
    for i in sem_repeticoes:
        print(f"{i}: {times.count(i)}")

# Questão 4. Desenvolva um programa que leia um arquivo pessoas.csv contendo nomes e idades
# de várias pessoas. O programa deverá identificar e exibir na tela as três pessoas mais velhas e as
# três pessoas mais novas presentes no arquivo.
def questao_4():
    # Lista para armazenar tuplas com (nome, idade)
    pessoas = []

    for linha in dados:
        pessoa = linha.strip().split(',')
        nome = pessoa[0].strip()
        try:
            idade = int(pessoa[2].strip())
            pessoas.append((nome, idade))
        except ValueError:
            continue
    pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

    # Três mais novas
    print("Três pessoas mais novas:")
    for nome, idade in pessoas_ordenadas[:3]:
        print(f"{nome} - {idade} anos")

    # Três mais velhas
    print("\nTrês pessoas mais velhas:")
    for nome, idade in pessoas_ordenadas[-3:]:
        print(f"{nome} - {idade} anos")

# Questão 5. Desenvolva um programa que leia um arquivo pessoas.csv contendo nomes e os
# esportes favoritos de cada pessoa. O programa deve solicitar ao usuário que digite o nome de um
# esporte e, em seguida, seu programa deve listar na tela todas as pessoas que praticam esse esporte,
# bem como o percentual total de pessoas que praticam esse esporte

def questao_5():
    # Buscar esporte
    esporte_busca = input("Digite o nome da cidade: ").strip().lower()

    encontrou = False
    pessoas=[]
    contador=0
    for linha in dados:
        contador+=1
        pessoa = linha.strip().split(',')
        esporte = pessoa[7].strip().lower()
        if esporte == esporte_busca:
            pessoas.append(pessoa[0])
            encontrou = True
            print(f"Nome: {pessoa[0]}  Esporte: {pessoa[7]}")
    if encontrou:
        calculo = (len(pessoas) * 100) / contador
        print(f"\n{esporte_busca} é o esporte favorito de {calculo:.2f}% das pessoas")
    if not encontrou:
        print(f"Nenhuma pessoa gosta de {esporte_busca}.")

