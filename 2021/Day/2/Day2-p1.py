from aocd import data

input = [step.strip().split() for step in data.splitlines()]

horiz_pos = 0
vert_pos = 0

for step in input:
    if step[0] == 'forward':
        horiz_pos += int(step[1])
    if step[0] == 'down':
        vert_pos += int(step[1])
    if step[0] == 'up':
        vert_pos -= int(step[1])

print(horiz_pos)
print(vert_pos)
print(horiz_pos * vert_pos)    
