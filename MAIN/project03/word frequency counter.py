import string

def count_words(text):
    word_freq = {}
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

def order_dict_by_freq(dictionary):
    sorted_values = []

    for key in dictionary:
        #(dictionary[key], key) makes a tuple with count, then key
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values

def main():
    choice = input("Enter '1' to input text manually or '2' to read from a file: ")
    
    if choice == '1':
        text = input("Enter the text: ")
        word_freq = count_words(text)
    elif choice == '2':
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                text = file.read()
                word_freq = count_words(text)
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid choice.")
        return

    print("\nWord frequencies:")
    


    top_words = order_dict_by_freq(word_freq)
    for tuple_freq in top_words:
        word_freq,word = tuple_freq
        print("{0:15}{1:8d}".format(word,word_freq))


if __name__ == "__main__":
    main()
