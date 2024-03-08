import json

file = "ikirundi-english.json"

with open(file, "r") as f:
  data = json.load(f)

# Count the number of translations
num_translations = len(data)

print("Translation File Information:")
print("------------------------------")
print(f"File Name: {file}")
print(f"Number of Translations: {num_translations}")
