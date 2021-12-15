#%% init block
jobs = ['kitchen ','garden  ','cleaning','woodwork']    #list of jobs
n = len(jobs)   # get count of groups
cycle = n   # store count of groups in cycle and preserve N
startIndex = 0  # assign start index as 0
#%% looper
for i in range(4):  #loop for number of schedules needed
    for each in jobs:   # loop for each job in job list
        print(str((cycle % n)) + "\t:\t" + str((startIndex + cycle) % n))   #print schedule
        cycle += 1  # increment cycle
    startIndex += 1 # increment startindex
    print("\n")
# %%
