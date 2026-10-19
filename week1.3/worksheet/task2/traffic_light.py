"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
try:
       maxtime = int(input('Number of Steps '))  # read an integer number of steps (>0)
       if maxtime <= 0:
               exit()
except:
        exit()
state = "red"
timeActive = 0

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
for systime in range (1, maxtime + 1):
    duration = states[state]
    timeActive = timeActive + 1
    if timeActive == duration:
        if state == 'red':
            state = 'red_amber'
            timeActive = 0
        elif state == 'red_amber':
                    state = 'green'
                    timeActive = 0
        elif state == 'green':
                    state = 'amber'
                    timeActive = 0
        elif state == 'amber':
                    state = 'red'
                    timeActive = 0
    print(f"Time {systime:03} State {state}")

                
                        


    


    

# At the end of each step you should output the time and state using the statement on line 14