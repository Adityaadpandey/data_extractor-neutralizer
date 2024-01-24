import re

def remove_timestamp(line):
    # Define pattern to match timestamp at the beginning of the line
    timestamp_pattern = re.compile(r'^\d+:\d+:\d+\.\d+\s')

    # Remove timestamp from the line
    return re.sub(timestamp_pattern, '', line)

def clean_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Remove timestamps from each line
    cleaned_lines = [remove_timestamp(line) for line in lines]

    # Remove the first line
    cleaned_lines = cleaned_lines[1:]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(cleaned_lines)
if __name__ == "__main__":
    input_file_path = "chc.txt"
    output_file_path = "tes.txt"

    clean_text(input_file_path, output_file_path)
    print("Timestamps removed successfully.")
