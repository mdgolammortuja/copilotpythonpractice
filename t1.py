# Task: Read the contents of 'data.txt' and print each line with line numbers
with open('data.txt', 'r') as file:
    # Use Copilot to complete the code to read and print each line with line numbers
    for line_number, line in enumerate(file, start=1):
        # TODO: Complete the code here
        print(f"Line {line_number}: {line.strip()}")
