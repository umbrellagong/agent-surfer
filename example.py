def mean(nums):
    s = 0
    for i in nums:
        s += i
    return s/len(nums)

def variance(nums):
    m = mean(nums)
    s = 0
    for x in nums:
        s += (x-m)**2
    return s/len(nums) 