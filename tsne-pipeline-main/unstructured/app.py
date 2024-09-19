## pip install streamlit
## activate env: .venv\Scripts\activate.bat
## run app: streamlit run app.py
## need to be in WSL to run maybe? -- check up on this


import streamlit as st  # type: ignore
import pandas as pd  # type: ignore

st.write("Convert your document to text here!")

df = pd.DataFrame({
    'doc options': ['xml', 'pdf', 'html', 'heic']
    })

option = st.selectbox(
    'Which document type are you using?',
    df['doc options'])

'You selected: ', option 


#st.file_uploader("Upload your input file", type=["csv"], key="uploaded_file")
#iris = pd.read_table(st.session_state["uploaded_file"] , sep=",", header=0)


uploaded_files = st.file_uploader(
    "Choose a file", accept_multiple_files=True
)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)