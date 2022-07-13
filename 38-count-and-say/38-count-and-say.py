class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"
        if n == 1:
            return say
        
        for i in range(n - 1):
            newSay = ""
            start = say[0]
            count = 0
            for j in range(len(say)):
                if say[j] == start:
                    count += 1
                else:
                    newSay += str(count)
                    newSay += str(start)
                    count = 1
                    start = say[j]
            newSay += str(count)
            newSay += str(start)
            say = newSay
        return say