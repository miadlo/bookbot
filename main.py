def main():
    frankenstein = read_book("books/frankenstein.txt")
    print(f'Number of words: {numOfWords(frankenstein)}')
    report_print(countLetters(frankenstein))

def report_print(counted):
    for letter in counted:
        print(f'The {letter} was found {counted[letter]} number of times')

def read_book(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def numOfWords(book):
    splitBook = book.split()
    return len(splitBook)

def countLetters(book):
    counted = {}
    lettersToCount = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lowerCaseBook = book.lower()
    for letter in lettersToCount:
        numberCounted = 0
        for character in lowerCaseBook:
            if character == letter:
                numberCounted += 1
        counted[letter] = numberCounted
    return counted

if __name__ == "__main__":
    main()