class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        min_list=[]
        max_list=[]
        p=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                min_list.append(nums[i])
            elif nums[i]>pivot:
                max_list.append(nums[i])
            elif nums[i]==pivot:
                p.append(nums[i])
        nums=min_list+p+max_list
        return nums
                
            