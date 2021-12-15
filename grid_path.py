# inp=[2,[1,2],[3,4]]
# inp=[2,[7, 8],[5, 5]]
# inp=(3,[1, 1],[2, 2],(3, 3))
# inp = (3,[1, 1],[2, 4],(3, 2))
inp = (3, [1, 1], [2, 4], (4, 2))

res = 0
table = inp[1:]

curr_row_max = 0
prev_row_max = 0

for row in table:
    curr_row_max = max(row)
    if curr_row_max > prev_row_max:
        res += curr_row_max
        prev_row_max = curr_row_max # store prev val
    else:
        break
        
print(res)

