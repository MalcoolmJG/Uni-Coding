import re
import sys

#comparing how many letters are the same between the target word and the words being searched through 
def same(item, target):                                     #item is current word in list
  return len([c for (c, t) in zip(item, target) if c == t]) #count matching letters between current word and target, appends number to list

def build(pattern, words, seen, list, black): #pattern is word with '.' replacing a letter 
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and #seen.keys looks at the words in the seen list
                    word not in list and word not in black]

def find(word, words, seen, target, path, black):                          #word is start variable
  list = []                                                         #list of words matching the start word
  for i in range(len(word)):                                        #repalce letter in starting word with . to ???
    list += build(word[:i] + "." + word[i + 1:], words, seen, list, black) #call build() function
  if len(list) == 0:                                                #if no matching words are found 
    return False
  list = sorted([(same(w, target), w) for w in list])               #call same() function and sort list by number of matching letters
  list.sort(reverse=True)
  for (match, item) in list:                                        #match is number in list, item is word
    if match >= len(target) - 1:                                    #this one ends the loop find( ) loop
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:  #searching through the new word
    path.append(item)         #continues the find() loop with new word
    if find(item, words, seen, target, path, black):
      return True
    path.pop()

def lists(name, word, words):
    try:
        file = open(name)                      #opens file for reading
        lines = file.readlines()                #adds all words to a list
        while True:                             #Start loop
            for line in lines:                    #loops through each line
                word = line.rstrip()                #removes end of line character
                if len(word) == len(start):         #adds only words with the 
                    words.append(word)                #same number of characters to word
            break    
    except FileNotFoundError:
        print("Wrong file or file path")
        sys.exit()

fname = input("Enter dictionary name: ")#Enter dictionary file name to search through
blist = input("Enter Blacklist name: ") #Enter blacklist
start = input("Enter start word:").replace(" ","")    #Starting word to change
target = input("Enter target word:").replace(" ","")#enter the target word
words = []
black = [] 
if len(start) != len(target):
    print("Target and Start words do not match lengths")
    sys.exit()


if fname.lower().endswith('.txt') and fname != '':  #check file type
    lists(fname, start, words) 
elif fname == '':                                   #use default dictionary
    fname = 'dictionary.txt'
else:
    fname = print("Wrong file for dictionary")
    sys.exit()    
if blist.lower().endswith('.txt') and blist != '': #check file type
    lists(blist, start, black)
elif blist == '':
    blist = blist 
else:
    fname = print("Wrong file type for blacklist")
    sys.exit()
if any(str.isdigit(c) for c in start) or any(str.isdigit(c) for c in target):
    print("Please enter letters only")
    sys.exit()
path = [start]                              #output path list 
seen = {start : True}                       #Adds the start value to seen list
print(words)
if find(start, words, seen, target, path, black):  #call find() function
  path.append(target)                       #add the ??`? to the path list
  print(len(path) - 1, path)                #print the path and how long it took to get there
else:                                       #find function can't find a path
  print("No path found")                    #print if no path found

