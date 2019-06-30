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

def dcp88(x,y):
    print("N/A")

def dcp216():
    def switch_roman_numerals(charToCheck):
        switcher = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
            'm': 1000,
            'd': 500,
            'c': 100,
            'l': 50,
            'x': 10,
            'v': 5,
            'i': 1            
        }
        return switcher.get(charToCheck, "Break")
    print("Roman Numeral Calculator\n")
    numToCalc = input("Please enter your desired roman numeral number: ")
    numLen = len(numToCalc)
    x = 0
    decimalVal = 0
    while x < numLen:
        checker = switch_roman_numerals(numToCalc[x])
        if checker is str:
            print("Invalid character detected quiting DCP - 216 \n")
            break
        else:
            decimalVal += checker
        x += 1
    print(f"Value is: {decimalVal}")






def main():
    while True:
        choice = input("Which DCP do you wanna run? ")
        type(choice)
        if choice=="18":
            dcp18()
        elif choice == "216":
            dcp216()
        else:
            print("Fuck Off")
main()
