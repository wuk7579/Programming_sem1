import random
numsList = []
for i in range(0,4):
    numslist.append([i])
    for j in range(0, 4):
        numlist[i].append(random.randiant(0, 100))
for nums in numslist:
    output = ""
    for num in nums:
        output += str(num)+ " "
    print(output)

div = int(input("please enter a num:")
count = 0
for nums in numslist:
    for num in nums:
        if num/div == 0:
          count += 1
print("There are", count, "numbers divisible by" , div,"in the list")
