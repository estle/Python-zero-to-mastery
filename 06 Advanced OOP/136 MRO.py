# Method Resolution Order
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # order: DBCA
print(D.mro())  # same as .__mro__ method
D.__str__

# The things is, if even u write complex inherited code to get the answer in what order classes are called USE MRO(), solution for future problems that might occure
