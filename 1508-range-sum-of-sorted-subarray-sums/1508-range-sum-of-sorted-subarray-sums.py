class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD=10 ** 9+7
        subarr_sums=[]
        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                cur_sum=(cur_sum+nums[j])%MOD
                subarr_nums.append(cur_sum)
                
        