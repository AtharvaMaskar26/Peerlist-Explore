from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv() # Load all env variables


new_prompt = """
You are an expert English to SQL Query converter! You will be asked an english question and have to have to respond with an SQL Query that would be useful to fetch required data. \n\n

The SQL Schema Looks something like this: \n
Database name: Projects\n
Columns: \n
link (VARCHAR) \n
monthly_rank (INT) \n
project_name (VARCHAR) \n
project_subheading (VARCHAR) \n
description (VARCHAR)\n
year (INT)\n
month (VARCHAR) ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] \n
number_of_upvotes (INT) \n

Here are some Examples:  \n
\n
Example 1: \n
Question: Which project has the most number of upvotes?\n
Response: SELECT project_name, description, link, number_of_upvotes FROM Projects ORDER BY number_of_upvotes DESC LIMIT 1;\n

Example 2:\n
Question 2: Give me top 3 projects built with typescript\n
Response: SELECT project_name, description, link, number_of_upvotes FROM Projects WHERE description LIKE '%Typescript%' ORDER BY number_of_upvotes DESC LIMIT 3;\n

Example 3: \n
Question 3: 
Response: SELECT project_name, description, link, number_of_upvotes FROM Projects WHERE month = 'Aug' AND year = 2023 ORDER BY number_of_upvotes DESC LIMIT 10;


No matter what the user asks for always retrun the project_name, description, link and number_of_upvotes.
NOTE: also the sql code should not have ``` in beginning or end and sql word in output. 

"""

prompt = """You are an expert in converting English questions to SQL query!
    The SQL database has the name Projects and has the following schema:
      The SQL Schema Looks something like this: \n
Database name: Projects\n
Columns:     link TEXT,
    monthly_rank BIGINT,
    project_name TEXT,
    project_subheading TEXT,
    description TEXT,
    month TEXT,
    year BIGINT,
    number_of_upvotes BIGINT, number_of_upvotes (INT)
        
          
For example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM Projects;

    \n Example 2 - Give me top 3 projects built with typescript
    Response: SELECT project_name, description, link, number_of_upvotes FROM Projects WHERE description LIKE '%Typescript%' ORDER BY number_of_upvotes DESC LIMIT 3;

    No matter what the user asks for always retrun the project_name, description, link and number_of_upvotes.
    also the sql code should not have ``` in beginning or end and sql word in output. 
"""

prompt_for_single_values = """
You are an expert communicator. You will be asked a question and given an answer. You have to write the answer so that the human understands it. Also write in first person if needed.   
"""

import streamlit as st
import os 
import sqlite3
import google.generativeai as genai

# Configure API key 
api_key = os.environ['GEMINI_API_KEY']
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SQL_URL = os.getenv('MYSQL_URL')
engine = create_engine(SQL_URL)
connection = engine.connect()

# Function to provide SQL query 
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])


    return response.text

def clean_string(str):
   return str.replace('\n', ' ')

# Function to retrieve data from SQL database
def read_sql_query(query):
    # Execute the query
    result = connection.execute(query)

    # Fetch all rows from the result
    rows = result.fetchall()

    return rows

with st.form('my-form'):
    

    question = st.text_input("Ask?")

    submitted = st.form_submit_button("Submit")
    if submitted:
        query = get_gemini_response(question, new_prompt)
        print(query)

        query = clean_string(query)
        response = read_sql_query(text(query))

        print(len(response[0]), response[0])
        # prompt += f"Question: {question}\n Response: {response}\n"
        if len(response[0]) == 4:
            projects = []

            for i, project in enumerate(response):
                project_name = response[i][0]
                description = response[i][1]
                link = response[i][2] 
                number_of_upvotes = response[i][3]

                project = {
                    "project_name": project_name, 
                    "description": description, 
                    "link": link, 
                    "number_of_upvotes": number_of_upvotes
                }

                projects.append(project)

            print("Project Length", len(projects))
            for project in projects: 
                with st.expander(f"{project['project_name']} ({project['number_of_upvotes']} upvotes)"):
                    st.write(f"Project Name: {project['project_name']}")
                    st.write(f"Description: {project['description']}")
                    st.write(f"Check out the project: {project['link']}")
        else:
            question_answer = f"Question: {question}\n Answer: {response}"
            reply = get_gemini_response(prompt_for_single_values, question_answer)
            st.write(reply)