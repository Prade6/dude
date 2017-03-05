import os

usrCmd = raw_input()

if "create" and "folder" in usrCmd.lower():
    print ("creating new folder")
    os.system("mkdir" + " " + "fldrByPython")

else:
    print ("no new folder created")
