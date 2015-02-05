# -*- coding:utf-8 -*-
import os
import shutil

import platform
is_windows = False
if str.lower(platform.uname()[0]) == "windows":
    is_windows = True


def yellow(msg):
    if is_windows:
        return msg
    else:
        return "\033[1;33m" + msg + "\033[1;m"


def red(msg):
    if is_windows:
        return msg
    else:
        return "\033[1;41m" + msg + "\033[1;m"

print yellow("\nWelcome Project-Template.")
print yellow("Start your Project")

project_name = str(raw_input(yellow('\nTyping project name :')))
print "what is project name? is" + red("\"" + project_name + "\"") + "."

project_path = "../" + project_name

print "Rename project to  " + red("\"" + project_name + "\"") + "..."
current_dir = os.path.abspath("./")
dest_dir = os.path.join(os.path.dirname(current_dir), project_name)
shutil.move(current_dir, dest_dir)


shutil.move("./project.conf", "./" + project_name +".conf")

with open("./project_base.py", "r") as f:
    file = f.read()
file = file.replace("project", project_name)
with open("./" + project_name+"_base.py", "w") as f:
    f.write(file)
os.remove("./project_base.py")


with open("./views/project_view.py", "r") as f:
    file = f.read()
file = file.replace("project", project_name)
with open("./views/"+ project_name + "_view.py", "w") as f:
    f.write(file)
os.remove("./views/project_view.py")

with open("./db/project_db.py", "r") as f:
    file = f.read()
file = file.replace("project", project_name)
with open("./db/"+ project_name + "_db.py", "w") as f:
    f.write(file)
os.remove("./db/project_db.py")

with open("./api/project_api.py", "r") as f:
    file = f.read()
file = file.replace("project", project_name)
with open("./api/"+ project_name + "_api.py", "w") as f:
    f.write(file)
os.remove("./api/project_api.py")



with open("./main.py", "r") as f:
    file = f.read()
file = file.replace("project", project_name)
with open("./main.py", "w") as f:
    f.write(file)


print yellow("Complete. Enjoy Developing.")
