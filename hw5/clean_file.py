file = open("/workspaces/data_3500_homework/hw5/AMD.txt", "r")
content = file.read()
modified_content = content.replace(" ", "")

file = open("/workspaces/data_3500_homework/hw5/AMD.txt", "w")
file.write(modified_content)