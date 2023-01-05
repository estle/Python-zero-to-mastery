class MyGen():
    def by_seven(self, n):
        for i in range(0, n+1, 7):
            yield i

for i in MyGen().by_seven(int(input())):
    print(i)