
print("\n\n********** QUESTION: CALCULATE AVERAGE TURN AROUND TIME WITH FIRST COME FIRST SERVE (FCFS) **********\n\n")

print("\n\n********** QUESTION: CALCULATE AVERAGE TURN AROUND TIME WITH SHORTEST JOB FIRST (SJF) **********\n\n")

import threading
import time
from queue import Queue
print_lock=threading.Lock()

def threads(both):
    time.sleep(0.002)
    with print_lock:
        print(threading.current_thread().name,both)

def threader():
    fcfs=q.get()
    sjf=q.get()
    threads(fcfs)
    q.task_done()
    threads(sjf)
    q.task_done()
    
q=Queue()
t=threading.Thread(target=threader)
t.killer=True
t.start()
start=time.time()

ata=[]
bta=[]
cta=[]
cta1=[]
tata=[]
tata1=[]

def Cloning(li1):
    li_copy = li1[:]
    return li_copy
n=int(input("enter no of processes\t"))
print("\n\n**********ENTER ARRIVAL AND BURST TIME**********\n\n")
for i in range(n):
    at=int(input("enter arival time  \t"))
    ata.append(at)
    ata1=Cloning(ata)
    ata2=Cloning(ata)
    for j in range(i,i+1):
        bt=int(input("enter burst time \t"))
        bta.append(bt)
        bta1=Cloning(bta)
        bta2=Cloning(bta)


def fcfs():
    print("\n\n**********COMPLETION TIME FOR FCFS**********\n\n")
    for u in range(n):
        cta.append(0)
    q=min(ata1)
    mi = ata1.index(min(ata1))
    s=q+bta1[mi]
    cta[mi]=s
    ata1[mi]=  float('inf')
    bta1[mi]=  float('inf')
    l=len(ata1)
    while l-1:
        q1=min(ata1)
        mi1= ata1.index(min(ata1))
        s=s+bta1[mi1]
        cta[mi1]=s
        ata1[mi1]= float('inf')
        bta1[mi1]= float('inf')
        l-=1
    for t in range(n):
        print("completion time is\t",cta[t] )
    
    print("\n\n**********TURN AROUND TIME FOR FCFS**********\n\n")      
    for l in range(n):
        tat=cta[l]-ata[l]
        print("turn around time \t",tat)
        tata.append(tat)
    print("\n\n**********AVERAGE TURN AROUND TIME FOR FCFS**********\n\n")
    atat=0
    for m in range(n):
        atat=atat+tata[m]
    print("\naverage turn around time with FCFS\t",atat/n)

def sjf():
    print("\n\n**********COMPLETION TIME FOR SJF**********\n\n")
    for u in range(n):
        cta1.append(0)
    q2=min(ata2)
    mi2 = ata2.index(min(ata2))
    s1=q2+bta2[mi2]
    cta1[mi2]=s1
    ata2[mi2]=  float('inf')
    bta2[mi2]=  float('inf')
    l=len(ata2)
    while l-2:
        q3=min(bta2)
        mi3= bta2.index(min(bta2))
        if set([q3 for q3 in bta2 if bta2.count(q3) > 1]):
            for ii in range(len(bta2)):    
                if bta2[ii]==q3:
                    if (ata2[ii]<ata2[mi3]):
                        s1=s1+bta2[ii]
                        cta1[ii]=s1
                        ata2[ii]= float('inf')
                        bta2[ii]= float('inf')
                    else:
                        continue
                        
        
        s1=s1+bta2[mi3]
        cta1[mi3]=s1
        ata2[mi3]= float('inf')
        bta2[mi3]= float('inf')
        l-=1
    for w in range(n):
        print("completion time is\t",cta1[w] )

    
    print("\n\n**********TURN AROUND TIME FOR SJF**********\n\n")

    for o in range(n):
        tat1=cta1[o]-ata[o]
        print("turn around time \t",tat1)
        tata1.append(tat1)

    print("\n\n**********AVERAGE TURN AROUND TIME FOR SJF**********\n\n")

    atat1=0
    for p in range(n):
        atat1=atat1+tata1[p]
    print("\naverage turn around time with SJF\t",atat1/n)     
    

q.put(fcfs())
q.put(sjf())
q.join()




        



