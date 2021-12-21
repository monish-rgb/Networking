import socket
import pandas as pd
import numpy as np
import csv


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
        
        
elif(ch == 'V'):
    #while True:
        #data = s.recv(409600)          
        #print(repr(data))
        #if not data: break
    #print("Done Receiving")
    data=s.recv(1024).decode()
    print(data)
    print("Done Receiving")
    
elif(ch=='C'):
    print(s.recv(1000).decode("utf-8"))
    
elif(ch=='B'):
    print("Pass is not issued to these luggage ID due to Overweight (or) \nItems does'nt pass the security requirements that our Airport need.\n  : ")
    unchecked_luggage=s.recv(1000).decode("utf-8")
    print(unchecked_luggage)
    
    BP = input(s.recv(1000).decode("utf-8"))
    s.send(BP.encode("utf-8"))