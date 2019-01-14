def dcp18():
    nums = [10, 5, 2, 7, 8, 7]    
    k = input("Give us a number: ")
    type(k)
    for x in range (len(nums)):
        maximum = 0
        if (x + int(k) - 1 < len(nums)):
            maximum = nums[x]
            comp = 0
            if (nums[x+2] < nums[x+1]):
                comp = nums[x+1]
            else:
                comp = nums[x+2]
            if (comp < maximum):
                print(maximum)
            else:
                print(comp)
    print ("Done with DCP18")
                
dcp18()
