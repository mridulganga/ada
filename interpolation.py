def interpolate(nums,key,low,high):
    pos = low + ((key - nums[low])*(high-low))/(nums[high]-nums[low])
    if nums[pos] == key:
        return pos
    elif nums[pos] < key:
        return interpolate(nums,key,pos+1,high)
    else:
        return interpolate(nums,key,low,pos-1)

str_nums = raw_input("Enter the numbers \n ")
nums=[]
for x in str_nums.split(" "):
    nums.append(int(x))

key = int(raw_input("Enter the Key : "))

print interpolate(nums,key,0,len(nums)-1)
