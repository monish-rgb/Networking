import socket
import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/monis/OneDrive/Desktop/stationary.csv")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))
ch = input(s.recv(1000).decode("utf-8"))
s.send(ch.encode("utf-8"))
if(ch == 'I'):
    n = int(input("Enter number of rows to be inserted :"))
    s.send(str(n).encode("utf-8"))
    for i in range(1, n + 1):
        date = input(s.recv(1000).decode("utf-8"))
        s.send(date.encode("utf-8"))
        pid = input(s.recv(1000).decode("utf-8"))
        s.send(pid.encode("utf-8"))
        qua = input(s.recv(1000).decode("utf-8"))
        s.send(qua.encode("utf-8"))
        cost = input(s.recv(1000).decode("utf-8"))
        s.send(cost.encode("utf-8"))
        
elif(ch == 'V'):
    print(df)

elif(ch == 'M'):
    df['totalcost'] = df['Quantity']*df['cost']
    df.to_csv("C:/Users/monis/OneDrive/Desktop/stationary.csv", mode='w', index=False)

elif(ch=='U'):
    df1=pd.read_csv("C:/Users/monis/OneDrive/Desktop/stationary.csv")
    df1["category"]=np.where(df1["totalcost"] > 1000,"B","A")
    df1.to_csv("C:/Users/monis/OneDrive/Desktop/stationary.csv", mode='w', index=False)
    print(df1)

elif ch == 'F':
    c = int(input("Enter  ProductId:"))
    s.send(c.encode())
    print(pd.read_csv(s.recv(1000).decode("utf-8")))
    d = input("\nEnter the Date:")
    s.send(d.encode("utf-8"))
    print(pd.read_csv(s.recv(1000).decode("utf-8")))
