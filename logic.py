"""
Course Number: ENGR 13300
Semester: Spring 2026

Description: 
    Has majority of the functions for creating an application that would allow users to select a country and learn a unique historical fact about that country. 

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
import pandas as pd
import streamlit as st

def get_country_fact(df, user_choice): #funtion is designed to get the country fact based on choice
    fact_result = "No historical fact found for this country."
    for index, row in df.iterrows():
        if str(row["Countries"]) == str(user_choice).strip():
            fact_result = row["Facts"]
            break
        elif user_choice == "":
            fact_result = "Please select a country"
    return fact_result

def validate_excel_data(df): #Function make sures the excel is valid. Collect the correct coloumn 
    required_col = ["Countries", "Facts"]
    for col in required_col:
        if col not in df.columns:
            return False, f"Missing column: {col}"
    return True, "Excel data is valid."

def calculate_rating_feedback(rating): #function that gives feedback based on the rating given by the user
    if rating >=4:
        return "Thank you for finding this fact interesting!"
    elif rating == 3:
        return "Thanks for the feedback!"
    else:
        return "Sorry to hear you didn't find this fact interesting."
    
def trigger_world_animation(user_choice): #function that triggers a pop up animation
    icons = ["🌍", "🌎", "🌏"]
    for i in range(3):
        selected_icon = icons[i % len(icons)]
        st.toast(f"Exploring {user_choice}", icon=selected_icon)