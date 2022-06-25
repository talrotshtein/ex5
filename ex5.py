import json
import os



def names_of_registered_students(input_json_path, course_name):
    names = []
    with open(input_json_path, 'r') as file:
        source = json.load(file)
        for course_data in source.values():
            if course_name in course_data['registered_courses']:
                names.append(course_data['student_name'])
    return names





def enrollment_numbers(input_json_path, output_file_path):
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




def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass


