import socket
import pandas as pd
import numpy as np
import csv

df = pd.read_csv(r"C:/Users/monis/OneDrive/Desktop/stationary.csv")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(10)
list1=[]
while True:
    clt, adr = s.accept()
    print(f"Connection established to {adr} established")
    clt.send(bytes("Input I for Insertion\nM for Modification\nV for View\nU for Updating\nF for product details\n", "utf-8"))
    ch = clt.recv(10).decode("utf-8")
    if(ch == 'I'):
        n = clt.recv(10).decode("utf-8")
        for i in range(1, int(n)+1):

            clt.send(bytes("Enter productid: ", "utf-8"))
            productid = clt.recv(1000).decode("utf-8")
            
            clt.send(bytes("Enter DATE :", "utf-8"))
            Date = clt.recv(1000).decode("utf-8")
            
            clt.send(bytes("Enter Quantity: ", "utf-8"))
            Quantity = clt.recv(1000).decode("utf-8")
            
            clt.send(bytes("Enter cost: ", "utf-8"))
            cost = clt.recv(1000).decode("utf-8")
            
            list1=[productid,Date,Quantity,cost]
            with open("C:/Users/monis/OneDrive/Desktop/stationary.csv",'a', newline='') as csvfile:
        
                writer = csv.writer(csvfile)
                writer.writerow(list1)
                
    elif(ch == 'V'):
        clt.send(str(df).encode())
        
       
    elif ch == 'F':
        c = clt.recv(1000)
        k = df.groupby('productid')
        g = k.get_group(c)
        g.to_csv("C:/Users/monis/OneDrive/Desktop/pid.csv", index=False)
        pid=pd.read_csv("C:/Users/monis/OneDrive/Desktop/pid.csv")
        clt.send(str(pid).encode())
        d = clt.recv(1000).decode("utf-8")
        k1 = df.groupby('Date')
        g1 = k1.get_group(d)
        g1.to_csv("C:/Users/monis/Desktop/Date.csv", index=False)
        clt.send(bytes("C:/Users/monis/Desktop/Date.csv", "utf-8"))


    


