import streamlit as st
import requests
import numpy as np
import pandas as pd
from PIL import Image
import cv2
from io import BytesIO


from streamlit_drawable_canvas import st_canvas



'''
# Easy LaTeX ✨
'''

st.markdown('''
*Submit your image and let the magic work ! 🪄*''')


'''
### Tired of typing this yourself ? ⬇️
'''




st.latex(r'''
    \sum_{k=0}^{n-1} ar^k =a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

with st.expander("LaTeX code ✨"):
    st.write("\sum_{k=0}^{n-1} ar^k =a \left(\\frac{1-r^{n}}{1-r}\\right)")

'''
______________________________________
'''
'''
## ⚠️ Just charge your image here...
'''

st.set_option('deprecation.showfileUploaderEncoding', False)
################################
# avec l'image uploadee
################################
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg"])
print(f'type uploaded file:{type(uploaded_file)}')
if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    print(f'type uploaded file :{type(uploaded_file.getvalue())}' )
    image_api_url = "http://127.0.0.1:8000/equations"
    response = requests.post(image_api_url, files=files)
    if response.status_code == 200:
        a=str(response.json()['code LaTeX'])
        st.write("Your LaTeX code:", a)
        st.latex(a)
    else:
        st.write("error:", response.status_code)

    image = Image.open(uploaded_file)
    img_array = np.array(image) # if you want to pass it to OpenCV
    st.image(image, caption="Your image", width=90)

#st.latex(r'''
    #\sum_{k=0}^{n-1} ar^k =a \left(\frac{1-r^{n}}{1-r}\right)
   # ''')

'''
______________________________________
## ...or draw your equation ✍🏻!
'''
#st.markdown(""" """)
#st.sidebar.header("Configuration")

################################
# avec le canva
################################

canvas_result = st_canvas(
    fill_color='rgba(0, 0, 0, 0.3)',
    stroke_width=3,
    stroke_color='#000000',
    background_color='rgba(255, 255, 255, 0.3)',
    background_image=None,
    update_streamlit=True,
    height=150,
    drawing_mode='freedraw',
    point_display_radius=2,
    key='canvas',)



if canvas_result is not None:
    #st.image(canvas_result.image_data)
    print(f'image_data type :{type(canvas_result.image_data)}')

#    cv2.imwrite(f"img.jpg",  canvas_result.image_data)
#   print(canvas_result.image_data)

    if canvas_result.image_data is not None:
        cv2.imwrite(f"img.jpg",  canvas_result.image_data)
        print("done")
        with open("img.jpg", 'rb') as fh:
            file = BytesIO(fh.read())
            print(f'image file type :{type(file)}')

    else:
        st.write("no image to save")



    # with open("img.jpg", "rb") as f:
    #     im_bytes = f.read()
    # im_b64 = base64.b64encode(im_bytes).decode("utf8")
    # file = json.dumps({"image": im_b64})
    print("done2")

    files = {"file": file}
    image_api_url = "https://image-equations-xp2pvcl2vq-ew.a.run.app/equations"
    response = requests.post(image_api_url, files=files)
    print("done3")
    if response.status_code == 200:
       a=str(response.json()['code LaTeX'])
       st.write("**Your LaTeX code:**",a)
       st.latex(a)
    else:
       st.write("error:", response.status_code)


st.latex("\\infty")
