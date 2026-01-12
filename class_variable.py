class student:
    school="ABC Public school"
    def __init__(self,name):
        self.name=name
s1=student("Rach")
s2=student("Lavu")
print(s1.school)
print(s2.school)
student.school="XYZ High school"
print(s1.school)
print(s2.school)
