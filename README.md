# News Streamlit App

This is a simple Streamlit application that fetches and displays news articles using the News API.

## Project Structure

```
news-streamlit-app
├── src
│   └── app.py          # Main application file for the Streamlit app
├── env
│   └── .env            # Environment variables (e.g., API keys)
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd news-streamlit-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source env/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   - Create a `.env` file in the `env` directory and add your News API key:
     ```
     API_KEY=your_api_key_here
     ```

6. **Run the Streamlit app:**
   ```
   streamlit run src/app.py
   ```

## Usage

Once the app is running, you can view it in your web browser at [http://localhost:8501](http://localhost:8501).

- Use the sidebar to select a country, category, and optionally enter a keyword.
- Click **Get News** to fetch and display the latest news articles.
- Each article shows the title, description, image (if available), and a link to read more.

## Notes

- You need a valid [NewsAPI](https://newsapi.org/) API key.
- The `.env` file should use `API_KEY` as the variable name