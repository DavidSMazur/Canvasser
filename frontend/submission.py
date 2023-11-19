import streamlit as st
from streamlit.logger import get_logger

st.header("File Submission")
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

choose=st.radio("Choose a Class to Submit for:",("eecs281","mhack16","hist604"))
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
# if uploaded_file is not None:
    # df = extract_data(uploaded_file)
