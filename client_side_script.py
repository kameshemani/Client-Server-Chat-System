#Student Name : Kamesh Emani
#Latech ID: 10244797

#Client side script to send data to the server, wait for reply from the server for only 1 second and then send an other message 

#References
#https://docs.python.org/2/library/socket.html
#https://docs.python.org/2/library/time.html
#http://www.tutorialspoint.com/python/python_networking.htm

#Importing all the functions from Socket Module
from socket import *

#Importing time module to count the Round Trip time
import time

#Setting Host as local host ("127.0.0.1") which can be set to any IP if required
HOST="127.0.0.1"

#Setting Port to 12000
PORT = 12000

#In this command AF_INIT is used to select IPV4 Address group and SOCK_DGRAM is protocol for UDP Functionality
clientSocket = socket(AF_INET,SOCK_DGRAM)

#Setting timeout time to 1 second so that if server does not response back in 1 second, it does not wait any more and sends next message
clientSocket.settimeout(1)

#Setting Sequence_number initially to 1
sequence_number = 1

#count variable
count=0

#intialize the round trip time to 0
round_trip_time = 0 

#setting the initial start time
start_time=time.time()

#Running while loop such that it terminates when sequence_number is greater than 10
while sequence_number<=10:
    #setting message to Ping
    message = "Ping"
    #Sending message to the server on port 12000
    clientSocket.sendto(message,(HOST,PORT))
    #try for 1 second
    try:
        #Receive response message from the server
        response_message, address = clientSocket.recvfrom(1024)
        #calulating Round trip time by subtracting start time from instant_time i.e. present time
        round_trip_time =((time.time() - start_time) - count - round_trip_time)   
        #Printing the output as per assignment requirements i.e. response message from server, sequence number and round trip time
        print response_message + " Sequence_number " + str(sequence_number) + " Round Trip Time " +  str(round_trip_time) + " in seconds"
        print ""
    #if 1 second exceeds then print exception Request timed out
    except:
        #If server does not respond back in 1second then print for that sequence number the request timed out
        print  "For  Sequence_number " + str(sequence_number) + " Request timed out"
        print""
        count=count+1
    #Increment sequence number
    sequence_number = sequence_number +1
    print(time.time() - start_time)
