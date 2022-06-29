import json
import os



def names_of_registered_students(input_json_path, course_name):
    names = []
    with open(input_json_path, 'r') as file:
        source = json.load(file)
    for student in source.values():
        if course_name in student['registered_courses']:
            names.append(student['student_name'])
    return names



def enrollment_numbers(input_json_path, output_file_path):
    courses = {}
    with open(input_json_path, 'r') as file:
        source = json.load(file)
    dest = open(output_file_path, 'w')
    for student in source.values():
        for course in student['registered_courses']:
            if course not in courses:
                courses[course] = len(names_of_registered_students(input_json_path, course))
    sorted_courses = sorted(courses.keys())
    for course in sorted_courses:
        dest.write('"%s" %s\n' % (course, courses[course]))
    dest.close()



    """
    num_of_students = 0
    course_names = []
    with open(input_json_path, 'r') as file:
        source = json.load(file)
    for course_data in source.values():
        for course_data['registered_courses'] in course_data:
             if course_data['registered_courses'] != course_names: #not sure about that
                course_names.append(course_data['registered_courses'])#not sure about that
                sorted(course_names)
                with open(output_file_path, 'w') as wfile:
                    """


def courses_for_lecturers(json_directory_path, output_json_path):
    lecturers_dict = {}
    files = os.listdir(json_directory_path)
    for semester in files:
        if semester[-1:-6:] != ".json":
            continue
        with open(semester, 'r') as file_2:
            source = json.load(file_2)
        for course_id in source.values:
            for lecturer in course_id['lecturers']:
                if lecturer not in lecturers_dict:
                    lecturers_dict[lecturer] = course_id['course_name']
                else:
                    if course_id['course_name'] not in lecturers_dict[lecturer]:
                        lecturers_dict[lecturer] += course_id['course_name']
    with open('myfile.json', 'w') as file_3:
         json.dump(lecturers_dict, file_3, indent= 4)




