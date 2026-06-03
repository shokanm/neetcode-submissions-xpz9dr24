class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)<2):
            return False
        stack = []
        listStr = list(s)
        lastEl = ""
        for ss in s:
            if(ss == "(" or ss == "[" or ss == "{"):
                stack.append(ss)
                print("stack ", stack)
            if(ss == ")" or ss == "]" or ss == "}"):
                if(len(stack)>0):
                    lastEl = stack.pop()
                else: 
                    return False
                print("lastEl ", lastEl)
                if(lastEl == "[" and ss != "]"):
                    return False
                if(lastEl == "(" and ss != ")"):
                    return False
                if(lastEl == "{" and ss != "}"):
                    return False
                lastEl = ""
            
        if(len(stack)>0):
            return False
        return True