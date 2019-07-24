class characterCount:
    variable=""
    def isString(self,temp):
    
        if (type(temp)==str):
            self.variable=temp
            print(self.variable)
        else:
            print("invalid")

    def charCount(self):
        count=0
        for char in self.variable:
            count+=1
        return count

cc=characterCount()
cc.isString(temp="abc")
print(cc.charCount())