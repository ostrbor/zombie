from os import fork, wait, _exit
from time import sleep

C_LIFE = 5 #life of child in sec
Z_LIFE = 30 #zombie
P_LIFE = 60 #parent

def child():
 sleep(C_LIFE)
 _exit(0) #or exit(0), in our case it doesn't matter

def parent():
 pid = fork()
 if not pid: child() #pid is 0 for child
 else:
  sleep(C_LIFE+Z_LIFE) #wait until child process in parallel is sleeping, plus zombie lifetime 
  wait() #reap zombie
  sleep(P_LIFE-C_LIFE-Z_LIFE) #comment it if you don't want parent to outlive 

if __name__ == '__main__':
 parent()
