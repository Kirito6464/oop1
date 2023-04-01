class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_rating = 0

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for k in self.grades:
            self.av_rating = sum(self.grades[k]) / len(self.grades[k])
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.av_rating}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, lecturer):
        return self.av_rating == lecturer.average_rating

    def __lt__(self, lecturer):
        return self.av_rating < lecturer.average_rating

    def __le__(self, lecturer):
        return self.av_rating <= lecturer.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rating = 0


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def __str__(self):
        for k in self.grades_lecturer:
            self.average_rating = sum(self.grades_lecturer[k]) / len(self.grades_lecturer[k])
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка: {round(self.average_rating, 1)}'

    def __eq__(self, student):
        return self.average_rating == student.av_rating

    def __lt__(self, student):
        return self.average_rating < student.av_rating

    def __le__(self, student):
        return self.average_rating <= student.av_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


some_lecturer1 = Lecturer('Some', 'Body')
some_lecturer1.courses_attached += ['Python']

some_student1 = Student('Roy', 'Eman', 'your_gender')
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Git']
some_student1.finished_courses += ['Введение в программирование']

some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 10)
some_student1.rate_hw(some_lecturer1, 'Python', 9)

some_reviewer1 = Reviewer('Some', 'Body')
some_reviewer1.courses_attached += ['Python']

some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 9)

some_lecturer2 = Lecturer('some', 'body')
some_lecturer2.courses_attached += ['Python']

some_student2 = Student('ruby', 'eman', 'your_gender')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += ['Введение в программирование']

some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 10)
some_student2.rate_hw(some_lecturer2, 'Python', 9)

some_reviewer2 = Reviewer('some', 'body')
some_reviewer2.courses_attached += ['Python']

some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 9)


def a_rating_st():
    for i in some_student1.grades:
        for k in some_student2.grades:
            if i == k:
                st = (sum(some_student1.grades[k]) + sum(some_student2.grades[k])) / \
                     (len(some_student1.grades[k]) + (len(some_student2.grades[k])))
                return st


def a_rating_le():
    for i in some_lecturer1.grades_lecturer:
        for k in some_lecturer2.grades_lecturer:
            if i == k:
                st = (sum(some_lecturer1.grades_lecturer[k]) + sum(some_lecturer2.grades_lecturer[k])) / \
                     (len(some_lecturer1.grades_lecturer[k]) + (len(some_lecturer2.grades_lecturer[k])))
                return st
