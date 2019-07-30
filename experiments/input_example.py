import subprocess
import cmd

user_name = input("What is yer name? \n")
user_quest = input("What is yer quest? \n")
user_color = input("What is yer favorite color? \n")

response = "So yer name is {0}, yer quest is {1} and yer favorite color is {2}"

print(response.format(user_name, user_quest, user_color))
