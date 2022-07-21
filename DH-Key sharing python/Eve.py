#Eve attempt to eavesdrop
import PRM, time, os, random
#Finds/ creates txt files.
path = os.path.dirname(os.path.abspath(__file__))           #Finds relative path
publicFile = "Public.txt"                                   #Public file                   
file_path = os.path.join(path, publicFile)                  #Join path/ file to open
publicFile = open(file_path, "r")                           #Open Public file to write to
publicList  = [line.rstrip('\n') for line in publicFile]    #Strips end-of-line char from list
#Print
print("Eve knows the prime,", publicList[0])
print("The primitive root modulo,", publicList[1])
print("Alice's public key,", publicList[2])
print("and Bob's public key,", publicList[3])
print("but not Alice and Bob's shared key or secret keys")
input("Press Enter to close:")