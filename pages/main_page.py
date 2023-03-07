import streamlit as st
from PIL import Image
import requests
from dotenv import load_dotenv
import os

# Set page tab display
st.set_page_config(
   page_title="Simple Image Uploader",
   page_icon= '🖼️',
   layout="wide",
   initial_sidebar_state="expanded",
)

# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
# url = 'http://localhost:8000'
load_dotenv()
url = os.getenv('API_URL')
url = 'http://localhost:8000'


# App title and description
st.header('Simple Image Uploader 📸')
st.markdown("---")

### Create a native Streamlit file upload input
st.markdown("### Let's do a tumor classification 👇")
img_file_buffer = st.file_uploader('Upload an image of an MRI')

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

  with col2:
    with st.spinner("Wait for it..."):
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()

      ### Make request to  API (stream=True to stream response as bytes)
    try:
        res = requests.post(url + "/upload_image", files={'img': img_bytes})
        if res.status_code == 200:
            ### Display the image returned by the API
            st.image(res.content, caption="Image returned from API ☝️")
        else:
            st.markdown("**Oops**, something went wrong 😓 Please try again.")
            print(res.status_code, res.content)        
    except:
        st.subheader('Error while communicating with API')

