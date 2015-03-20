# -*- coding:utf-8 -*-
import os
import shutil

import platform
is_windows = False
if str.lower(platform.uname()[0]) == "windows":
    is_windows = True


print "\nWelcome Project-Template."
print "Start your Project"

project_name = str(raw_input('\nTyping project name :'))
print "what is project name? is" + "\"" + project_name + "\"" + "."

project_path = "../" + project_name

print "Rename project to  " +  "\"" + project_name + "\"" + "..."
current_dir = os.path.abspath("./")
dest_dir = os.path.join(os.path.dirname(current_dir), project_name)
shutil.move(current_dir, dest_dir)


shutil.move("./project.conf", "./" + project_name +".conf")


change_file_list = list()

change_file_list.append({"filepath" : "./project_base.py", "is_remove" : True})
change_file_list.append({"filepath" : "./views/project_view.py", "is_remove" : True})
change_file_list.append({"filepath" : "./db/project_db.py", "is_remove" : True})
change_file_list.append({"filepath" : "./api/project_api.py", "is_remove" : True})
change_file_list.append({"filepath" : "./project.py", "is_remove" : True})
change_file_list.append({"filepath" : "./project.ini", "is_remove" : True})
change_file_list.append({"filepath" : "./start.sh", "is_remove" : False})
change_file_list.append({"filepath" : "./stop.sh", "is_remove" : False})


for file_info in change_file_list:


    with open(file_info["filepath"], "r") as f:
        file = f.read()
    file = file.replace("project", project_name)

    if file_info["is_remove"]:

        with open(file_info["filepath"].replace("project", project_name), "w") as f:
            f.write(file)
        os.remove(file_info["filepath"])

    else:
        with open(file_info["filepath"], "w") as f:
            f.write(file)
print "Complete. Enjoy Developing."