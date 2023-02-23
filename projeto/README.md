# Projeto do shell para o sistema de arquivos

Vamos atualizar o projeto desenvolvido na disciplina anterior para transformar o emulador numa interface que manipule de fato o sistema de arquivos da sua máquina. Lembrando que os comandos desenvolvidos foram para o shell fora os seguintes:
* **new [caminho/nome-do-arquivo]**: cria um novo arquivo no diretório especificado no caminho (caminho é opcional)
* **del [caminho/nome-do-arquivo]**: remove o arquivo do diretório especificado no caminho (caminho é opcional)
* **ls [caminho]**: lista todos os arquivos e diretórios localizados no caminho (caminho é opcional)
* **mkdir [caminho/nome-do-dir]**: cria um diretório novo no diretório especificado no caminho (caminho é opcional)
* **rmdir [caminho/nome-do-dir]**: remove um diretório existente no diretório especificado no caminho (caminho é opcional)
* **cp [caminho/nome-do-arquivo] [destino]**: copia o arquivo para um diretório especificado no destino
* **mv [caminho/nome-do-arquivo] [destino]**: move o arquivo para um diretório especificado no destino
* **exit**: sai do shell

  ## Planejamento das entregas
 1. Ao iniciar o shell, devem ser solicitadas as credenciais do usuário autorizado para rodar o shell. Faça com que o login e a senha do usuário autorizado estejam armazenadas nas seguintes variáveis de ambiente: **INFNET_USER** e **INFNET_PASSWD**. Ao entrar com o usuário e a senha, seu módulo de autenticação deve conferir se estas credenciais digitadas são as mesmas que estão nas variáveis de ambiente.
 2. Crie um diretório na sua máquina para servir de **HOME_DIR** do seu shell. Ou seja, depois que você se autenticar e entrar no shell, o diretório atual deve estar posicionado no **HOME_DIR**. Configure o caminho do seu **HOME_DIR** na variável de ambiente **INFNET_HOMEDIR**
 3. Transforme os comandos **ls, mkdir e rmdir** para interagirem com o sistema de arquivos da sua máquina. Ou seja, o **ls** retorna os arquivos que estão no diretório especificado do comando (ou o atual, caso seja omitido do comando) e o **mkdir/rmdir** cria/remove um subdiretório. Você não precisa mais manter suas estruturas de dicionário do emulador.
 4. Transforme os comandos cp e mv para interagirem com o sistema de arquivos da sua máquina
 5. Transforme os comandos new e del para interagirem com o sistema de arquivos da sua máquina
 6. Implemente o módulo de backup: Crie uma variável de ambiente chamada **BACKUP_HOME** para gaurdar o caminho da sua máquina onde deve ser mantido um backup. Crie um novo comando para o shell com a seguinte sintaxe: **backup [nome-backup]**. Este comando deve criar uma pasta com o nome do backup no **BACKUP_HOME** e copiar todo o conteúdo do diretório atual (onde o comando foi executado) para o diretório do backup.
 7. Trate todas as exceções e possíveis erros dos comandos. Os eventuais erros devem ser guardados num arquivo de log com o rótulo ERROR. Todos os comandos executados na sessão do shell devem ser logados no modo DEBUG
 8. Outras funcionalidades ainda serão propostas

