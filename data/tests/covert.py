data = 'data/tests/PSC_test/PSC_E2_0.txt'

# 1. Open the original file and read its contents
with open(data, "r") as file:
    content = file.read()

# 2. Replace all commas with tabs
modified_content = content.replace("\t", ", ")

# 3. Save the modified text to a new file
with open(data, "w") as file:
    file.write(modified_content)
