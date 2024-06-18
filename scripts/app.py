import streamlit as st

from utils import retrieve_word_list, resample_sentance

# Streamlit app
def main():
    st.title("Scrabble Trainer Chatbot")

    # Load the word list
    word_list = retrieve_word_list()

    # Initialize session state for chat history
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Chat input
    user_input = st.chat_input("Your sentence:")

    if user_input:
        resampled_sentence = resample_sentance(user_input, word_list)

        # Add user input and bot response to chat history
        st.session_state.history.append(("user", user_input))
        st.session_state.history.append(("scrabble_genius", resampled_sentence))

        # Clear the input field
        st.session_state.user_input = ""

    # Display chat history
    for sender, message in st.session_state.history:
        if sender == "user":
            
            with st.chat_message("user"):
                st.write(message)

        else:
            with st.chat_message("assistant"):
                st.write(message)

if __name__ == "__main__":
    main()
