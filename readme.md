# Scrabble Trainer Chatbot

Welcome to the Scrabble Trainer Chatbot! This app is designed to help users prepare for your Scrabble matches by transforming your sentences into fun, resampled versions. Each word in your sentence is replaced by another word that starts with the same letter and is of the same length. The twist? The replacements are random, so you get a different result each time!

<video width="600" controls>
  <source src="data/video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Watch the video to see the app in action:
`data/video.mp4`

## How It Works

### The Main Functions

Let's break down the core functions that make this magic happen:

1. **retrieve_word_list()**: This function reads a list of English words from a file and cleans it up by converting all words to lowercase. This word list is the pool from which I draw replacements.

2. **test_input_validity()**: Basic check to test that their are no digits in the sentence that the user submitted.

2. **resample_word(word_list, input_word)**: This function takes an input word and resamples it from the word list. It filters words that start with the same letter and have the same length as the input word. If no matching word is found, it returns the original word. Otherwise, it randomly selects a word from the filtered list. To ensure that the response is speedy, `python's` list comprehension syntax is used.

3. **split_input_sentence(input_sentence)**: This function splits the input sentence into individual words based on spaces.

4. **resample_sentence(input_sentence, word_list)**: This function resamples each word in the input sentence using the `resample_word` function and joins the resampled words back into a sentence.

### The Streamlit App

Streamlit is a powerful tool that allows us to create interactive web applications with ease. This code can be run without the streamlit app, but it's a lot more user friendly to have a minimal front-end to interact with. Here’s how the Scrabble Trainer Chatbot is set up using Streamlit:

1. **Title**: Start by setting the title of the app using `st.title("Scrabble Trainer Chatbot")`.

2. **Load the Word List**: The word list is loaded once when the app starts using `retrieve_word_list()`.

3. **Chat History**: Use `st.session_state` to keep track of the chat history, so you can see the conversation flow.

4. **User Input**: The user inputs their sentence in a text input field. When the "Send" button is pressed, the input sentence is resampled, and both the original and resampled sentences are added to the chat history.

5. **Display Chat History**: The chat history is displayed, differentiating between user inputs and bot responses.

## Limitations & Improvements

1. Some of the words in the provided data are not **recognizable english words** (to me). This list should be refined before being used for Scrabble. Refining the set of words to recognizable english words was not a requirement specified in the assignment.
2. More data quality tests should be incorporated for the solution to be used as a scrabble assistant. For example, in the current state non-compliant Scrabble words may be submitted by the user (contractions, propper nouns etc.). 

## Setup

To get started with the Scrabble Trainer Chatbot, you'll need to set up your environment using Poetry. Poetry is a tool for dependency management and packaging in Python. Here's how to install Poetry and set up the environment using the provided `pyproject.toml` file in the repository.

**Thsese scripts have only been tested with python 3.11.1 and Windows.**

### Install Poetry

1. **Install Poetry**: Open your terminal (Command Prompt or PowerShell) and run the following command to install Poetry:
   ```powershell
   curl -sSL https://install.python-poetry.org | python -
    ```

2. Add Poetry to Path: Add Poetry to your PATH by following the instructions provided after the installation completes. This typically involves adding Poetry's install location to the PATH environment variable. You can do this through the System Properties menu:

* Open the Start Search, type in "env", and select "Edit the system environment variables."
* In the System Properties window, click on the "Environment Variables" button.
* In the Environment Variables window, under "System variables", find the Path variable, select it, and click "Edit."
* Click "New" and add the path to the Poetry installation directory, typically C:\Users\<YourUsername>\AppData\Roaming\Python\Scripts

### Set Up the Environment
Clone the Repository: If you haven't already, clone the repository containing the Scrabble Trainer Chatbot code and navigate into the project directory:

```powershell
git clone https://github.com/wbarich/scrabble-champion.git
cd scrabble-champion
```

Install Dependencies: Use Poetry to install the dependencies specified in the pyproject.toml file:
```powershell
poetry install
```

Activate the Virtual Environment: Once the dependencies are installed, activate the virtual environment created by Poetry:

```powershell
poetry shell
```

With the environment set up, you're ready to run the Scrabble Trainer Chatbot!

## How to Run the Code

You can either run the code in the command line or as a Streamlit app.

### 1. In the Command Line:

Make sure that you have navigated to the folder where the scripts are in the command line. You should be in the root directory of the repository. For example:
```powershell
C:\Users\wrich\repos\scrabble-champion\
```

Then you can run the code by entering `python utils.py`.

### 2. As a Streamlit App
You can run the code as a Streamlit App.

Make sure that you have navigated to the folder where the scripts are in the command line. You should be in the root directory of the repository. For example:
```powershell
C:\Users\wrich\repos\scrabble-champion\
```

Then you can run the app as:
```powershell
streamlit run app.py
```


