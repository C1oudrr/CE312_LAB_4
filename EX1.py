class cylender1():
    radius = 5
    height = 10

    def cal(self):
        self.cal = 3.14 * (self.radius * self. radius) * self.height
        return self.cal
class cylender2():
    radius = 7
    height = 13

    def cal2(self):
        self.cal2 = 3.14 * (self.radius * self.radius) * self.height
        return self.cal2

c1 = cylender1()
c2 = cylender2()

print("1st cylinder = ",str(c1.cal()))
print("1st cylinder = ",str(c2.cal2()))
