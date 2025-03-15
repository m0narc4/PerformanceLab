nums = []
file = input()

with open(file) as f:
    for line in f:
        nums.append(int(line.rstrip()))

nums.sort()

if len(nums) % 2 == 0:
    index = int(len(nums) / 2)
else:
    index = (len(nums) // 2) - 1

count = 0
reduced_number = nums[index]

for elem in nums:
    count += abs(elem - reduced_number)

print(count)

