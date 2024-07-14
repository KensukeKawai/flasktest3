
import threading
import time
import btserial as bt
import requestapp as rq

CYCLE = 1 # [s]
reqdata = []
req_flag = 0

def dataprepro(data):
    predata = []
    predata.append(data[bt.ROLL])
    predata.append(data[bt.PITCH])
    predata.append(data[bt.YAW])
    return predata

def trg():
    global req_flag
    req_flag = 1
    
    t = threading.Timer(CYCLE,trg)
    t.start()

t = threading.Thread(target=trg)
t.start()

while True:
    recdata = bt.btserial()
    reqdata = dataprepro(recdata)
    if req_flag == 1:
        rq.datareq(reqdata)
        req_flag = 0