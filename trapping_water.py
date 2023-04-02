# brute force method - not the best
def trap_water_bruteforce(ground_array):
    water_sum = 0
    for ind, elem in enumerate(ground_array):
        left_split = ground_array[:ind]
        right_split = ground_array[ind + 1:]

        # if the left and right are filled with vals
        if left_split and right_split:
            # find the max of each list and take the min of these
            # then minus the current elem
            m = min(max(left_split), max(right_split))
            if m > elem:
                water_sum += m - elem
    return water_sum
# dynamic programming approach
def trap_water_dynamic_programming(ground_array):
    size = len(ground_array)
    if not ground_array: return 0
    sum = 0
    left_max = [ground_array[0]]
    right_max = [0] * size
    right_max[-1] = ground_array[-1]

    for ind in range(1, size):
        left_max.append((max(ground_array[ind], left_max[ind - 1])))
    ind = size - 2

    while ind >= 0:
        right_max[ind] = ((max(ground_array[ind], right_max[ind + 1])))
        ind -= 1
    for num in range(size):
        sum += min(left_max[num], right_max[num]) - ground_array[num]
    return sum
if __name__ == '__main__':
    ground_array = [0,3,5,7,5,4,4,6,7,7,7,4,4,6,3,2,2,8,2,9,5,4,5,6,6,7,8,]
    print(trap_water_dynamic_programming(ground_array))
