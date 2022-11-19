class Width():
    Width = 0

class Height():
    Height = 0

class Length():
    Length = 0

class Pyramid():
    Length = 0
    Width = 0
    Height = 0

    def value(self):
        print("Pyramid Length = ",str(self.Length.Length))
        print("Pyramid Height = ", str(self.Height.Height))
        print("Pyramid Width = ", str(self.Width.Width))

    def cal(self):
        self.cal = (self.Length.Length) * (self.Width.Width) * (self.Height.Height) / 3
        return self.cal

Pyramid = Pyramid()
Length.Length = 10
Width.Width = 7
Height.Height = 17
Length = Length()
Width = Width()
Height = Height()
Pyramid.Length = Length
Pyramid.Width = Width
Pyramid.Height = Height
Pyramid.value()
print("Calculated Pyramid = ",'{:.2f}'.format(Pyramid.cal()))