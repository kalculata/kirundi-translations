import json
import os

file = "ikirundi-english.json"

# Read the JSON data from the file
with open(file, "r") as f:
  data = json.load(f)

# Sort the list of dictionaries based on the "rn" key (case-insensitive)
sorted_data = sorted(data, key=lambda x: x["rn"].casefold())

# Delete the old file
os.remove(file)

# Initialize a counter for duplicates deleted
duplicates_deleted = 0

# Create a dictionary to store unique translations
unique_translations = {}

# Create a list to store words with empty translations
empty_translations_words = []

# Iterate over sorted data and keep only unique translations
for item in sorted_data:
  rn = item["rn"].strip()
  en = item["en"].strip()
  if en == "":
    empty_translations_words.append(rn)

  if rn not in unique_translations:
    unique_translations[rn] = en
  else:
    duplicates_deleted += 1

# Reconstruct the data with unique translations
unique_data = [{"rn": rn, "en": en} for rn, en in unique_translations.items()]

# Write the unique translations to the file
with open(file, "w") as f:
  json.dump(unique_data, f, indent=2)

print("Number of duplicates deleted:", duplicates_deleted)
print("✨ Ordered and cleaned ✨")

# Print words with empty translations
if empty_translations_words:
  print("\nWords with empty translations:")
  for word in empty_translations_words:
    print("❓", word)
