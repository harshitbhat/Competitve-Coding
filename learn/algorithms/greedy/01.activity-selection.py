# ---------------------------------------------------------------------------- #
#                               Problem Statement                              #
# ---------------------------------------------------------------------------- #
'''
You are given n activities with their start and finish times. 
Select the maximum number of activities that can be performed by a single person, 
assuming that a person can only work on a single activity at a time. 
'''

def MaxActivities(activity, n):
    activity.sort(key = lambda x : x[1])

    selected = []

    i = 0
    selected.append(activity[0])

    for j in range(1, n):
        if activity[j][0] >= activity[i][1]:
            selected.append(activity[j])
            i = j
            
    return selected 


activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
n = len(activity)
selected = MaxActivities(activity, n)
print("Following activities are selected :")
print(selected)