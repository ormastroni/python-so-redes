import os
import subprocess, psutil, time

###########################
## Execução de processos e subprocessos
###########################

'''executavel_sem_path = 'notepad.exe'
executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\notepad.exe'

os.spawnl(os.P_NOWAIT, executavel_com_path, " ")
print('processo pai volta a executar')

input('Pressione qq tecla')

os.execl(executavel_com_path, " ")
print('processo pai não volta a executar')'''

###########################
## Captura do objeto processo
###########################

'''p = subprocess.run(["calc"])
print(p)
print('Função run terminou a execução e código Python volta a executar')'''

'''p = subprocess.Popen(["notepad", "arq_texto.txt"])
print("PID do processo criado:", p.pid)
print(p)
input('Pressione qualquer tecla')'''

###########################
## Captura dos processos da máquina
###########################

#processos = psutil.pids()
#print(processos)

'''if psutil.pid_exists(77072):
    p = psutil.Process(77072)
    print(str(p.pid) + '-' + p.name() + '-' + p.status())
    print(p.exe())
    print(p.cwd())
    print(p.username())
else:
  print('O processo nao existe')'''

'''for p in psutil.process_iter():
    print(str(p.pid) + '-' + p.name() + '-' + p.status() + '-' + str(p.create_time()) + '-' + time.ctime(p.create_time()))
    print(p.cpu_times())
    print(p.memory_percent())
    print(p.memory_info())
    print(p.num_threads())    
    print('--------------------------------------------')

    # As seguintes funções não podem ser chamadas de um programa Python no Windows 
    # Exceto que o usuário tenha direitos de administrador

    print(p.exe())
    print(p.cwd())
    print(p.username())
    print(p.cpu_affinity())
    print(p.threads())'''

'''print(psutil.cpu_times())
print(psutil.cpu_times(percpu=True))
print(psutil.cpu_times_percent())'''

psutil.cpu_times_percent()
for i in range(10):
  time.sleep(5)
  print(psutil.cpu_times_percent())

'''print(psutil.cpu_times_percent(percpu=True))
for i in range(10):
    print(psutil.cpu_times_percent(interval=1))'''

'''print(psutil.cpu_percent(interval=1)) # Espera 1 segundo para coletar para o processador
print(psutil.cpu_percent(interval=1, percpu=True)) # Por núcleo'''


###########################
## Captura das informações de memória e disco
###########################
'''print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_partitions())
print(psutil.disk_usage('C:\\users\\andre'))'''