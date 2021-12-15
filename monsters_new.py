#ACTUAL INPUT
# input_arr=[2,123,78,130,10,0]
# input_arr=[3,100,101,100,304,100,1,524]

#test inputs
# input_arr=[6,123,120,112,143,156,300,250,12,14,25,1,100,13]

input_arr = input()

input_arr = [int(each) for each in input_arr.split(',')]
# print(input_arr)

num_of_monsters = input_arr[0]
# print('num of mon', num_of_monsters)

xp = input_arr[1]
# print('xp', xp)

power = [ input_arr[i] for i in range( 2, num_of_monsters + 2)]
# print('power', power)

bonus = [ input_arr[i] for i in range( num_of_monsters + 2, len(input_arr))]
# print('bonus', bonus)

monsters = list(zip(power,bonus))
# print('monsters',monsters)

monsters.sort()
# print('monsters sorted',monsters)

killable = 0
for monster in monsters:
    if monster[0] <= xp:
        xp += monster[1]
        killable += 1
        # print('new xp', xp)
        # print("new monsters",monsters)

print(killable)