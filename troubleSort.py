tests=int(input())

for test in range(tests):
    n=int(input())
    nums=list(map(int,input().split()))
    #splitting the array 
    #sorted the slicing array
    odds=sorted(nums for num in nums[1::2])
    evens=sorted(nums for num in nums[::2])

    finalList=[]
    
    # Interleaving the spliced and sorted arrays
    for num1, num2 in zip(evens, odds):
        finalList.append(num1)
        finalList.append(num2)
    if len(evens) > len(odds):
        finalList.append(evens[-1])
    badIdx = -1
    # Check if combined array is sorted, if not - store the first index of sorting error in 'badIdx'
    for i in range(len(nums) - 1):
        if(finalList[i] > finalList[i+1]):
            badIdx = i
            break
    
    if badIdx == -1:
        print(f"Case #{test}: OK")
    else:
        print(f"Case #{test}: {badIdx}")