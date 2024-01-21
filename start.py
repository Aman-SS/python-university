# python university
class University:
    def __init__(self, name, started):
        self.name = name
        self.started = started

U1 = University("Python University", "21-01-2024");
print("=> University Name: "+U1.name)
print("=> Starting Date: "+U1.started,)
print(end="\n")

# university courses
class CoursesList:
    def __init__(self, courses):
        self.courses = courses

CL = CoursesList(courses=["1. Python Programming", "2. Data Structure and Algorithm in Python"])
print("=> Courses")
for course in CL.courses:
    print(course)
print(end="\n")

# mentors
class MentorsList:
    def __init__(self, mentors):
        self.mentors = mentors

ML = MentorsList(mentors=["1. Aman Shankar Singh", "2. Dev Aman"])
print("=> Mentors")
for mentor in ML.mentors:
    print(mentor)
print(end="\n")