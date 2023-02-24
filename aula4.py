import logging

### Diferentes tipos de configuração:
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG, format='%(process)d-%(levelname)s-%(message)s')
#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

## Logando variáveis
name = input('Entre com o nome do usuario: ')
logging.warning(f'{name} logou no sistema')

## Capturando as pilhas de exceções
a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.error("Exceção gerada", exc_info=False)