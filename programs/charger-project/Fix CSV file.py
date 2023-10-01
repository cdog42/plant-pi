import csv

# Define the unwanted port labels in this list
unwanted_port_labels = ["USB Bus 1 1.1.1","USB Bus 1 1.1"]  # Add more as needed

# Define a mapping of unfriendly port labels to friendly names
port_label_mapping = {
    "USB Bus 1 1.1.1.4": "Dad",
    "USB Bus 1 1.1.1.3": "Hudson",
    "USB Bus 1 1.1.1.2": "Meadow",
    "USB Bus 1 1.1.1.1": "Spare1",
    "USB Bus 1 1.1.4": "Spare2",
    "USB Bus 1 1.1.3":"Spare3",
    "USB Bus 1 1.1.2":"Spare4"
    # Add more mappings as needed
}

def clean_csv_file(filename):
    # Read the original rows
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        original_rows = list(reader)

    # Filter rows and replace unfriendly port labels
    cleaned_rows = []
    for row in original_rows:
        if row[0] not in unwanted_port_labels:
            # Replace the port label if a friendly name is defined
            row[0] = port_label_mapping.get(row[0], row[0])
            cleaned_rows.append(row)

    # Write the cleaned rows back to the CSV file
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)

if __name__ == "__main__":
    clean_csv_file("Charge Log.csv")
