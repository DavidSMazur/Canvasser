import streamlit as st
from streamlit.logger import get_logger
import requests
import json

import dotenv
import os

dotenv.load_dotenv()

st.header("File Submission")
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

course_list = {}

auth_token = os.getenv('CANVAS_AUTH')
headers = {'Authorization': f'Bearer {auth_token}'}
url = 'http://127.0.0.1:8000/v1/display/'
response = requests.post(url, headers=headers)
response = json.loads(response.content)
for course in response:
    course_id = course.get('course_id')
    print(course_id)
    course_list[course_id] = course.get('course_name')

choose=st.radio("Choose a Class to Submit for:",(course_list.values()))
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    assignment_ids = []
    auth_token = os.getenv('CANVAS_AUTH')
    headers = {'Authorization': f'Bearer {auth_token}'}
    course_id = list(course_list.keys())[list(course_list.values()).index(choose)]
    print("Selected course", course_id)

    # url = 'http://127.0.0.1:8000/v1/display/'
    # response = requests.post(url, headers=headers)
    # response = json.loads(response.content)
    # for course in response:
    # course_id = course.get('course_id')
    print(course_id)
    url = 'http://127.0.0.1:8000/v1/assignments/'
    data = {'course': course_id}
    assignment_list = requests.post(url, json=data, headers=headers)
    assignment_list = json.loads(assignment_list.content)
    # print(assignment_list)
    for assignment in assignment_list:
        assignment_ids.append(assignment.get('id'))
        st.markdown("**" + assignment.get('name') + "**")
        st.markdown("- Due At: " + assignment.get('due_at'))
        st.markdown("- " + assignment.get('description'))
        st.divider()
    assignment_choice = st.radio("Choose an Assignment to Submit for:", (assignment_ids))
    if st.button('Submit'):
        url = "http://127.0.0.1:8000/v1/uploadfile/"
        # file_bytes = uploaded_file.getvalue()
        r = requests.post(url, files={"file": uploaded_file})
        r = json.loads(r.content)
        file_location = r.get('file_location')
        url = "http://127.0.0.1:8000/v1/submit/"
        data = {"file_path": file_location, "course_id": course_id, "assignment_id": assignment_choice}
        r = requests.post(url, json=data, headers=headers)
        if (r.status_code == 200):
            print(r.text)
            success_message = 'Submitted successfully at: ' + r.text
            st.success(success_message, icon="✅")
        else:
            st.error('We hit an error ):', icon="🚨")


