
nums = [1,2,3,4,5,6,7]
k = 3

k %= len(nums)
for i in range(k):
    nums.insert(0,nums[-1])
    nums = nums[:-1]
print(nums)

nums = [1,2,3,4,5,6,7]
K=k%len(nums)
a = nums[k*-1:]
b = nums[:len(nums)-k]
nums = a + b
print(nums)

nums = [1,2,3,4,5,6,7]
k %= len(nums)
nums = list(reversed(nums))
nums[0:k] = list(reversed(nums[0:k]))
nums[k:] = list(reversed(nums[k:]))
print(nums)

nums = [1,2,3,4,5,6,7]
K=k%len(nums)
nums[:]=nums[-K:]+nums[:-K]
print(nums)
