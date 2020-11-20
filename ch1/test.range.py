# basic use of range, default start is 0,
# stop is 5 and it will increment +1 until
# it reaches 5 interations 0,1,2,3,4
print("basic range")
for i in range(5):
    print(i)

# use of range with start/stop/step all defined using +1
print("all args defined, +1 step")
for i in range(14,18,+1):
    print(i)
    

# use of range with start/stop/step all defined using +2
print("all args defined, +2 step")
for i in range(75,84,+2):
    print(i)

# use of range with start/stop/step all defined using -1
print("all args defined, -1 step")
for i in range(16,12,-1):
    print(i)

# use of range with start/stop/step all defined using -2
print("all args defined, -2 step")
for i in range(22,17,-2):
    print(i)
