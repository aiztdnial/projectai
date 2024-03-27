import os
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import Image
import streamlit as st
from StoryMethods import StoryMethods as sm

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def main():
    
    # Streamlit app layout
    st.title('Outfit Idea Generator For Men')

    # User input for story generation
    user_prompt = st.text_area('Provide your face shape and hair length. Then provide the occasion that you need to go:')

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
        
    if st.button('Generate:'):
        
        story =sm.story_ai(user_prompt,client)
        design =sm.design_ai(story,client)
        uploaded_files =sm.cover_ai(design,client)
        
        st.image(uploaded_files, caption='Style Example', use_column_width=True)
        
        st.write('Generated Image Prompt:')
        st.write(design)
        
        st.divider()
        
        st.write('Advised:')
        st.write(story)


if __name__=="__main__":
    main()