file = open("/workspaces/data_3500_homework/hw5/NVDA.txt", "r")
content = file.read()
modified_content = content.replace(" ", "")

file = open("/workspaces/data_3500_homework/hw5/NVDA.txt", "w")
file.write(modified_content)