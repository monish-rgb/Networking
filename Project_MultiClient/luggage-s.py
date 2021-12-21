import socket
import csv
import pandas as pd
import numpy as np
from csv import writer
from _thread import *

df = pd.read_csv("C:/Users/monis/Desktop/luggage.csv")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((socket.gethostname(), 1024))
except socket.error as error:
  
    print("Sorry ! Check Your Connection Please" + str(error))

print ("Luggage Server running")
print("Waiting For Connection ........ ")

s.listen(10)
list1=[]
def threaded_client(clt):
    while True:
        ch = clt.recv(10).decode("utf-8")
        if(ch == 'I'):
            n = clt.recv(10).decode("utf-8")
            for i in range(1, int(n)+1):
                clt.send(bytes("Enter Luggage_ID :", "utf-8"))
                lid = clt.recv(1000).decode("utf-8")
                
                clt.send(bytes("Luggage Weight :", "utf-8"))
                load = clt.recv(1000).decode("utf-8")
                           
                list1=[lid,load,]
                with open("C:/Users/monis/Desktop/luggage.csv",'a', newline='') as csvfile:
        
                    writer = csv.writer(csvfile)
                    writer.writerow(list1)   
                    
        elif(ch == 'V'):
            
                #file = open('luggage.csv','rb')
                #df = file.read(1024)
                #while df:
                    #clt.send(df)
                    #break
                    #df = file.read(1024)
            clt.send(str(df).encode())
            
        elif(ch == 'C'):
            df.loc[df.Lug_Wght >= 25, "checking"] = "No"
            df.loc[df.Lug_Wght < 25, "checking"] = "Yes"
            
            df.to_csv('C:/Users/monis/Desktop/luggage.csv')
            
            clt.send(bytes("Luggages are checked ","utf-8"))
            
        elif(ch == 'B'):
            rslt = df.loc[df['checking'] == 'No']
            a=rslt['Lug_Wght']
            clt.send(str(a).encode("utf-8"))
            print("\n\n")
            
            clt.send(bytes("Enter Enter Boarding Pass Number :", "utf-8"))
            BP = clt.recv(1000).decode("utf-8")
            list2=[BP]
            with open("C:/Users/monis/Desktop/luggage.csv",'a', newline='') as csvfile:
        
                writer = csv.writer(csvfile)
                writer.writerow(list2)
        
        
while True:
    clt, adr = s.accept()
    print(f"Connected Successfully to {adr} Client")
    start_new_thread(threaded_client, (clt, ))
    clt.send(bytes("Give Following Inputs\nI for Insertion\nV for View\nC for allowing checking luggage weight and its items\nB To issue Boarding pass\n", "utf-8"))




    


