# 1. Read all the lists of words
# 2. Generate a random number
# 3. Take that word


# 1. 
# import random
# words = []
# with open("sowpods.txt", "r") as s:
#     for x in s:
#         sowpods = s.readline().strip()
#         words.append(sowpods)
# #for i in range(20):
#     print(random.choice(words))   

# 3.
import random
with open("sowpods.txt", "r") as f:
    line = f.readlines()   # mozna tez f.read().split()

word = random.choice(line).strip()   #strip() usuwa white space'y
print(word)  





