import requests
import json
import re
# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def getAssignmentInfo(auth_token: str, course: int):
    return_list = []
    headers = {'Authorization': f'Bearer {auth_token}'}
    url = 'https://umich-dev.instructure.com/api/v1/courses/' + str(course) + '/assignments'
    response = requests.get(url, headers=headers)
    print(response)
    reponse_obj = json.loads(response.content)
    for assignment in reponse_obj:
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

