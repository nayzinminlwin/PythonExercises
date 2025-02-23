
class Solution:
    def stringTesting(self)->None:
        credit_card = "123-456-789-1000"

        # stringArray[start:stop:step]
        last_four = credit_card[-4:]
        print(f"Your credit card : XXX-XXX-XXX-{last_four}")

        reversed = credit_card[::-1]
        print(f"Reversed: {reversed}")

        every_second = credit_card[::2]
        print(f"Every Other: {every_second}")

        every_second_reversed = credit_card[-1::-2]  # -1 is the last character
        print(f"Every Other Reversed: {every_second_reversed}")

    def formatSpecifiers(self)->None:
        number1 = 123.88
        number2 = -923784.222
        number3 = 432.1
        number4 = 0.0

        print(f"number1:{number1:+015.2f}") 
        #+ mean show + if positive, 015 mean take 15 place, filling with 0, .2f :2decimal places
        print(f"number2:{number2:^+15.2f}")
        # ^ mean align centre
        print(f"number3:{number3:<15.2f}")
        # < : align left
        print(f"number4:{number4:>15.3f}")
        # > : align right

    def loopTesting(self)->None:
        for i in reversed(range(10,0,-1)):
            print(i)

    
    def DataStructure_Arrays_Ex1(self)->None:
        monthlyExpense = [2200,2350,2600,2130,2190]
        print(f"1. In Feb, I spend ${monthlyExpense[1]-monthlyExpense[0]} extra than Jan.")
        print(f"2. Total spent in first quatar is ${monthlyExpense[0]+monthlyExpense[1]+monthlyExpense[2]}.") 
        if 2000 in monthlyExpense :
            print(f"3. $2k is spent on {monthlyExpense.index(2000)+1}th month.")
        else :
            print("3. There is no month spent exactly $2k.")
        monthlyExpense.append(1980)
        print(f"4. Spent in new month,June is ${monthlyExpense[-1]}.")
        monthlyExpense[3]-=200
        print(f"5. Expense in April after getting $200 refund ${monthlyExpense[3]}.")

    def DataStructure_Arrays_Ex2(self)->None:
        heros=['spider man','thor','hulk','iron man','captain america']
        print(f"1. Length of the list is {len(heros)}.")
        heros.append("Black Panther")
        print(f"2. List after adding BP : {heros}")
        heros.remove("Black Panther")
        heros.insert(3,"Black Panther")
        print(f"3. List after switching BP : {heros}")
        heros[1:3]=['Doctor Strange']
        print(f"4. List after replacing 2 heros : {heros}")
        # print(dir(heros))
        heros.sort()
        print(f"5. Heros after sorted {heros}")

    def DataStructure_Arrays_Ex3(self)->None:
        # numCount = int(input("How many odd numbers u want : "))
        # oddArr = [1]
        # for i in range(numCount):
        #     oddArr.append(oddArr[i]+2)
        # print(oddArr)

        maxNum = int(input("Enter the max number : "))
        oddArr = [1]
        while(oddArr[-1]<maxNum-1):
            oddArr.append(oddArr[-1]+2)

        print(oddArr)




sol = Solution()
# sol.stringTesting()
# sol.formatSpecifiers()
# sol.loopTesting()
# sol.DataStructure_Arrays_Ex1()
# sol.DataStructure_Arrays_Ex2()
sol.DataStructure_Arrays_Ex3()