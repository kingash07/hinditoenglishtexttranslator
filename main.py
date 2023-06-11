import csv
import pandas as pd
from googletrans import Translator


# # Read the original CSV file
# df = pd.read_csv('airport1_499.csv')
#
# # Create a translator object
# translator = Translator()
#
# # Open the new file in append mode
# new_file = open('translated_rows.csv', 'a')
#
# # Iterate over each row of the DataFrame
# for index, row in df.iterrows():
#     # Get the value of the row you want to translate
#     text_to_translate = row['Owners']
#
#     # Translate the text
#     translated_text = translator.translate(text_to_translate).text
#
#     # Append the translated row to the new file
#     new_file.write(translated_text + '\n')
#
#     # Delete the translated row from the DataFrame
#     df.drop(index, inplace=True)
#
# # Close the new file
# new_file.close()
#
# # Save the updated DataFrame to the original file without the translated rows
# df.to_csv('airport1_499.csv', index=False)

def translate_hindi_to_english(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text


# def translate_hindi_to_hinglish(text):
#     pass
# Implement your Hinglish translation logic here
# You can use any available Hinglish translation library or API


def translate_csv(input_file, output_file, column_name, translate_func):
    df = pd.read_csv(input_file, encoding='utf-8', usecols=[column_name])

    translated_column = df[column_name].apply(translate_func)

    with open(output_file, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(df.columns.tolist())  # Write the header row to the output file

        for index, row in df.iterrows():
            translated_row = row.tolist()
            translated_row[df.columns.get_loc(column_name)] = translated_column[index]
            writer.writerow(translated_row)


# Example usage: Translate Hindi cells to English
translate_csv(input_file='airport1_499.csv', output_file='output.csv', translate_func=translate_hindi_to_english,
              column_name='Owners')

# Example usage: Translate Hindi cells to Hinglish
# translate_csv('input.csv', 'output.csv', translate_hindi_to_hinglish)


# remove the original file
# import pandas as pd
# from googletrans import Translator
# import time
# import csv
# import os
# import json
#
#
# def translate_hindi_to_english(text):
#     translator = Translator(service_urls=['translate.google.com'])
#     translation = None
#     rnt = 0
#     retries = 3
#     while retries > 0:
#         try:
#             translation = translator.translate(text, src='hi', dest='en')
#             rnt += 1
#             print(rnt)
#             break
#         except Exception as e:
#             print(f"Translation error: {e}")
#             print("Retrying...")
#             retries -= 1
#             time.sleep(1)  # Wait for 1 second before retrying
#     return translation.text if translation is not None else ''
#
#
#
#
#
# def translate_csv(input_file, output_file, column_name, translate_func):
#     df = pd.read_csv(input_file, encoding='utf-8')
#     rnt = 0
#     translated_column = df[column_name].apply(translate_func)
#
#     with open(output_file, 'a', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#
#         for index, row in df.iterrows():
#             translated_value = translated_column[index]
#             rnt += 1
#             print(rnt)
#             if translated_value is not None:
#                 translated_row = row.tolist()
#                 translated_row[df.columns.get_loc(column_name)] = translated_value
#                 writer.writerow(translated_row)
#                 rnt +=1
#                 print(rnt)# Append the translated row to the output file
#
#     df.dropna(subset=[column_name], inplace=True)
#     df.to_csv(input_file, index=False)  # Update the input file without the translated rows
#
#
# # Example usage: Translate the "HindiColumn" to English and append to a new CSV file
# translate_csv(input_file='kangra_Airport1_499.csv', output_file='output.csv', translate_func=translate_hindi_to_english, column_name='Owners')
#

# def translate_hindi_to_english(text):
#     translator = Translator(service_urls=['translate.google.com'])
#     translation = translator.translate(text, src='hi', dest='en')
#     return translation.text
#
#
# def translate_hindi_to_hinglish(text):
#     pass
#     # Implement your Hinglish translation logic here
#     # You can use any available Hinglish translation library or API
#
#
# def translate_csv(input_file, output_file, column_name, translate_func):
#     df = pd.read_csv(input_file, encoding='utf-8')
#
#     translated_column = df[column_name].apply(translate_func)
#
#     rows_to_delete = []
#
#     with open(output_file, 'a', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(df.columns.tolist())  # Write the header row to the output file
#
#         for index, row in df.iterrows():
#             translated_row = row.tolist()
#             translated_row[df.columns.get_loc(column_name)] = translated_column[index]
#             writer.writerow(translated_row)  # Append the translated row to the output file
#
#             if not pd.isna(translated_column[index]):
#                 rows_to_delete.append(index)
#
#     # Delete the rows from the input file
#     if rows_to_delete:
#         df.drop(rows_to_delete, inplace=True)
#         df.to_csv(input_file, index=False)
#
#     # Remove the output file if it's empty
#     if os.path.isfile(output_file) and os.stat(output_file).st_size == 0:
#         os.remove(output_file)
#
#
# # Example usage: Translate the "HindiColumn" to English and append to a new CSV file,
# # and delete the translated rows from the input file
# translate_csv(input_file='kangra_Airport.csv', output_file='output.csv', translate_func=translate_hindi_to_english,
#               column_name='Owners')
