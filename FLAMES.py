'''
FLAMES :
    Friends, Lovers, Affectionate, 
    Marriage, Enemies, Siblings
'''

flames = ['Friendship', 'Love', 'Affection', 
    'Marriage', 'Enemy', 'Siblings']


#name input
name1 = list(input("Enter the first name : "))
name2 = list(input("Enter the second name : "))


#find & remove common letters
trial1 = [ch for ch in name1 
            if ch not in name2]

trial2 = [ch for ch in name2 
            if ch not in name1]

name3 = trial1 + trial2    #new list



#iterating over flames
i = 1
j = 0
while len(flames) > 1:    #ends only when last flames left
    
    if i == len(name3):   #runs at end of name3
        flames.pop(j)
        i = 0

    if j+1 >= len(flames):
        j = 0
    else:
        j+=1

    i+=1

# ''.join(list1) -> converts list[] to str " "
print(f"{''.join(name1)} and {''.join(name2)} will have {''.join(flames)}!!")
