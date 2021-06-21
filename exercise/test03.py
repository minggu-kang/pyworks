# Q1

a = " Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a : print("need")
else: print("none")

print("="*50)

# Q2

result = 0
i = 1
while i <=1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

print("="*50)

# Q3

i = 0
while True:
    i += 1
    if i >5 :break
    print("*"*i)

print("="*50)

#이중 for 문

for i in range(1,6):
    for j in range(1,i+1): 
        print("*",end='')
    print()



print("="*50)

# Q4
for i in range(1,101):
    print(i)


print("="*50)

# Q5
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
number = len(A)
for score in A :
    total += score
average = total / number
print(average)    

print("="*50)

# Q6
