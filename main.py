def twoSum(nums, target):
    tmp_list=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                tmp_list.append(i)
                tmp_list.append(j)
                return tmp_list
