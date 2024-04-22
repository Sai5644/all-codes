target =int(input())
n=int(input())
nums = list(map(int, input().strip().split()))
nums=sorted(nums)

left = 0
right =len(nums)-1
found = False
while left<=right:
    mid=(left+right)//2
    if nums[mid] == target:
        found = True
        break
    elif nums[mid]> target:
        right = mid - 1
    else:
        left = mid+1
if found == True:
    print("Target is present")
else:
    print("Target is not present")
