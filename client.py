import errno
import socket
# Client side
import time
import random 

host, port = "localhost", 5088
data = "2"
helped = False
lastMessage = 0
#connected = 0

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server
    sock.connect((host, port))
    sock.settimeout(1)
    #connected = 0
    #while sock.recv(1024).strip() != "EMPEZAMOS":
    #    pass
    
    while helped == False:
        wakingTime = random.randint(3, 4)
        #print(wakingTime) ##################################################################################3
        time.sleep(wakingTime)
        # Receive the id of the helpMessage
        #try: 
        try:
            received = int (sock.recv(1024)) 
            #print(received)
            if random.randint(0,100) <= 30:
                sock.sendall(bytes( "AYUDO", "utf-8"))
                print("ayudo con el mensaje ", received)
            else: 
                sock.sendall(bytes( "NO AYUDO", "utf-8"))
                print("NO ayudo con el mensaje ", received)
        except socket.error as e:
            if e.args[0] == errno.EWOULDBLOCK:
                print("HOLI")
        #received = int (sock.recv(1024)) #decoding
        
        #if lastMessage != received:
            #messageId = int (received)
            # We send help if the generated number is 30 or less
            #print("VAMO A COMPROBAR NUMEROS") ##################################################################################3
                #if random.randint(0,100) <= 30:
            #print(received)
            #sock.sendall(bytes( str(received) + "\n", "utf-8")) # coding 
        #except: sock.sendall(bytes( str(0) + "\n", "utf-8")) # coding





#print("Sent:     {}" .format(data))
#print("Received: {}".format(received)),

#sock.close()