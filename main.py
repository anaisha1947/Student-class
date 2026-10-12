#Write a program to create a class with the name Student 
# and perform the following tasks 
# 1. Declare a variable grade 
# 2. Print a sentence inside the class 
# 3. Create an object of class student and see the output
class students:
    grade = 98
    def display(self):
        print("Hello, I am a student. My grade is", self.grade)
s = students()
s.display()