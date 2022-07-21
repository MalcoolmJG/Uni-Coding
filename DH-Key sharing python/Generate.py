#File used to generate initial/ new Prime, Primitive root modulo, Alice key and Bob key.
import PRM, os, random, time
from sympy import randprime
#Finds/ creates txt files.
path = os.path.dirname(os.path.abspath(__file__))   #Finds relative path
publicFile = "Public.txt"                           #Public file
file_path = os.path.join(path, publicFile)          #Join path/ file to open
publicFile = open(file_path, "w")                   #Open Public file to write to
aliceFile = "Alice.txt"                             #Alice file
file_path = os.path.join(path, aliceFile)           #Join path/ file to open
aliceFile = open(file_path, "w")                    #Open Alice file to write to
bobFile = "Bob.txt"                                 #Bob file
file_path = os.path.join(path, bobFile)             #Join path/ file to open
bobFile = open(file_path, "w")                      #Open Bob file to write to 
#Finds random prime.
print("Generating random prime. Please wait.")      
time.sleep(2)
p = randprime(100, 1500)                            #Generate random prime, limit to between 100 and 1500 for reasonable Primitive root modulo finding  
publicFile.write(str(p))                            #Writes p to public.txt
publicFile.write("\n")                              #line break 
print("The public prime, p =", p,".")               
#Lists/ choose random PRM.
print("Calculating Primitive Root Modulos. Please wait.")
prm = PRM.primRoots(p)                              #Runs PRM.py
g = random.choice(prm)                              #Chooses random PRM for g
print("There are ", len(prm), "PRMs, selecting one randomly.")
time.sleep(2)
print("The primitive root modulo, g = ", g,".")     
time.sleep(2)
publicFile.write(str(g))                            #Writes g to public.txt
publicFile.write("\n")                              
#Create Alice key.
aliceKey = random.randint(1, p-1)                   #Choose random int below chosen prime 
aliceFile.write(str(aliceKey))                      #Write Alice's secret key to file
aliceFile.write("\n")                               
print("Alices private key has been chosen.")
time.sleep(2)
#Create Bob key.
bobKey = random.randint(1, p-1)                     #Choose random int below chosen prime 
bobFile.write(str(bobKey))                          #Write Bobs's secret key to file
bobFile.write("\n")                                 
print("Bob's private key has been chosen.")
time.sleep(2)
#Create Alice public key.
apk = g**aliceKey%p                                 #Formula to generate the public key 
publicFile.write(str(apk))                          #Writes Alice's public key to public.txt
publicFile.write("\n")      
#Create Bob public key.                       
bpk = g**bobKey%p                                   #Formula to generate the public key
publicFile.write(str(bpk))                          #Writes Bob's public key to public.txt
publicFile.write("\n")                              
#Close files.
publicFile.close()
aliceFile.close()
bobFile.close()
#Print to window.
print("Alice's public key is: ", apk, ", Bob's public key is:", bpk,".")
print("Run Alice.py and Bob.py to generate the shared secret key.")
print("Run Eve.py to see what information is public and can be eavesdropped.")
input("Press Enter to end:")