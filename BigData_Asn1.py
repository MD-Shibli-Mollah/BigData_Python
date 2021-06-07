


# def common_divisors(x, y):
#
#     my_list = []
#     for i in range(1, min(x, y) + 1):
#         if x % i == y % i == 0:
#             my_list.append(i)
#     return my_list
#
#
# # Function call
# my_result = common_divisors(12, 24)
# print(my_result)

# # Assignment 1
# #Participant's Name: MD SHIBLI MOLLAH
# # input is a text file & output should be like this
# # {'am': 1, 'python': 1, 'affraid': 1, 'want': 1, 'learn': 1, 'of': 1, 'to': 1, 'I': 2, 'python.': 1, 'But': 1}
#
# import time
# import sys
#
# start_time = time.clock()
#
# myFile = open("C:\\Users\\user\Desktop\\BIGDATA\\assign.txt")
#
# print("filename is: ")
# args = sys.argv[0:]
#
# if args:
#         file_name = args[0]
#         print(file_name)
#         fp = open(file_name)
# contents = fp.read()
#
# counts = 0
# words = 0
# counts = dict()
#
# for line in myFile:
#     words = line.split()
#     print(words)
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] = counts[word] + 1
#
# ###output will be printed here as counts
# print(counts)
# end_time = time.clock()
# time_diff = end_time - start_time
# print("The running time of my program is: %s seconds" % time_diff)
# exit(0)
