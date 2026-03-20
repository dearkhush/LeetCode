class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        a = 0
        for i in range(2,(int(num**0.5)+1)):
            if (num%i)==0:
                a=a+i
                if i!=num/i:
                    a+= num/i
                    
        if num >1:
            a=a+1
                

        print(a)
        return a == num
        

        