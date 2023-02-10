peaks = 0

nums = [int(num) for num in input().split()]
for i, num in enumerate(nums[1:-1]):
    if num > nums[i] and num > nums[i+2]:
        peaks+=1
print(peaks)
