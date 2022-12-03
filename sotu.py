input_string = "3 2 1"

nums = input_string.split(" ")

for _ in range(len(nums)-1):
	for i in range(len(nums)-1):
		if(nums[i] > nums[i+1]):
			tmp = nums[i+1]
			nums[i] = nums[i+1]
			nums[i+1] = tmp

print(" ".join(nums))