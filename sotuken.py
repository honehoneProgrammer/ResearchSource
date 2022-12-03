input_string = "2 3 1"

nums = input_string.split(" ")

if(nums[0] >= nums[1]):
	if(nums[0] >= nums[2]):
		print(nums[1] + " " + nums[2] + " " + nums[0])
	else:
		print(nums[0] + " " + nums[1] + " " + nums[2])
else:
	if(nums[1] >= nums[2]):
		print(nums[0] + " " + nums[2] + " " + nums[1])
	else:
		print(nums[1] + " " + nums[0] + " " + nums[2])

print(" ".join(nums))