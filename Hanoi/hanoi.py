from stack import Stack

num_discs = 10
tower_a = Stack()
tower_b = Stack()
tower_c = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)

print("Initial hanoi towers")
print(tower_a)
print(tower_b)
print(tower_c)

def hanoi(begin, end, temp, num_discs):
    # base case
    if num_discs == 1:
        end.push(begin.pop())
    # recursion
    else:
        hanoi(begin, temp, end, num_discs-1) # temp and end
        hanoi(begin, end, temp, 1) # base case
        hanoi(temp, end, begin, num_discs-1) # begin and temp

print("End hanoi towers")
hanoi(tower_a, tower_c, tower_b, num_discs)
print(tower_a)
print(tower_b)
print(tower_c)
