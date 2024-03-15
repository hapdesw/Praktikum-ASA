container_capacity = int(input())
weights = [int(i) for i in input().split()]

def maximize_items(container_capacity, weights):
    total_weights = 0
    Returns = 0
    for i in weights:
        total_weights += i
        if total_weights <= container_capacity:
            Returns += 1
    return Returns

print(maximize_items(container_capacity, weights))