import requests
import json
import re

# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


def get_assignment_info(auth_token: str, course: int):
    return_list = []
    headers = {'Authorization': f'Bearer {auth_token}'}
    url = 'https://umich-dev.instructure.com/api/v1/courses/' + str(course) + '/assignments'
    response = requests.get(url, headers=headers)
    print(response)
    response_obj = json.loads(response.content)
    for assignment in response_obj:
        # print(assignment)
        assignment_dict = {}
        id = str(assignment.get('id'))
        assignment_dict['id'] = id
        description = cleanhtml(str(assignment.get('description'))).replace("\n", " ")
        assignment_dict['description'] = description
        due_date = str(assignment.get('due_at'))
        assignment_dict['due_at'] = due_date
        # try:
        #     rubric = assignment_dict.get('rubric')
        #     print(rubric)
        #     assignment_dict['rubric'] = rubric
        # except KeyError:
        #     pass
        return_list.append(assignment_dict)
    return return_list


def get_announcements(auth_token: str, course: int):
    return_list = []
    headers = {'Authorization': f'Bearer {auth_token}'}
    url = 'https://umich-dev.instructure.com/api/v1/announcements?context_codes[]=course_' + str(course)
    response = requests.get(url, headers=headers)
    print(response)
    response_obj = json.loads(response.content)
    for courses in response_obj:
        # print(courses)
        course_dict = {}
        id = str(courses.get('id'))
        course_dict['id'] = id
        title = str(courses.get('title'))
        course_dict['title'] = title
        message = cleanhtml(str(courses.get('message'))).replace("\n", " ")
        course_dict['description'] = message
        return_list.append(course_dict)
    return return_list


def get_courses(auth_token: str):
    return_list = []
    headers = {'Authorization': f'Bearer {auth_token}'}
    url = 'https://umich-dev.instructure.com/api/v1/courses?include[]=syllabus_body'
    response = requests.get(url, headers=headers)
    print(response)
    response_obj = json.loads(response.content)
    for courses in response_obj:
        # print(courses)
        course_dict = {}
        id = str(courses.get('id'))
        course_dict['course_id'] = id
        user_id = str(courses.get('enrollments')[0].get('user_id'))
        course_dict['user_id'] = user_id
        course_name = str(courses.get('name'))
        course_dict['course_name'] = course_name
        syllabus = cleanhtml(str(courses.get('syllabus_body'))).replace("\n", " ")
        course_dict['syllabus'] = syllabus
        return_list.append(course_dict)
    return return_list