import json
import os



def names_of_registered_students(input_json_path, course_name):
    names = []
    with open(input_json_path, 'r') as file:
        source = json.load(file)
    for i in source:
        if course_name in ['registered_courses']:
            names += ['student_name']
    return names





def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    pass



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass

names_of_registered_students("semesters_databases/2022a.json", "asd")

