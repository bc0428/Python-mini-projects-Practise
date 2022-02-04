from difflib import SequenceMatcher

with open('FILE PATH 1') as file_1, open('FILE PATH 2') as file_2:
    file_1_strings = file_1.read()
    file_2_strings = file_2.read()
    similarity_index = SequenceMatcher(None, file_1_strings, file_2_strings).ratio()
    print(f"similarity: {similarity_index}")
