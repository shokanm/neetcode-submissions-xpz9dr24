class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newList = []
        for n in operations:
            if self.is_numeric(n):
                newList.append(int(n))
            else:
                match n:
                    case "+":
                        sum = 0
                        for c in newList[-2:]:
                            sum += int(c)
                        newList.append(sum)
                    case "D":
                        newVal = newList[-1] * 2
                        newList.append(int(newVal))
                    case "C":
                        del newList[-1]
        sumFin = 0
        for c in newList:
            sumFin += int(c)
        return sumFin
    def is_numeric(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False