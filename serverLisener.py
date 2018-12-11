# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:28:08 2018

@author: Rotem Goren
"""

import socket 
import struct
import numpy as np  
# import thread module 
import threading 
from queue import Queue
import time

#print_lock = threading.Lock() 
  
# thread fuction 
def lisener(c,q): 
    while True: 
        start=time.time()
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
              
            # lock released on exit 
            #print_lock.release() 
            break
  
        # reverse the given string from client 
        #data = data[::-1] 
        data=np.array(struct.unpack('>12d', data))
        
        #print (data)
        q.put(data)    
        #print('Took',time.time()-start)
        print(q.qsize())
        # send back reversed string to client 
        #c.send(data) 
  
    # connection closed 
    
    c.close() 
    print ('connection close')

def processing(q): 
    while t1.isAlive():
        if(q.qsize()>0):
            data=q.get()
            print(data)
            print('Num Elements:' , q.qsize())
       
  
host = '127.0.0.1' 
  
# reverse a port on your computer 
# in our case it is 12345 but it 
# can be anything 
port = 12347
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port)) 
print("socket binded to post", port) 
  
# put the socket into listening mode 
s.listen(2) # how many clients 
print("socket is listening") 
  
# a forever loop until client wants to exit 

q=Queue()


  
# establish connection with client 
c, addr = s.accept() 

# lock acquired by client 
#print_lock.acquire() 
print('Connected to :', addr[0], ':', addr[1]) 
# Start a new thread and return its identifier 
t1=threading.Thread(target=lisener,args=(c,q))
t1.daemon=True;
t1.start()


loop=t1.isAlive()
t2=threading.Thread(target=processing,args=(q,))
t2.daemon=True;
t2.start()

 
    

    
s.close() 
  
