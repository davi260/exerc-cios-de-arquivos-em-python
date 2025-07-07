# Questão 9. Elabore um programa que leia um arquivo CSV com os campos nome, idade e
# profissão, e crie a partir desses dados um novo arquivo .txt, onde cada linha contenha uma frase no
# seguinte formato: "João, 34 anos, trabalha como Engenheiro." Todos os registros do CSV devem ser
# convertidos para esse novo formato
# Abrir o arquivo CSV em modo leitura
with open('profissao.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

# Pegar os dados (ignorando o cabeçalho)
dados = linhas[1:]

# Abrir o novo arquivo em modo escrita (sobrescreve o conteúdo antigo)
with open('profissao_reescrito.txt', 'w', encoding='utf-8') as arquivo_reescrito:
    for linha in dados:
        nome, idade, profissao = linha.strip().split(',')
        frase = f"{nome}, {idade} anos, trabalha como {profissao}."
        arquivo_reescrito.write(frase + '\n')
