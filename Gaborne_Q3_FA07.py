import numpy as np

steps = np.array([
    [7800, 12300, 4600, 15000, 9100],  
    [8400, 13200, 5700, 10200, 7600],  
    [11900, 8800, 14100, 6300, 9700]   
])

names = ["Jungwon", "Heeseung", "Jay"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print("Step Count Summary:\n")

for i in range(len(steps)):
    total = steps[i].sum()
    average = steps[i].mean()
    
    print(names[i], "steps:", steps[i])
    print("Total steps:", total)
    print("Average steps:", round(average, 2))
    print()

max_steps = steps.max()
print("Highest step count recorded:", max_steps)