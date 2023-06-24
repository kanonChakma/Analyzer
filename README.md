# Analyzer

This is Sentiment Analysis web applicaitons that performs sentiment analysis on text using a pre-trained model("StatsGary/setfit-ft-sentinent-eval" model and tokenizer from the Transformers library). It predicts the sentiment of the provided text as either negative, neutral, or positive.

For testing i have used Google colaboratory which is an open source platform for machine learning or data science projects.

# Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/kanonChakma/Analyzer
    ```

2. Create a virtual environment (optional but recommended):

    ```shell
     python3 -m venv venv
     source venv/bin/activate
    ```

3. Install the required dependencies:

    ```shell
    pip install -r requirements/local.txt
    ```

4. Start the server:

    ```shell
    python manage.py runserver
    ```

# API Endpoint

-   **URL:** `api/analyze/`
-   **Method:** POST
-   **Request Body:**
-   `text` (string, required): The text to be analyzed for sentiment.
