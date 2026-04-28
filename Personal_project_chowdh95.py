"""
Course Number: ENGR 13300
Semester: Spring 2026

Description: 
    Creating an application that would allow users to select a country and learn a unique historical fact about that country. 

Assignment Information:
    Assignment:     Personal Project
    Team ID:        001 - 20 
    Author:         Sreisti Chowdhury, chowdh95@purdue.edu
                    
    Date:           04/27/2026

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
import streamlit as st
import pandas as pd
import logic
import base64

# python -m streamlit run Personal_project_chowdh95.py
#The above is used for running the app on the terminal 

theme = st.sidebar.selectbox("Choose a Theme", ["Normal","UN Blue", "Purdue"]) #the 3 themes accessible to the user
if theme == "UN Blue":
    bg ="#009EDB"
    text = "black"
elif theme == "Purdue":
    bg = "#ceb888"
    text = "black"
elif theme == "Normal":
    bg = "#B8B284"
    text = "black"

st.markdown(f""" 
        <style>
    .stApp {{
        background-color: {bg};
        color: {text};
        transition: 0.5s; 
    }}
   
    h1, h2, h3, [data-testid="stSidebar"] {{
        color: {text} !important;
    }}
  
    .stAlert {{
        background-color: {bg};
        border: 1px solid "black";
    }}
    </style>
    """, unsafe_allow_html=True)

def add_custom_icon(image_file): #function that focuses on adding the custom icon I designed for the app 
    with open(image_file, "rb") as img:
        img_data = img.read()
        data = base64.b64encode(img_data).decode("utf-8")
        st.markdown(
            f"""
            <style>
            .foot-icon{{
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 20px;
                height: 20px;
            }}
            </style>
            <img src="data:image/png;base64,{data}" class="footer-icon">
        """,
            unsafe_allow_html=True
        )

st.set_page_config(page_title="UN Country History Facts", page_icon="🌍") 
st.title("UN Country History Facts Explorer 🌍") #creates the title of the app
st.markdown("Select a country to discover a unique history fact!") #Instructions
add_custom_icon("Icon.png") #icon that I designed 
with st.sidebar.expander("About this App"): #explores all the information put in the side bar about the app and the developer
    st.write("""
             This project was developed for ENGR 13300.
             It uses Streamlit to create an interactive web, 
             The app uses a Excel database created by me (Sreisti) and a lot of Google searching.
             The Excel file contains 193 UN Member States and a unique historical fact about each country.
             The User is able to select what country they want to explore and afterwards rate the fact out of 5 stars.
             The User can also select from 3 different themes to customize the look of the app.
             The main goal of the project is to provide accessible historical information through a web interface.
             The reason this project was created was because I have an interest in history.
             Hence I wanted to combine my STEM skills with my interest in history to create this project.
             """)
st.sidebar.markdown("---")
st.sidebar.markdown("Created by Sreisti Chowdhury")
st.sidebar.write(f"Total Countries: 193")
st.sidebar.markdown("---")
st.sidebar.subheader("Connect with the Developer")
st.sidebar.markdown("[GitHub](https://github.com/Sreisti)")
st.sidebar.markdown("[LinkedIn](www.linkedin.com/in/sreisti-chowdhury)")

try: #the main function of the app that runs the app and calls all the functions in logic.py to make the app work as intended. It also has error handling for if the excel file is not found or if there is an unexpected error.
    df = pd.read_excel("countries.xlsx") 
    is_valid, message = logic.validate_excel_data(df)
    if is_valid:
        st.subheader("Discover Historical Facts")
        user_choice = st.selectbox("Choose a country:", df["Countries"].tolist())
        if st.button("Reveal Fact"):
            fact = logic.get_country_fact(df, user_choice)
            logic.trigger_world_animation(user_choice)
            st.info(f"Historical Fact for {user_choice}: {fact}")
            st.toast("New History Knowledge Unlocked!", icon="🌍")
            st.markdown("---")
            st.subheader("Rate this Fact")
            user_rating = st.feedback("stars")

            if user_rating is not None:
                stars = user_rating + 1
                feedback_msg = logic.calculate_rating_feedback(stars)
                st.write(f"You rated this {stars} stars.")
                st.success(feedback_msg)
            else:
                st.error(f"Data Error: {message}")

except FileNotFoundError:
    st.error("Error: 'countries.xlsx' file not found. Please ensure the file is in the correct location.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")