import threading
import time


def count_to(hulk):
    for hulk in range (25):
        print(hulk)

    
    
for j in range (10):
    time.sleep(0.25)
    randomer = ["A","B","C","D","E","F","G","H","I","J"]
    hulk = 10
    print(randomer[j])
    threading.Thread(target=count_to,args=(hulk,)).start()
    
