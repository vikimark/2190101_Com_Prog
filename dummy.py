def find_duplicate(nums):
    tor=nums[0]
    har=nums[0]
    while True:
        tor = nums[tor]
        har = nums[nums[har]]
        print(tor, har)
        if tor == har:
            break
    pr1 = nums[0]
    pr2 = tor
    print("---")
    while pr1 != pr2:
        pr1 = nums[pr1]
        pr2 = nums[pr2]
        print(pr1, pr2)
    return pr1

print(find_duplicate([*map(int,input().split())]))