def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            print( [diff, num])
        seen.add(num)

sum_pairs([4, 3, 2, 3, 4],6)
    






