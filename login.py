from datetime import datetime
# Questão 7. Crie um programa que simule o registro de login de usuários. a cada execução, o
# programa deve solicitar o nome do usuário e registrar o horário de acesso (pode ser inserido
# manualmente ou capturado automaticamente com datetime). As informações devem ser gravadas
# em um arquivo chamado logins.csv. Ao final, o programa deve exibir todos os acessos registrados
arquivo = open('login.csv', 'a+')
arquivo.seek(0)
nome =  input("Nome: ")


agora =datetime.now()
# Gravar no arquivo no formato correto (sem espaço depois da vírgula!)
arquivo.write(f"{nome},{agora}\n")
arquivo.flush()

# Voltar ao início para ler todos os produtos e calcular o total
arquivo.seek(0)
total = 0

for linha in arquivo:
    dados = linha.strip().split(',')  # ['nome', 'preco', 'quantidade']
    print(dados)
