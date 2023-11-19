# https://canvas.instructure.com/doc/api/file.file_uploads.html#method.file_uploads.post
import requests
import json


def submit_file(token: str, file_path: str, course_id: str, assignment_id: str):
    # Step 1
    url = 'https://umich-dev.instructure.com/api/v1/users/self/files'
    params = {"name": file_path, "parent_folder_path": "my_files"}
    headers = {'Authorization': f'Bearer {token}'}
    files = {
        'file': (file_path, open(file_path, 'rb')),
    }
    x = requests.post(url, headers=headers, params=params)
    # Step 2
    json_x = json.loads(x.text)
    # print(json_x)
    url = json_x.get("upload_url")
    x = requests.post(url, files=files)
    # Upload to Assignment
    json_x = json.loads(x.text)
    # print(json_x)
    file_id = json_x.get("id")
    url = 'https://umich-dev.instructure.com/api/v1/courses/' + course_id + '/assignments/' + assignment_id + '/submissions'
    params = {"submission[submission_type]": "online_upload", "submission[file_ids][]": file_id}
    x = requests.post(url, headers=headers, params=params)
    json_x = json.loads(x.text)
    # print(json_x)
    return json_x.get("submitted_at")


# auth_token = ''
# print(submit_file(auth_token, "empty_property.pdf", "309", "4554"))
