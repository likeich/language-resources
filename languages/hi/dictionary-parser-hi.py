import csv

# Specify the input and output file names
directory = 'languages/hi/'
input_filename = directory + 'dictionary-source-hi.csv'
output_filename = directory + 'dictionary-hi.csv'

# Open the input file in read mode and output file in write mode
with open(input_filename, mode='r', newline='', encoding='utf-8') as file_in, \
     open(output_filename, mode='w', newline='', encoding='utf-8') as file_out:
    # Create a CSV reader
    reader = csv.DictReader(file_in)

    # Create a list of fieldnames excluding the first column
    # Assuming the first column is at index 0
    fieldnames = reader.fieldnames[1:]  # Removes the first element in the fieldnames list

    # Create a CSV writer with updated fieldnames
    writer = csv.DictWriter(file_out, fieldnames=fieldnames)

    # Write the header to the output file
    writer.writeheader()

    # Iterate over each row in the input CSV
    for row in reader:
        # Modify the row dict to remove the key of the first column
        row.pop(reader.fieldnames[0], None)  # Safely remove the first column key

        # Check if the 'hi' column contains exactly one word
        # Make sure 'hi' is still in the row after popping the first column
        if 'hi' in row and len(row['hi'].split()) == 1:
            # Write rows that meet the criterion to the output file
            writer.writerow(row)

print("Filtering complete. Check the output file:", output_filename)
