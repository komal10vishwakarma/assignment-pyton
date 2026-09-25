class Addition:
    def add(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
    def display(self):
        return self.c

x=Addition()
x.add(30,45)
y=x.display()
print("the sum is",y)
    
    