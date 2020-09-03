n = int(input("Enter the length of the sequence: ")) # Do not change this line

tala1 = 1
tala2 = 2
tala3 = 3
tala4 = 0
print(tala1)
print(tala2)
print(tala3)
for i in range(0,n):
    tala4 = tala1 + tala2 + tala3
    tala1 = tala2
    tala2 = tala3
    tala3 = tala4
    print (tala4)
    
