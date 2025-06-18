'''with open("simpletextfile.txt", "w") as file:
    wrt_obj = file.write("Hello welcome to python file handling")
    print("characters written", wrt_obj)'''
import csv

# write() will write string to file and return numbers of charters written into file
#######################################################################################################
# To check file exists if not raise filenotFound error
"""import os

filename = "simpextfile.txt"
try :
    with open("simpextfile.txt","r") as file:
        print("File located in", os.path.abspath(filename))
except FileNotFoundError:
    print(f"File '{filename}' does NOT exist.")
except Exception as e:
    print(f"An error occurred: {e}")"""
#######################################################################################################
"""import csv


def process_csv(input_file, output_file):
    filtered_rows = []

    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)

        for row_num, row in enumerate(reader, start=1):
            try:
                # Example columns: 'Name', 'Age', 'Email', 'Score'

                # Handle missing data
                if not row['Name'] or not row['Age'] or not row['Score']:
                    print(f"Skipping row {row_num}: missing required data")
                    continue

                # Convert age and score to int/float safely
                age = int(row['Age'])
                score = float(row['Score'])

                # Filter condition: Age > 18 and Score >= 75
                if age > 18 and score >= 75:
                    filtered_rows.append(row)

            except ValueError as e:
                print(f"Skipping row {row_num}: invalid data format ({e})")
                continue

    # Define CSV output headers
    headers = ['Name', 'Age', 'Email', 'Score']

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(filtered_rows)

    print(f"Filtered data written to {output_file}")


# Usage
process_csv('score.csv', 'filtered_output.csv')
"""
#######################################################################################################
with open("score.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
