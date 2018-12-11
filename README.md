# serverListenerProcessing
This is a way to create server listener to client data and processing the data meanwhile in parallel.
It can be use for receving online stream data and process it in parallel.
The main idea here is when connection with the client is made a thread is created and start collecting the data and put it in buffer or queue
also the process thread is created and start to pull the data from the queue and process them. 
when the connection ends the listener thread is dies, the process thread listen to listener process and if he dies the process theard also dies.
In this way we can process data without getting any data lost.
It is neccery to check that time to processing < time receving data . otherwise we will get queqe overflow. 
