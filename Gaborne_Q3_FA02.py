
steps = [
    [7800, 12300, 4600, 15000, 9100],  
    [8400, 13200, 5700, 10200, 7600],  
    [11900, 8800, 14100, 6300, 9700]   
]
names = ["Jungwon", "Heeseung", "Jay"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print("Daily steps (Monday to Friday):")
for i in range(len(names)):
    print(names[i], ":", steps[i])
