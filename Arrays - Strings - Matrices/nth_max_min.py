def sec_max_min(nums):
    max = min = max2 = min2 = max3 = min3 = max4 = min4 = nums[0]

# First Max and Min
    for num in nums:
        if num > max:
            max = num
        if num < min:
            min = num

# Second Max and Min
    for num in nums:
        if num > max2 and num != max:
            max2 = num
        if num < min2 and num != min:
            min2 = num

# Third Max and Min
    for num in nums:
        if num > max3 and num != max and num != max2:
            max3 = num
        if num < min3 and num != min and num != min2:
            min3 = num

# Forth Max and Min
    for num in nums:
        if num > max4 and num not in [max, max2, max3]:
            max4 = num
        if num < min4 and num not in [min, min2, min3]:
            min4 = num

    return min, min2, min3, min4, max4, max3, max2, max

list = nums = [4,4,3,3,4,7,7,0,9,2,6,8,1,99,10,8,0,3,99]
result = sec_max_min(list)
print(result)