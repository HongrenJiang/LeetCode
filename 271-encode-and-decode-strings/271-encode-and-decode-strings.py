class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for i in range(len(strs)):
            res += strs[i]
            res += "¥"
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ## "Apple#Banana#Organge#"
        res, i = [], 0
        
        while(i < len(s)):
            j = i
            while s[j] != "¥":
                j += 1
            
            res.append(str(s[i:j]))
            i = j + 1
        
        return res
            


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))