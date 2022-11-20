# ---------------------------------------------------------------
#  GENERAL INFO:
# The server sends 20 messages with the numbers from 0 to 19
# Each of them represents the different asking help messages
# Each agent can answer HELP or NO_HELP, if the response times 
# out, it will be interpreted as a NO_HELP
# When all of the messages are sent, an END message is sent 
# and the results are printed
# ---------------------------------------------------------------
import random
import socket
import time
from _thread import *
import errno

host = '127.0.0.1'
port = 1234
# Number of helping agents connected
numAgents = 0
# Array with the number of help messages received in 20 iterations
arrayHelp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# CONSTANTS
AGENTS_NEEDED = 3
CONSENSUS = 2

# Array of random generated sleeping times.
# In order to make each connection's random sleeping time
# the same in each iteration
randomSleepTime = [0,0,0,0,0,0,0,0,0,0]

# Variable to print only once the array at the end
# Should have been done with semaphores
onlyOnce = 1

random.seed(2022)

# This method's structure is:
# - Waiting room until all 3 agents are connected
# Then, loop:
# - Send message asking for help
# - Sleep a random time
# - Receive help or no help messages
# - Loop again
def client_handler(connection):
    # Waiting room
    connection.setblocking(False)
    while numAgents != AGENTS_NEEDED:
        pass
    # Sleep to sync all 3 connections
    time.sleep(1)
    # Message ID
    numMessage = 0
    
    while True:
        for _ in range(len(arrayHelp)):
            connection.settimeout(0.1)
            # Send message asking for help
            connection.sendall(str.encode(str(numMessage)))
            time.sleep(randomSleepTime[numMessage%10])
            try:
                # Receive helping message
                data = connection.recv(2048)
                rcvMessage = data.decode('utf-8')
                # If the response is NO_HELP do nothing
                if rcvMessage == 'NO_HELP':
                    print("NO_HELP (response),   message: ", numMessage)
                    pass
                # If the response is HELP, increase the number of agents who
                # helped to the given message
                elif rcvMessage == 'HELP':
                    print("HELP,                 message: ", numMessage)
                    increase_helper(numMessage)
                # Increase message id
                numMessage = numMessage + 1
            except socket.timeout:
                # If response timedout do nothing
                print("NO_HELP (timeout),    message: ", numMessage)
                # Increase message id
                numMessage = numMessage + 1
            except socket.error as error:
                if error.args[0] == errno.EWOULDBLOCK:
                    pass
                else:
                    print(error)
        else: 
            # Send ending message
            connection.sendall(str.encode('END'))

            global onlyOnce
            # Only print once the results
            if onlyOnce == 3:
                print("")
                calculate_help_percentage()
                print('The help messages array is ', arrayHelp)
            else:
                onlyOnce += 1
        break
    connection.close()

# We accept and establish every new connection
def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    global numAgents 
    numAgents = numAgents + 1
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))

# Method that increases the number of helpers
def increase_helper(i):
    global arrayHelp
    arrayHelp[i] = arrayHelp[i] + 1

# Generate 10 random times for the sleeping times of the server
def random_times():
    for i in range(len(randomSleepTime)):
        sleepTime = random.randint(1,2)
        randomSleepTime[i] = sleepTime

# Calculate the percentage of times that helpers have helped
def calculate_help_percentage():
    helpedTimes = 0
    for numHelpers in arrayHelp:
        if numHelpers >= CONSENSUS:
            helpedTimes += 1
    print('I have been helped ' + str(100*(helpedTimes/len(arrayHelp))) + '%' + ' of the time.')

def start_server(host, port):
    ServerSocket = socket.socket()
    random_times()
    
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)
start_server(host, port)