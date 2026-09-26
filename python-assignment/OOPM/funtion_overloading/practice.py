# class A:
#     def __init__(self):
#         print("aayush")
#     def __init__(self,name):
#         print("komal")
# obj=A()
# print(obj.A("name"))

# class A:
#     def komal(self):
#         print("aayush")
#     def komal(self,age):
#         print("komal")
# obj=A()
# print(obj.komal(20))

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_brand_name(self):
        return f"{self.brand}{self.model}"
obj=Car("tata","nexon")
print(obj.brand)
print(obj.model)
print(obj.full_brand_name())
