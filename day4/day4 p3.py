nums = [8,1,2,2,3]
counts = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if i!= j and nums[j] < nums[i]:
            count += 1
    counts.append(count)
print(counts)
