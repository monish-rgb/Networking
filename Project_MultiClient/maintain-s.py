import socket
import csv
import pandas as pd
import numpy as np
from csv import writer
from _thread import *

df = pd.read_csv("C:/Users/monis/Desktop/Airplane-maintenance.csv")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((socket.gethostname(), 1024))
except socket.error as error:
  
    print("Sorry ! Check Your Connection" + str(error))

print ("Maintenance Server running")
print("Waiting For Connection ........ ")

s.listen(10)
list1=[]
def threaded_client(clt):
    while True:
        ch = clt.recv(10).decode("utf-8")
        if(ch == 'I'):
            n = clt.recv(10).decode("utf-8")
            for i in range(1, int(n)+1):
                clt.send(bytes("Enter Flight-name :", "utf-8"))
                fn = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("MAX load ", "utf-8"))
                load = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("No of Sensors: ", "utf-8"))
                Sensors = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("No of Engines: ", "utf-8"))
                engines = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("LM ?:", "utf-8"))
                lm = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("HM ?:", "utf-8"))
                hm = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("No of seats:", "utf-8"))
                seats = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("Checked ? :", "utf-8"))
                check = clt.recv(1000).decode("utf-8")
            
            
                list1=[fn,load,Sensors,engines,lm,hm,seats,check]
                with open("C:/Users/monis/Desktop/Airplane-maintenance.csv",'a', newline='') as csvfile:
        
                    writer = csv.writer(csvfile)
                    writer.writerow(list1)   
                    
        elif(ch == 'V'):
            clt.send(bytes("C:/users/monis/Desktop/Airplane-maintenance","utf-8"))
            
        elif(ch == 'N'):
            a=df[df['check'] == 'No']['F N'].count()
            a=a.item()
            clt.send(repr(a).encode("utf-8"))
            
        elif(ch == 'U'):
            rslt = df.loc[df['check'] == 'No']
            a=rslt['F N']
            clt.send(str(a).encode("utf-8"))
        
        
while True:
    clt, adr = s.accept()
    print(f"Connected Successfully to {adr} Client")
    start_new_thread(threaded_client, (clt, ))
    clt.send(bytes("Give Following Inputs\nI for Insertion\nV for View\nN To count Number Of Planes are Unchecked\nU To Check Planes That are not serviced\n", "utf-8"))




    


