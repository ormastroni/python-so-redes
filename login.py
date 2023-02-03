import os

## Idéia de como implementar a autenticação por variável de ambiente
## com as variáveis INFNET_USER e INFNET_PASSWD

print(os.environ['INFNET_USER'])
print(os.environ['INFNET_PASSWD'])

usuario = input('Entre com o login:')
senha = input('Senha:')
home_dir = r'C:\Users\andre\temp'

def autenticate(usr, passw):
    usr_autorized = os.getenv('INFNET_USER')
    if (usr != usr_autorized):
        return False
    pass_autorized = os.getenv('INFNET_PASSWD')
    if (passw != pass_autorized):
        return False
    return True

if (autenticate(usuario, senha)):
    ## Se autorizado, o usuário entra no sistema no diretório HOME
    print(os.getcwd())
    os.chdir(home_dir)
    print(os.getcwd())
    print(os.listdir())
else:
    print('Nao autorizado')