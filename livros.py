# Questão 6. Desenvolva um programa que permita ao usuário cadastrar livros, informando o
# título, o nome do autor e o ano de publicação. Os dados devem ser armazenados no arquivo
# livros.csv. Após o cadastro, o programa deve ler esse arquivo e exibir todos os livros publicados após
# o ano 2000.

arquivo = open('livros.csv', 'a+')
arquivo.seek(0)
titulo =  input("Digite O titulo: ")
nome, ano = input("Agora digite o nome e ano de publicação: ").split()


# Gravar no arquivo no formato correto (sem espaço depois da vírgula!)
arquivo.write(f"{titulo},{nome},{ano}\n")
arquivo.flush()

# Voltar ao início para ler todos os produtos e calcular o total
arquivo.seek(0)

for linha in arquivo:
    dados = linha.strip().split(',')  # ['nome', 'preco', 'quantidade']
    ano =  int(dados[2])
    if ano>2000:
        print(dados)