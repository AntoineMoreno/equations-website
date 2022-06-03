import streamlit as st
import requests
import numpy as np
import pandas as pd
from PIL import Image

from streamlit_drawable_canvas import st_canvas



'''
# Le site des équations 🥳
'''

st.markdown('''
*Submit your image and let the magic work ! 🪄*''')


'''
### Tired of typing this yourself ? ⬇️
'''




st.latex(r'''
    \sum_{k=0}^{n-1} ar^k =a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

with st.expander("equation"):
    st.write("\sum_{k=0}^{n-1} ar^k =a \left(\\frac{1-r^{n}}{1-r}\\right)")


'''
### Just charge your image here
'''

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a CSV file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image) # if you want to pass it to OpenCV
    st.image(image, caption="Your equation", width=400)


'''
______________________________________
'''

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')
     '''

        ## Once we have these, let's call our API in order to retrieve a prediction

        See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

        🤔 How could we call our API ? Off course... The `requests` package 💡


        2. Let's build a dictionary containing the parameters for our API...

        3. Let's call our API using the `requests` package...

        4. Let's retrieve the prediction from the **JSON** returned by the API...

        ## Finally, we can display the prediction to the user
'''







st.title("Drawable Canvas")
st.markdown("""
Draw on the canvas, get the image data back into Python !
* Doubleclick to remove the selected object when not in drawing mode
""")
st.sidebar.header("Configuration")



# Create a canvas component
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


# Do something interesting with the image data
if canvas_result is not None:
    st.image(canvas_result.image_data)

code_latex = ":)"
st.write("voici le code", code_latex)
