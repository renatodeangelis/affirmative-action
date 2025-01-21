import os
import pandas as pd

def replace_word_in_filenames(output_folder, old_word, new_word):
    for csv_file in os.listdir(output_folder):
        if csv_file.endswith(".csv") and old_word in csv_file:
            old_csv_path = os.path.join(output_folder, csv_file)
            new_csv_file = csv_file.replace(old_word, new_word)
            new_csv_path = os.path.join(output_folder, new_csv_file)
            
            # Rename the file
            os.rename(old_csv_path, new_csv_path)
            print(f"Renamed: {old_csv_path} to {new_csv_path}")

# Example usage
output_folder = "/Users/macbook/affirmative-action/data/tables"
old_word = "African"
new_word = "B2"

replace_word_in_filenames(output_folder, old_word, new_word)