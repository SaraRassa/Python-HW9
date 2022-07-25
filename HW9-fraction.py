def show_menu():
    print('1_ Sum')
    print('2_ Subtract')
    print('3_ Multiple')
    print('4_ Divide')
    print('5_ Exit')

class fraction:
    def __init__(self,s,m):
        self.soorat= s
        self.makhraj= m

    def show(self):
        print('Ans=',self.soorat,'/',self.makhraj)

    def sum(self,guess):
        result= fraction(None,None)
        result.soorat= self.soorat*guess.makhraj + self.makhraj*guess.soorat
        result.makhraj= self.makhraj*guess.makhraj
        return result

    def sub(self,guess):
        result= fraction(None,None)
        result.soorat= self.soorat*guess.makhraj - self.makhraj*guess.soorat
        result.makhraj= self.makhraj*guess.makhraj
        return result

    def mult(self,guess):
        result= fraction(None,None)
        result.soorat= self.soorat * guess.soorat
        result.makhraj= self.makhraj * guess.makhraj
        return result

    def div(self,guess):
        result= fraction(None,None)
        result.soorat= self.soorat * guess.makhraj
        result.makhraj= self.makhraj * guess.soorat
        return result

while True:
    show_menu()
    choice=int(input('Select an option: '))
    if choice==5:
        exit()
    else:
        a= fraction(int(input('S1: ')),int(input('M1: ')))
        b=fraction(int(input('S2: ')),int(input('M2: ')))

        if choice==1:
            c= a.sum(b)
            c.show()
        elif choice==2:
            d= a.sub(b)
            d.show()
        elif choice==3:
            e= a.mult(b)
            e.show()
        elif choice==4:
            f= a.div(b)
            f.show()
