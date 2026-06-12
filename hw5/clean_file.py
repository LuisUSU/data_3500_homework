with open("/workspaces/data_3500_homework/hw5/AAPL.txt", "r") as file:
    content = file.read()

modified_content = content.replace(" ", "")

with open("/workspaces/data_3500_homework/hw5/AAPL.txt", "w") as file:
    file.write(modified_content)