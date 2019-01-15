def dcp18():
    nums = [10, 5, 2, 7, 8, 7,9,18,33,2,97,10,3]
    k = input("Give us a number: ")
    type(k)
    x=0
    while x+int(k)< (len(nums)):        
        c = x 
        maximum= nums[c]
        for y in range (x, x+int(k)):
            if nums[y]>maximum:
                maximum=nums[y]
        print(maximum)
        x=x+1
    print ("Done with DCP18")
while True:
    choice = input("Which DCP do you wanna run?")
    type(choice)
    if choice=="18":
        dcp18()
    else:
        print("Fuck Off")
