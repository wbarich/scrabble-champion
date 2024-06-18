import random

def retrieve_word_list():
    """
    Read in the word list from the file.
    """
    word_list_path = "../data/words_alpha.txt"
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
    
    #else sample a word from the remaining set
    return random.choice(filtered_set)
    
def split_input_sentence(input_sentence):
    """
    Split the input sentence into words.
    Assume that words are only separated by spaces.
    No other delimiter is allowed.
    """
    return input_sentence.split(" ")

def resample_sentance(input_sentance, word_list):
    """
    Resample the input sentance by resampling each word.
    """
    words = split_input_sentence(input_sentance)
    resampled_words = [resample_word(word_list, word) for word in words]
    return " ".join(resampled_words)

if __name__ == "__main__":
    word_list = retrieve_word_list()

    test_case = "lightly fried fish are delicious"
    resampled_sentance = resample_sentance(test_case, word_list)

    print(f"Original:  {test_case}")
    print(f"Resampled: {resampled_sentance}")

    test_case = "zygomaticosphenoidalis are really nice"
    resampled_sentance = resample_sentance(test_case, word_list)

    print(f"Original:  {test_case}")
    print(f"Resampled: {resampled_sentance}")

    input_word = input("Enter a word: ")
    print(f"Resampled word: {resample_word(word_list, input_word)}")
