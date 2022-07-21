#Bobs DH algorithm
import os
#Finds/ creates txt files.
path = os.path.dirname(os.path.abspath(__file__))           #Finds relative path
publicFile = "Public.txt"                                   #Public file                        
file_path = os.path.join(path, publicFile)                  #Join path/ file to open
publicFile = open(file_path, "r")                           #Open Public file
bobFile = "bob.txt"                                         #Bob file
file_path = os.path.join(path, bobFile)                     #Join path/ file to open
bobFile = open(file_path, "r")                              #Open bob file
#Perform DH on public keys
publicList  = [line.rstrip('\n') for line in publicFile]    #Strips end-of-line char from list
p = int(publicList[0])                                      #Public key, Prime
bpk = int(publicList[2])                                    #Bobs public key
pk = int(bobFile.readline())                                #Bobs private key
sharedKey = bpk**pk%p                                       #Shared key formula
#Close files.
bobFile.close()
publicFile.close()
#Print
print("Bob's private key is:",pk)
print("Alice and Bobs shared key is:", sharedKey) 
input("Press Enter to exit:")