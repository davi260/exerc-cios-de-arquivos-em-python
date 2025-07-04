arquivo = open('produtos.csv', 'a+')
arquivo.seek(0)

nome, preco, quantidade = input("Digite nome, preço e quantidade: ").split()
preco = float(preco)
quantidade = int(quantidade)

# Gravar no arquivo no formato correto (sem espaço depois da vírgula!)
arquivo.write(f"{nome},{preco},{quantidade}\n")
arquivo.flush() 

# Voltar ao início para ler todos os produtos e calcular o total
arquivo.seek(0)
total = 0

for linha in arquivo:
    dados = linha.strip().split(',')  # ['nome', 'preco', 'quantidade']
    if len(dados) == 3:
        try:
            preco = float(dados[1])
            quantidade = int(dados[2])
            total += preco * quantidade
        except ValueError:
            pass  # Ignora linhas mal formatadas

arquivo.close()  # Sempre fecha o arquivo depois

# Exibe o resultado
print(f"Valor total em estoque: R$ {total:.2f}")