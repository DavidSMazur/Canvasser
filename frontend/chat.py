import streamlit as st
import requests  # For making API requests

st.title("Canvassist")
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

choose=st.radio("select your course",("eecs281","mhack16","hist604"))

st.sidebar.markdown(
    """
    <style>
        .sidebar .success {
            display: flex;
            justify-content: center;
            text-align: center;
        }
    </style>
    """
, unsafe_allow_html=True)

st.sidebar.success("###  Submit or Chat")


def call_api(message):
    # Replace with your API endpoint URL
    api_url = "http://127.0.0.1:8000/v1/query"
    
    # Prepare the payload
    payload = {
        "course_id": "MHacks: Canvasser",
        "query_text": message
    }

    # Send the request to your API
    response = requests.post(api_url, json=payload)

    # Return the response text or handle errors
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error: Unable to fetch response"


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask away"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    api_response = call_api(prompt)
    with st.chat_message("assistant"):
        st.write(api_response)
    st.session_state.messages.append({"role": "assistant", "content": api_response})
