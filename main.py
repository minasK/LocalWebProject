import os
import sys

# os.getlogin()
# print(os.getlogin())
#
# #os.system("%windir%\system32\calc.exe")
#
# print(dir(os))
#
# #gives the current working directory
# print(os.getcwd())
#
# os.chdir('C:/Users/minas/OneDrive/Desktop')
# os.chdir('C:\Riot Games')
# print(os.getcwd())
#
# #list the direrectory where you are at
# print(os.listdir())

restartShutdown = input("do you want to shut down or restart the pc\n" +
                        "press 1 for shutdown 2 for restart\n" )

timeToRS = input("how much seconds to close")

# must be with " or else it wont read it
if (restartShutdown == "1"):
    os.system('shutdown /s /t %s' % timeToRS)


elif (restartShutdown == "2"):
    os.system('shutdown /r /t %s' % timeToRS)

# see how to exit the app in python
# else:
#     os.exit(0)
#     pass

# quit makes the the program python quit not the app

os.system('tasklist')
x=input("what do u want to close")
os.system('taskkill/im %s.exe /f' % x)




#to make comment simply press ctrl + /

# TODO sync this pc with laptop

