# Peerlist Explore

## Introduction

🌟 **Peerlist** is an incredible platform for developers to showcase their projects. But what if you could search for any project you wanted?

Even better, imagine being able to find projects by simply describing what you need. Type naturally and discover the perfect projects effortlessly! 🚀✨

**ProjectFinder** is a powerful tool that does exactly that! 👀

## Features

- **Effortless Search:** Type in your requirements as if you're having a conversation, and get instant results.
- **Discover Projects:** Explore a wide range of projects with detailed descriptions, links, and upvotes.
- **Enhanced Interaction:** Dive deep into the details of each project and find exactly what you're looking for.

Say goodbye to endless scrolling and hello to smart, conversational searching! 🚀🔍

## Installation

To get started with ProjectFinder, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/AtharvaMaskar26/Peerlist-Explore.git
   ```

2. Navigate to Text2SQL Directory
    ```bash 
    cd Text2SQL
    ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add the scraped data to your database
```bash
cd scraping
python sql.py
```

4. Set up your environment variables by creating a .env file in the root directory of the project. Add your MySQL and GEMINI URLs in the following format:

    ```bash
    MYSQL_URL= MYSQL_URL
    GEMINI_URL= ENTER_GEMINI_API_KEY
    ```

5. Start the streamlit app:
   ```bash
   streamlit run app.py
   ```

6. Use the interactive search interface to find projects:
   - Enter your search requirements in natural language.
   - Browse through the results and explore detailed project information.

## Examples

### Example Search Queries

- "Show me the top projects from March 2024."
- "Suggest me some projects that would help me with design."
- "Suggest me top 5 projects built with Python."

### Example Output

```json
{
  "project_name": "Scattr",
  "description": "The Easiest Way to Spread Your Writing Across the Internet | Cross-posting tool",
  "link": "https://peerlist.io/codersalman/project/scattr",
  "number_of_upvotes": 106
}
```

## Contributing

We welcome contributions to Peerlist Explore! If you have suggestions for improvements or want to report a bug, please open an issue or submit a pull request.

## Contact

For any questions or feedback, please reach out to us at [atharvamaskar10@gmail.](mailto:atharvamaskar10@gmail.com).