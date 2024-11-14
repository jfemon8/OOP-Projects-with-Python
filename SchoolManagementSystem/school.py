class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
        
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
        
    def add_teacher(self, subject, teacher):
        self.teachers[teacher] = subject
        
    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)
    
    @staticmethod
    def calculate_grade(marks):
        if marks>=80:
            return 'A+'
        elif marks>=70:
            return 'A'
        elif marks>=60:
            return 'A-'
        elif marks>=50:
            return 'B'
        elif marks>=40:
            return 'C'
        elif marks>=33:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value==5.00:
            return 'A+'
        elif value>=4.00:
            return 'A'
        elif value>=3.50:
            return 'A-'
        elif value>=3.00:
            return 'B'
        elif value>=2.00:
            return 'C'
        elif value>=1.00:
            return 'D'
        else:
            return 'F'
    
    def __repr__(self):
        print('** All Classroom **')
        for key in self.classrooms.keys():
            print(key)
        
        print('\n** All Students **')
        result = ''
        for key, value in self.classrooms.items():
            result += f'{key.upper()} Class Student\n'
            for student in value.students:
                result += f'{student.name}\n'
        print(result)
        
        print('** All Subjects **')
        subject = ''
        for key, value in self.classrooms.items():
            subject += f'{key.upper()} Class Subjects\n'
            for sub in value.subjects:
                subject += f'{sub.name}\n'
        print(subject)
        
        print('** All Teachers **')
        for teacher, subject in self.teachers.items():
            print(f'{teacher.name} - {subject.name}')
            
        print('\n** All Students Result **')
        for key, value in self.classrooms.items():
            print(f'{key.upper()} Students Result: ')
            for student in value.students:
                for k, i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[k])
                student.final_grade()
                print(f'Overall Grade: {student.grade}\n')

        return ''

           