# project_creator for Kinetis SDK 1.0.0GA release
# Author: Neo (b44513@freescale.com)

import os
import shutil
import msvcrt

print "------------- Welcome to project creator for Kinets SDK -------------"


work_path = os.getcwd()

prj_name = raw_input("Step1: Input the project name you want to create:")
#print "Your project name is {0}".format(prj_name)
brd_name = raw_input("Step2: Input the board name you want to create:")
#print "Your board name is {0}".format(brd_name)
print "Step3: Select one of below Freescale official boards as a clone base"


# list all TWR or FRDM boards dir in /demos/hello_world/IDE/ folder
work_path = os.getcwd()
base_ide_path = work_path + "/hello_world/iar"
base_src_path = work_path + "/hello_world/src"

files = os.listdir(base_ide_path)
n = 0
for f in files:
#    if (os.path.isdir(work_path + '/' + f)):
    if ('twr' in f) or ('frdm' in f):
        n = n + 1
        print "{0}: {1}".format(n, f)

# check if no boards there.
if n == 0:
    print "*** ERROR! No TWR or FRDM board was found in '/demos/hello_world/iar' folder ***"
    exit()

# key in to select the base board
while True:
    ch = msvcrt.getch()
    if ch >= '1' and ch <= str(n):
        break
base_prj_name = files[int(ch) - 1];

# create /demos/prj_name/IDE/brd_name folder
prj_path = work_path + '/' + prj_name
os.mkdir(prj_path);

ide_path = prj_path + '/' + 'iar'
os.mkdir(ide_path)

src_path = prj_path + '/' + 'src'
os.mkdir(src_path)

workspace_path = ide_path + '/' + brd_name
os.mkdir(workspace_path)

# copy src file
shutil.copy(base_src_path + '/' + "hello_world.c", src_path + '/' + prj_name + '.c')

# copy project and workspace files
shutil.copy(base_ide_path + '/' + base_prj_name + '/' + "hello_world.eww", workspace_path + '/' + prj_name + '.eww')
shutil.copy(base_ide_path + '/' + base_prj_name + '/' + "hello_world.ewp", workspace_path + '/' + prj_name + '.ewp')
shutil.copy(base_ide_path + '/' + base_prj_name + '/' + "hello_world.ewd", workspace_path + '/' + prj_name + '.ewd')

print "SUCCESS"
