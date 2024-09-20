#trying to figure out a way to load in the txt file and append to an array

'''
x = []
print(x)

with open('levels/level1.txt','r') as f:
    for x in f.read():
        a = [item.strip() for item in x.split(',')] #strip removes whitespace and split creates arrays at comma or something like that
        x.append(f)

print(x)
'''
sample_list = [

    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1],
]


world_data = []
count = 0
with open ('levels/level1.txt' , 'r') as file:
    #print(f.read())
    for x in file:
        a = [item.strip(',') for item in x.split()] #list comprehension
        #data.append(x)
        world_data.append(a)

    for x in world_data:
        for y in x:
            y = int(y)
            x[count] = y
            count += 1
            if count >= len(x):
                count = 0
            
        #data = [ int(x) for x in data ]
        #data.append(b)
print(world_data)