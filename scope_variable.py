class Class1:  
    global w
    def __init__ (self,a=1): 
        w=22
        self.x=a
        print('in __init__ () self.x =',self.x,' a =',a,' w =',w)
    
    def m1(self): 
        self.y=90  
        z=w=2
        print('in m1(self)... self.y is ',self.y,'z = ',z,' w =',w)

    def m2(s): 
        w=1
        print('in c1.m2()..w is ',w)
        print('in c1.m2()..x is ',s.x)
        print('in c1.m2()..y is ',s.y)

c1=Class1() 
c1.m1()
c1.x+=c1.y 
c1.m2()
