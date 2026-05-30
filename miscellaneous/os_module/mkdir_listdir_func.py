import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())


returned_value = os.system("mkdir my_first_directory")
print(returned_value)

