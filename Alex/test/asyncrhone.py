import threading
import time
import random

def count_to(hulk):
    for hulk in range (25):
        print(hulk)

    
    
for j in range (10):
    time.sleep(0.25)
    randomer = ["A","B","C","D","E","F","G","H","I","J"]
    hulk = 10
    int(input("stop"))
    print(randomer[j])
    threading.Thread(target=count_to,args=(hulk,)).start()
    
