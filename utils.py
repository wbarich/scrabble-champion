import random

def retrieve_word_list():
    """
    Read in the word list from the file.
    """
    word_list_path = "data/words_alpha.txt"
    with open(word_list_path, "r") as f:
        word_list = f.readlines()

    #clean up the word list. assume lower case only allowed
    word_list = [word.strip().lower() for word in word_list]
    return word_list    

def resample_word(word_list, input_word):
    """
    For any input word, resample the word from the word list. 
    """
    #make sure that the input word is of standard format
    input_word = input_word.strip().lower()

    #filter for words that start with the same letter
    filtered_set = [x for x in word_list if x.startswith(input_word[0])]

    #filter for words that have the same length
    filtered_set = [x for x in filtered_set if len(x) == len(input_word)]

    #if there are no words then return the original word
    if len(filtered_set) == 0:
        return input_word
    
    # if there is only 1 word in the filtered_set and it is the same as the input word
    # it is not a problem because we should return the input word in that case
    
    #else sample a word from the remaining set
    return random.choice(filtered_set)
    
def split_input_sentence(input_sentence):
    """
    Split the input sentence into words.
    Assume that words are only separated by spaces.
    No other delimiter is allowed.
    """
    return input_sentence.split(" ")

def test_input_validity(input_sentence):
    """
    Check that the user input is valid.
    No numbers may be submitted in any of the input words.
    """
    words = split_input_sentence(input_sentence)
    for word in words:
        if any(char.isdigit() for char in word):
            return False
    return True

def resample_sentence(input_sentence, word_list):
    """
    Resample the input sentence by resampling each word.
    """
    try:
        #only continue if the user's input is valid (no digits in the words)
        if test_input_validity(input_sentence):
            words = split_input_sentence(input_sentence)
            resampled_words = [resample_word(word_list, word) for word in words]
            return " ".join(resampled_words)
        else:
            return "Invalid input. Please try again."
    except:
        return "An unhandled exception occured."

if __name__ == "__main__":
    word_list = retrieve_word_list()

    test_case = "lightly fried fish are delicious"
    resampled_sentence = resample_sentence(test_case, word_list)

    print(f"Original:  {test_case}")
    print(f"Resampled: {resampled_sentence}")

    test_case = "zygomaticosphenoidalis are really nice"
    resampled_sentence = resample_sentence(test_case, word_list)

    print(f"Original:  {test_case}")
    print(f"Resampled: {resampled_sentence}")

    input_sentence = input("Enter a sentence: ")
    response = resample_sentence(input_sentence, word_list)
    print(f"Resampled sentence: {response}")
