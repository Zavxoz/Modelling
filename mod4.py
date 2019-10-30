from random import uniform, randint, random

lifetimes = []
p=0.5
counts = 2000000
np= 1-p
p1=0.45
np1=1-0.45
p2=0.35
np2=1-p2
tasks = []
class Task:
    def __init__(self, id, cur_state="000"):
        self._id = id
        self.lifetime = -1
        self.cur_state = cur_state
        self.stage = 0
'''        
states ={"000":{"010":"np", "000": "p"},
         "010":{"110": "np*p2", "011":"np*np1", "001":"p*np1","010":"p*p2"},
         "110":{"011":"p*np1","111":"np*np1", "110":"p1"},
         "111":{"110":"p1*np2", "011":"np1", "111":"p1*p2"},
         "011":{"110":"np*p1*np2","111":"np*p1*p2","001":"p*(1-p1)","010":"p*p1*np2","011":"p*p1*p2+np*np1"},
         "001":{"011":"np*p2", "010":"np*np2","000":"p*np2","001":"p*p2"}}


list_of_k=[]
list_of_v=[]
prev_state = "000"
for i in range(counts):
    rnd = uniform(0,1)    
    max_p = "0"
    max_age = 0
    if prev_state=="000" and rnd<np:
        continue
    for k, v in states[prev_state].items():
        if eval(v)>=eval(max_p):
            max_p = v
            max_k = k
            if rnd>eval(v):
                list_of_v.append(max_p)
                list_of_k.append(max_k)
            else:
                list_of_v.append(max_p)
                list_of_k.append(max_k)
    if len(list_of_k)>1:
        list_of_k = [i for i in zip(list_of_k,list_of_v) if eval(i[1])==eval(max_p)]
    if len(list_of_k)>1:
        index = randint(0, len(list_of_k)-1)
        for j in tasks:            
            j.cur_state = list_of_k[index][0]
            j.lifetime += 1
        if "np" in list_of_k[index][1]:
            tasks.append(Task(i, list_of_k[index][0]))
    else:
        for j in tasks:
            index = 0
            j.cur_state = list_of_k[index][0]
            j.lifetime += 1
        if "np" in list_of_k[0][1]:
            tasks.append(Task(i, j.cur_state))
    prev_state = list_of_k[index][0]
    
    if tasks and tasks[0].cur_state.count("1")!=len(tasks):
        for x in tasks:
            if x.lifetime>max_age:
                max_age = x.lifetime
        for x in tasks:
            if x.lifetime == max_age:
                if len(tasks)!=0:
                    tasks.remove(x)
                else:
                    x.cur_state = "000"
        lifetimes.append(max_age)
        
    list_of_k.clear()
    list_of_v.clear()
    
print(float(sum(lifetimes)/len(lifetimes)))
'''
from collections import defaultdict

new_tasks=[]   
stages = defaultdict(int) 
tasks_in_system = []
new_lifetimes = []
numb_of_finished = 0
for i in range(1,4):
    stages[i]    
numb_of_tasks = 0
task_per_count=[]
for i in range(counts):
    rnd = random()
    if rnd > p2:
        if stages[3] == 1:
            stages[3] = 0
            numb_of_finished += 1
            new_lifetimes.append(new_tasks[0].lifetime)
            new_tasks.pop(0)
            tasks_in_system.append(1)
    else:
        tasks_in_system.append(0)
                    
    if rnd > p1:
        if stages[2] == 1:
            if stages[3] == 1:
                new_lifetimes.append(new_tasks[1].lifetime)    
                new_tasks.pop(1)  
                stages[2] = 0          
                continue
            stages[3] = 1
            stages[2] = 0
            if stages[1] == 1:
                stages[1] = 0
                stages[2] = 1    
               
    if rnd > p:
        numb_of_tasks += 1
        if stages[1] == 1:
            new_lifetimes.append(0)
            continue
        if stages[2] == 1:
            new_tasks.append(Task(i))
            stages[1] = 1
        else:
            stages[2] = 1
            new_tasks.append(Task(i))
    
    for i in new_tasks:
        i.lifetime += 1
    task_per_count.append(len(new_tasks))

print("Wc = ", float(sum(new_lifetimes)/len(new_lifetimes)))
print("A = ", float(sum(tasks_in_system)/len(tasks_in_system)))
print("Q = ", numb_of_finished/numb_of_tasks)
