nums=(85,24,56,78,9,34)
print(nums)
print("Highest number:", max(nums))
print("Lowest number:", min(nums))
print("Total sum:", sum(nums))

print("Even numbers in list: ")
for num in nums:
	if num%2==0:
		print(num)