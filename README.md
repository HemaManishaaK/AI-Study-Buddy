# AI Study Buddy

A beginner-friendly Generative AI project built using Python, Streamlit, and the Gemini API.

## Features

- Explain any topic
- Generate short study notes
- Generate multiple-choice quizzes

## Technologies

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## Setup

1. Open the project folder in VS Code.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate it on Windows:

```bash
venv\Scripts\activate
```

4. Install the packages:

```bash
pip install -r requirements.txt
```

5. Create a file named `.env` and add:

```text
GEMINI_API_KEY=your_actual_api_key
```

6. Run the application:

```bash
python -m streamlit run app.py
```

## Important

Do not upload your `.env` file or API key to GitHub.
