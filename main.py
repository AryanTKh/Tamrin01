import re


class User:
    def __init__(self, type, id, name, password):
        self.type = type
        self.id = id
        self.name = name
        self.password = password
        self.courses = []


class Course:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.students = 0


courses = []
users = []
current_student = None


def print_courses():
    print('course list:')
    for course in courses:
        print(f'{course.id} {course.name} {course.students}/{course.capacity}')


def student_menu(student):
    print('entered student menu')

    while True:
        c = input().strip()
        p = c.split()

        if re.match(r'^edu get course -i .+ edu$', c):
            ix = p.index('-i')
            id = ' '.join(p[ix + 1: len(p) - 1])

            course = [course for course in courses if str(course.id) == id]

            if course:
                if id in student.courses:
                    print('you already have this course')
                else:
                    course = course[0]
                    if course.students == course.capacity:
                        print('course is full')
                    else:
                        student.courses.append(id)
                        course.students += 1
                        print('course added successfully!')
            else:
                print('incorrect course id')

        elif c == 'edu show course list edu':
            print_courses()

        elif c == 'edu log out edu':
            print('logged out successfully!')
            print('entered log in/sign up menu')
            break

        elif c == 'edu current menu edu':
            print('student menu')

        elif c == 'edu exit edu':
            exit(0)

        else:
            print('invalid command')


def professor_menu():
    print('entered professor menu')

    while True:
        c = input().strip()
        p = c.split()

        if re.match(r'^edu add course -c .+ -i .+ -n .+ edu$', c):
            ix = p.index('-i')
            nx = p.index('-n')

            name = ' '.join(p[4:ix])
            id = ' '.join(p[ix + 1: nx])
            capacity = ' '.join(p[nx + 1: len(p) - 1])

            if name.count(' '):
                print('invalid course name')
            else:
                if not id.isdigit():
                    print('invalid course id')
                else:
                    if not capacity.isdigit():
                        print('invalid course capacity')
                    else:
                        id = int(id)
                        capacity = int(capacity)
                        if [course for course in courses if course.id == id]:
                            print('course id already exists')
                        else:
                            course = Course(id, name, capacity)
                            courses.append(course)
                            print('course added successfully!')

        elif c == 'edu show course list edu':
            print_courses()

        elif c == 'edu log out edu':
            print('logged out successfully!')
            print('entered log in/sign up menu')
            break

        elif c == 'edu current menu edu':
            print('professor menu')

        elif c == 'edu exit edu':
            exit(0)

        else:
            print('invalid command')


def is_valid_password(password):
    if len(password) < 4:
        return False

    a = password.count('*')
    b = password.count('.')
    c = password.count('!')
    d = password.count('@')
    e = password.count('$')
    f = password.count('%')
    g = password.count('^')
    h = password.count('&')
    i = password.count('(')
    j = password.count(')')

    return sum([a, b, c, d, e, f, g, h, i, j]) != 0


def login_signup_menu():
    while True:
        c = input().strip()
        p = c.split()

        if c == 'edu current menu edu':
            print('log in/sign up menu')

        elif c == 'edu exit edu':
            exit(0)

        elif re.match(r'^edu sign up -.+ -i .+ -n .+ -p .+ edu$', c):
            ix = p.index('-i')
            nx = p.index('-n')
            px = p.index('-p')

            tpe = ' '.join(p[3:ix])[1:]

            if tpe not in ['S', 'P']:
                print('invalid type')
            else:
                id = ' '.join(p[ix + 1: nx])

                if not id.isdigit():
                    print('invalid id')
                else:
                    name = ' '.join(p[nx + 1: px])

                    if name.count(' '):
                        print('invalid name')
                    else:
                        password = ' '.join(p[px + 1: len(p) - 1])

                        if not is_valid_password(password):
                            print('invalid password')
                        else:
                            user = [user for user in users if user.id == id]

                            if user:
                                print('id already exists')
                            else:
                                user = User(tpe, id, name, password)
                                users.append(user)
                                print('signed up successfully!')

        elif re.match(r'^edu log in -i .+ -p .+ edu$', c):
            ix = p.index('-i')
            px = p.index('-p')

            id = ' '.join(p[ix + 1: px])
            password = ' '.join(p[px + 1: len(p) - 1])

            user = [user for user in users if str(user.id) == id]

            if user:
                user = user[0]
                if user.password == password:
                    print('logged in successfully!')
                    if user.type == 'S':
                        student_menu(user)
                    else:
                        professor_menu()
                else:
                    print('incorrect password')
            else:
                print('incorrect id')

        else:
            print('invalid command')


def main():
    login_signup_menu()


if __name__ == "__main__":
    main()
