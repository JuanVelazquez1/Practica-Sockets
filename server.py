import socketserver
# Doc: https://docs.python.org/3/library/socketserver.html

import random
import time
from math import trunc
# The server that receives data from the client
from datetime import datetime


# We define the helping message number
#helpMessageId = 1
#numHelpers = 0
response = "GRACIAS"
helped = False
connected = 0

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler): # changes
    def handle(self):
        
        helpMessageId = 1
        numHelpers = 0

        while True:
            self.request.sendall(bytes(str(helpMessageId) + "\n", "utf-8"))
            print("Envío el mensaje de ayuda " + str (helpMessageId))
            #time.sleep(5)
            
            try:
                data = self.request.recv(1024).strip() # recv() is the buffer
                #print(data)
                if data.decode("utf-8") == "AYUDO":
                    numHelpers += 1
                    #print("ME HAN AYUDADO MAJOS")
                else:
                    #print("NO ME HAN AYUDADO")
                    pass
                
            except:
                print("No answer")
            if numHelpers >= 3:
                print("ME HAN AYUDADO")
                break
            helpMessageId += 1


            #print("Me han respondido: " + str(data) )
            #numberOfMessageAnswered = int (data)

            #if numberOfMessageAnswered == helpMessageId:
            #    print("ME HAN AYUDADO")
            #    global numHelpers
            #    numHelpers = numHelpers + 1
            #    print(numHelpers)
            #else:
            #    print("NO ME HAN AYUDADO")
            #helpMessageId += 1
        #self.request.sendall(bytes(response + "\n", "utf-8"))
        #print(dir(self.request))
        # DOC: https://docs.python.org/3/library/socketserver.html#request-handler-objects
    
    #def handle_timeout(self):
    #    return 0

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

# A socket connection has a "file" syntax 
with socketserver.TCPServer(('', 5088), ThreadedTCPRequestHandler) as server: # localhost:5088˙
    print('The date server is running...')
    server.serve_forever()

# The client
## in our case, the client can be the OS 

# using netcat or nc commands:
# echo hola | nc localhost 5088