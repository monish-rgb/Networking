import socket
import pandas as pd
import numpy as np
import csv
df = pd.read_csv(r"C:/Users/monis/Desktop/Airplane-maintenance.csv")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))
ch = input(s.recv(1000).decode("utf-8"))
s.send(ch.encode("utf-8"))

if(ch == 'I'):
    n = int(input("Enter number of rows to be inserted :"))
    s.send(str(n).encode("utf-8"))
    for i in range(1, n + 1):
        fn = input(s.recv(1000).decode("utf-8"))
        s.send(fn.encode("utf-8"))
        
        load = input(s.recv(1000).decode("utf-8"))
        s.send(load.encode("utf-8"))
        
        sensors = input(s.recv(1000).decode("utf-8"))
        s.send(sensors.encode("utf-8"))
        
        engines = input(s.recv(1000).decode("utf-8"))
        s.send(engines.encode("utf-8"))
        
        lm = input(s.recv(1000).decode("utf-8"))
        s.send(lm.encode("utf-8"))
        
        hm = input(s.recv(1000).decode("utf-8"))
        s.send(hm.encode("utf-8"))
        
        seats = input(s.recv(1000).decode("utf-8"))
        s.send(seats.encode("utf-8"))

        check = input(s.recv(1000).decode("utf-8"))
        s.send(check.encode("utf-8"))
        
elif(ch == 'V'):
    view=(s.recv(5000).decode("utf-8"))
    print(df)
    
elif(ch=='N'):
    print("Number Of Planes Unchecked Are = ",s.recv(1000).decode("utf-8"))
    
elif(ch=='U'):
    print("Planes Unchecked Are : ")
    unchecked_planes=s.recv(1000).decode("utf-8")
    print(unchecked_planes)