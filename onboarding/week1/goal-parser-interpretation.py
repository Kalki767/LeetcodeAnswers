class Solution:
    def interpret(self, command: str) -> str:
        a = ""
        m = []
        for i in command:
            if i=="("or i=="a" or i=="l":
                 m.append(i)
            elif i=="G":
                  a+=i
            else:
                n = m.pop()
                if n=="(":
                     a+="o"
                else:
                    a+="al"
        return a
        