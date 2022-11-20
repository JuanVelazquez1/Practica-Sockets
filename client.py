import random
import socket
import time

host = '127.0.0.1'
port = 1234
counter = 0

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
while True:
    counter += 1
    # Receive message
    messageBuff = ClientSocket.recv(2048)
    message = messageBuff.decode('utf-8')

    # If it's the ending message, exit loop
    if message == 'END':
        break

    # If it's the 10th message or higher,
    # the message's id will be the 2 last characters received
    # else, it'll be the last character received
    if counter > 10:
        numMessage = message[-2:]
    else:
        numMessage = message[-1]

    print('Message received: ', numMessage)
    # Sleep random time
    sleep = random.randint(1,3)
    time.sleep(sleep)

    # Give random help
    if random.randint(1,10) <= 3:
        Input = 'HELP'
    else:
        Input = 'NO_HELP'
    # Send message
    ClientSocket.send(str.encode(Input))
    print('My response to message ' + numMessage + ' is ' + Input)
    
ClientSocket.close()
