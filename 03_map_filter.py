informacion = {
    'students': [
        {
            'name': 'Galileo Guzman',
            'age': 31,
            'hobbies': ['music', 'movies', 'biking', 'read', 'books']
        },
        {
            'name': 'Omar Flores',
            'age': 18,
            'hobbies': ['troba', 'movies', 'biking', 'read', 'books']
        },
        {
            'name': 'Armando',
            'age': 18,
            'hobbies': ['music', 'read', 'books']
        },
        {
            'name': 'Eduardo',
            'age': 18,
            'hobbies': ['music', 'read', 'books']
        },
    ],
    'last_update': '2021-02-27',
    'modified_by': 'frasgado@mail.io'
}

print(type(informacion))
print(type(informacion['students']))
print(type(informacion['last_update']))
print(type(informacion['modified_by']))

def hobbies_counter(student):
    total_hobbies = len(student['hobbies'])
    student['hobbies_counts'] = total_hobbies
    return student

students_with_hobbies = list(map(hobbies_counter, informacion['students']))
print(students_with_hobbies)

def students_with_more_than_three_hobbies(student):
    return student['hobbies_counts'] > 3

total_students_with_more_than_three_hobbies = list(filter(students_with_more_than_three_hobbies, students_with_hobbies))
print(total_students_with_more_than_three_hobbies)
