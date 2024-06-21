def get_book():
  with open("books/frankenstein.txt") as f:
    return f.read()

def word_count(book):
  words = book.split()
  return len(words)

def letter_count(book):
  letters = {}
  count = 1
  for char in book.lower():
    if char in letters:
      letters[char] += count
    else:
      letters[char] = count
  return letters

def sort_on(dict):
    return dict["num"]
  
def report(book):
  char_list = []
  letters = letter_count(book)
  print("--- Begin report of books/frankenstein.txt ---")
  print(word_count(book), "words found in the document")
  
  for key, val in letters.items():
    char_list.append({"char":key, "num":val})
  char_list.sort(reverse=True, key=sort_on)
  for char in char_list:
    if char["char"].isalpha():
      print(f"The {char['char']} character was found {char['num']} times")
  
  print("--- End report ---")

def main():
  book = get_book()
  word_count(book)
  letter_count(book)
  report(book)

main()
