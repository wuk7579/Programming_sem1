
start = int(input("From which number do you want to start?:"))
end = int(input("Which number you want to end?:"))
output = ""
for i in range(start, end+1, +2):
    output = output+ str(i) + " "
print(output)
