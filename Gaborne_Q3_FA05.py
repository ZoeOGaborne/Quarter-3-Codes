
import numpy as np

steps = np.array([
    [7800, 12300, 4600, 15000, 9100],  
    [8400, 13200, 5700, 10200, 7600],  
    [11900, 8800, 14100, 6300, 9700]   
])

names = ["Jungwon", "Heeseung", "Jay"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(len(names)):
    tot_steps = np.sum(steps[i])
    avg_steps = np.mean(steps[i])
    min_steps = np.min(steps[i])
    max_steps = np.max(steps[i])
    print(
        f"{names[i]} - Total Steps: {tot_steps} | "
        f"Average: {avg_steps:.1f} | Min: {min_steps} | Max: {max_steps}"
    )

    print(f"\nPerson with the highest total steps: {names[max_index]} ({total_steps[max_index]} steps)")

difference = total_steps[max_index] - total_steps[min_index]
print(f"Difference between highest and lowest total steps: {difference} steps")