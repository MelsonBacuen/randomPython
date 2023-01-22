import os
# This is just a simple python script to automatically update a linux distro
# I'm just a beginner in python feel free to modify my code any way you like
print("hello this script will update and upgrade your linux distro")
con = input("do you want to continue Yes or No")

if con == "No":
    update = "sudo apt update"
    upgrade = "sudo apt upgrade"

    os.system(update)
    os.system(upgrade)
else:
    exit()
