class Person(object):
    def __init__(self, name):
        self.name = name

    def get_attributes(self):
        return self.name


class Student(Person):
    def __init__(self, name, course, year):
        Person.__init__(self, name)
        self.course = course
        self.year = year

    def get_details(self):
        return "%s is enrolled on %s course, and is in year %s."\
            % (self.name, self.course, self.year)


class Tutor(Person):
    def __init__(self, name, faculty, level):
        Person.__init__(self, name)
        self.faculty = faculty
        self.level = level

    def get_details(self):
        return "%s is a %s-level tutor in the %s department."\
            % (self.name, self.level, self.faculty)
