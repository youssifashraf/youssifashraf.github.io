# import streamlit as st
# st.set_page_config(
#     page_title="Eye tracking System",
#     page_icon="👀",
#     layout="wide",
#     initial_sidebar_state="expanded",
  
# )
# st.title("Hello…")
# st.text("""
# This page responisble for eye tracking system
# implemented by ENG.Youssif Ashraf
# """)

# st.button('Say hello')

from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")

import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)


# import streamlit as st
# import cv2
# import numpy as np
# import requests

# st.title( 'Mobile Camera Preview in Streamlit' )
# frame_window = st.image( [] )
# take_picture_button = st.button( 'Take Picture' )

# while True:
#     # Request the image from the server
#     response = requests.get(url="http://192.168.1.6:4747/video")
#     imgNp = np.array(bytearray(response.content), dtype=np.uint8)
#     frame = cv2.imdecode(imgNp, cv2.IMREAD_UNCHANGED )
#     # As OpenCV decodes images in BGR format, we'd convert it to the RGB format
#     frame = cv2.cvtColor( frame , cv2.COLOR_BGR2RGB )

#     frame_window.image(frame)

#     if take_picture_button:
#         # Pass the frame to a model
#         # And show the output here...
#         break



# import streamlit as st
# import cv2
# import pandas as pd
# import numpy as np

# vid = cv2.VideoCapture(0)
# st.set_page_config(
#     page_title="Eye tracking System",
#     page_icon="👀"
#     # layout="wide",
#     # initial_sidebar_state="expanded",
  
# )
# st.title( 'Eye tracking System' )
# frame_window = st.image( [] )
# #take_picture_button = st.button( 'Take Picture' )
# first_time=True


# chart_data = pd.DataFrame(
#     [1,0,0,1,1,1,1,1],
#     columns=['eye contact'])

# st.line_chart(chart_data)

# while True:
#     got_frame , frame = vid.read()
    
#     if got_frame:
#         frame = cv2.cvtColor( frame , cv2.COLOR_BGR2RGB )
#         frame=cv2.rectangle(frame,(50,50),(100,100),(224,0,0),1)
#         frame_window.image(frame)
#     elif first_time :
#         st.text("""
#             check your camera app 
#             or if there are another user online...
#             """)
#         first_time=False

#     # if take_picture_button:
#     #     # Pass the frame to a model
#     #     # And show the output here...
#     #     break

# vid.release()

