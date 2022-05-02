from statistics import mean

def get_average(grades):
    average = 0
    len = 0
    for key, value in grades.items():
        average += mean(value)
        len += 1
    if len == 0:
        average = 0
    else:
        average = average / len
    return average

student_list = []
lecturer_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lc(self, lecturer, course, grade): # функция выставления оценки лекторам
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self):
        res = f'''Имя : {self.name} 
        Фамилия : {self.surname} 
        Средняя оценка за домашнее задание : {get_average(self.grades):.2f} 
        Курсы в процессе обучения: {','.join(self.courses_in_progress)}
        Завершенные курсы: {','.join(self.finished_courses)}'''
        return res

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Этот человек самозванец')
            return
        return get_average(self.grades) < get_average(other.grades)



class Mentor:
    def __init__(self, name, surname):
        self.courses_attached = []
        self.name = name
        self.surname = surname



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = None
        self.courses_attached = []
        self.grades = {}



    def __str__(self):
        res = f'Имя : {self.name} \n Фамилия : {self.surname} \n Средняя оценка за лекцию : {get_average(self.grades):.2f}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Этот человек самозванец')
            return
        return get_average(self.grades) < get_average(other.grades)



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade): # функция оценивания студентов
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя : {self.name} \n Фамилия : {self.surname}'
        return res

def average_for_course(students, course):
    av_for_course = 0
    len = 0
    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            av_for_course += mean(student.grades[course])
            len += 1
    if len == 0:
        av_for_course = 0
    else:
        av_for_course = av_for_course / len
    return av_for_course

def average_for_lecturer(lecturers, course):
    av_for_course = 0
    len = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            av_for_course += mean(lecturer.grades[course])
            len += 1
    if len == 0:
        av_for_course = 0
    else:
        av_for_course = av_for_course / len
    return av_for_course




best_student_one = Student('Ruoy', 'Eman', 'your_gender')
best_student_one.courses_in_progress.append('Python')
best_student_one.courses_in_progress.append('GIT')
best_student_one.finished_courses.append('Введение в программировыание')

best_student_two = Student('Ivan', 'Dulin', 'your_gender')
best_student_two.courses_in_progress.append('Python')
best_student_two.courses_in_progress.append('GIT')
best_student_two.finished_courses.append('Введение в программировыание')

cool_lecturer_one = Lecturer('Zurab', 'Zurabov' )
cool_lecturer_one.courses_attached.append('Python')
cool_lecturer_two = Lecturer('Islambek', 'Islambekov' )
cool_lecturer_two.courses_attached.append('Python')

best_student_one.rate_lc(cool_lecturer_one, 'Python', 9)
best_student_two.rate_lc(cool_lecturer_one, 'Python', 7)
best_student_one.rate_lc(cool_lecturer_two, 'Python', 8)
best_student_two.rate_lc(cool_lecturer_two, 'Python', 8)

cool_reviewer_one = Reviewer('Abut', 'Abut-ogli')
cool_reviewer_two = Reviewer('Nazran', 'Nazranov')
cool_reviewer_one.rate_hw(best_student_one, 'Python', 6)
cool_reviewer_one.rate_hw(best_student_two, 'Python', 9)
cool_reviewer_two.rate_hw(best_student_one, 'Python', 7)
cool_reviewer_two.rate_hw(best_student_two, 'Python', 7)

student_list += [best_student_one]
student_list += [best_student_two]
lecturer_list += [cool_lecturer_one]
lecturer_list += [cool_lecturer_two]

print(f'Средняя оценка студентов за курс Python: {average_for_course(student_list,"Python"):.2f}')
print(f'Средняя оценка лекторов за курс Python: {average_for_lecturer(lecturer_list, "Python"):.2f}')

print(f'{best_student_one} \n')
print(f'{best_student_two} \n')
print(f'{cool_lecturer_one} \n')
print(f'{cool_lecturer_two} \n')
print(f'{cool_reviewer_one} \n')
print(f'{cool_reviewer_two} \n')
print(best_student_two < best_student_one)
print(cool_lecturer_one < cool_lecturer_two)


