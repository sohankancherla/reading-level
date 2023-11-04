from sys import exit

text = input("Text: ").strip()
if text == "":
    print("no text was entered")
    exit(1)

letters, words, sentences = 0, 1, 0 
for char in text:
    if char.isalpha():
        letters += 1
    elif char == " ":
        words += 1
    elif char in [".", "!", "?"]:
        sentences += 1

L = (100 / words) * letters
S = (100 / words) * sentences

index = round((0.0588 * L) - (0.296 * S) - 15.8)

if index <= 0:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")

exit(0)