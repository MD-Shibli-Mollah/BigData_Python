# Assignment 1
#Participant's Name: MD SHIBLI MOLLAH
# input is a text file & output should be like this
# {'am': 1, 'python': 1, 'affraid': 1, 'want': 1, 'learn': 1, 'of': 1, 'to': 1, 'I': 2, 'python.': 1, 'But': 1}

import time
import sys
import os

start_time = time.clock()

args = sys.argv[1:]

counts = dict()
if args:
 for i in args:
  if os.path.exists(i):
 # print(i)
   fp = open(i)
   if fp:
    for line in fp:
     words = line.split()

     for word in words:
       if word not in counts:
          counts[word] = 1
       else:
          counts[word] = counts[word] + 1
  else:
   my_dirs = os.listdir(os.getcwd())
   print(my_dirs)
   for root, dirs, files in os.walk('.'):
      for file in files: # loops through directories and files
     # for file in files: 
       if file == i: # compares to your specified conditions
            print("File exists")
            print(file)
   print("%s does not exist" %i)

###output will be printed here as counts
print(counts)
end_time = time.clock()
#print(end_time)
time_diff = end_time - start_time
print("The running time of my program is: %s seconds" % time_diff)
exit(0)
