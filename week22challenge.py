#Write a function called single_letter_count. This function takes in two parameters (two strings).
# The first parameter should be a word and the second should be a letter.
# The function returns the number of times that letter appears in the word.
# The function should be case insensitive (does not matter if the input is lowercase or uppercase).
# If the letter is not found in the word, the function should return 0.

def single_letter_count(word,letter):
    count=0
    for i, v in enumerate(word):
        if v.lower() == letter.lower():
            count=count+1
    return count

def main():
    word = input("Enter the word:")
    letter = input("Enter the letter to be counted:")
    print(single_letter_count(word,letter))

main()