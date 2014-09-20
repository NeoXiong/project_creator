# project_creator for Kinetis SDK 1.0.0GA release
# Author: Neo (b44513@freescale.com)

import os
import shutil
import msvcrt
import time

def DisplayMsgExit(info):
	print info
	time.sleep(2)
	exit(1)

print "------------- Welcome to project creator for Kinetis SDK -------------"
# check environment 
WORK_PATH = os.getcwd()
BASE_PRJ_PATH = WORK_PATH + '/' + "hello_world"
BOARDS_PATH = WORK_PATH + '/' + ".." + '/' + "boards"
if (not os.path.exists(BASE_PRJ_PATH)) or (not os.path.exists(BOARDS_PATH)):
	DisplayMsgExit("\n*** ERROR! Make sure project_creator.exe in KSDK_x.x.x/demos ***")

# #get prj_name, brd_name, ide_name and base_prj_name
prj_name = raw_input("Step1: Input the project name you want to create:")
brd_name = raw_input("Step2: Input the board name you want to create:")

print "Step2: Which IDE project you want to create:"

# list all IDE folders in /demos/hello_world/
files = os.listdir(BASE_PRJ_PATH)
n = 0
valid_files = []
for f in files:
	if ('iar' in f) or ('kds' in f) or ('uv4' in f):
		valid_files.append(f)
		n = n + 1
		print "{0}: {1}".format(n, f)
# check if no IDE there.
if n == 0:
    DisplayMsgExit("\n*** ERROR! No IDE was found ***")
# key in to select the IDE
while True:
    ch = msvcrt.getch()
    if ch >= '1' and ch <= str(n):
        break
ide_name = valid_files[int(ch) - 1];

print "Step4: Select a TWR or FRDM board as a clone base"

# list all TWR or FRDM boards in /demos/hello_world/IDE/ folder
BASE_IDE_PATH = WORK_PATH + '/' + "hello_world"+ '/' + ide_name
files = os.listdir(BASE_IDE_PATH)
n = 0
valid_files = []
for f in files:
    if ('twr' in f) or ('frdm' in f):
		valid_files.append(f)
		n = n + 1
		print "{0}: {1}".format(n, f)
# check if no base boards there.
if n == 0:
    DisplayMsgExit("\n*** ERROR! No TWR or FRDM board was found ***")
# key in to select the base board
while True:
    ch = msvcrt.getch()
    if ch >= '1' and ch <= str(n):
        break
base_brd_name = valid_files[int(ch) - 1];

# copy all files in boards/base_brd_name to boards/brd_name
shutil.copytree(BOARDS_PATH + '/' + base_brd_name, BOARDS_PATH + '/' + brd_name)

# rename base_brd_name*.peb to brd_name*.peb
files = os.listdir(BOARDS_PATH + '/' + brd_name)
for f in files:
    if base_brd_name in f:
		new_f = f.replace(base_brd_name, brd_name)
		os.rename(BOARDS_PATH + '/' + brd_name + '/' + f, BOARDS_PATH + '/' + brd_name + '/' + new_f)  

# create /demos/prj_name/
PRJ_PATH = WORK_PATH + '/' + prj_name
os.mkdir(PRJ_PATH);
# create /demos/prj_name/IDE
IDE_PATH = PRJ_PATH + '/' + ide_name
os.mkdir(IDE_PATH)
# create /demos/prj_name/src
SRC_PATH = PRJ_PATH + '/' + 'src'
os.mkdir(SRC_PATH)
# create /demos/prj_name/IDE/brd_name
WORKSPACE_PATH = IDE_PATH + '/' + brd_name
os.mkdir(WORKSPACE_PATH)

# copy hello.c file and rename to prj_name.c 
BASE_SRC_PATH = WORK_PATH + '/' + "hello_world"+ '/' + "src"
shutil.copy(BASE_SRC_PATH + '/' + "hello_world.c", SRC_PATH + '/' + prj_name + '.c')

if ide_name == "iar":
	# copy project files and replace string 'hell_world' to prj_name, base_brd_name to brd_name
	srcfile     = open(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "hello_world.eww", 'r')
	targetfile  = open(WORKSPACE_PATH + '/' + prj_name + ".eww", 'w')
	for line in srcfile:
		targetfile.write(line.replace("hello_world", prj_name).replace(base_brd_name, brd_name))
	targetfile.close()
	srcfile.close()

	srcfile     = open(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "hello_world.ewp", 'r')
	targetfile  = open(WORKSPACE_PATH + '/' + prj_name + ".ewp", 'w')
	for line in srcfile:
		targetfile.write(line.replace("hello_world", prj_name).replace(base_brd_name, brd_name))
	targetfile.close()
	srcfile.close()

	srcfile     = open(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "hello_world.ewd", 'r')
	targetfile  = open(WORKSPACE_PATH + '/' + prj_name + ".ewd", 'w')
	for line in srcfile:
		targetfile.write(line.replace("hello_world", prj_name).replace(base_brd_name, brd_name))
	targetfile.close()
	srcfile.close()
elif ide_name == "uv4":
	# copy project files and replace string 'hell_world' to prj_name, base_brd_name to brd_name
	srcfile     = open(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "hello_world.uvmpw", 'r')
	targetfile  = open(WORKSPACE_PATH + '/' + prj_name + ".uvmpw", 'w')
	for line in srcfile:
		targetfile.write(line.replace("hello_world", prj_name).replace(base_brd_name, brd_name))
	targetfile.close()
	srcfile.close()

	srcfile     = open(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "hello_world.uvproj", 'r')
	targetfile  = open(WORKSPACE_PATH + '/' + prj_name + ".uvproj", 'w')
	for line in srcfile:
		targetfile.write(line.replace("hello_world", prj_name).replace(base_brd_name, brd_name))
	targetfile.close()
	srcfile.close()
	
	# copy .uvopt if existed
	if os.path.exists(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "hello_world.uvopt"):
		srcfile     = open(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "hello_world.uvopt", 'r')
		targetfile  = open(WORKSPACE_PATH + '/' + prj_name + ".uvopt", 'w')
		for line in srcfile:
			targetfile.write(line.replace("hello_world", prj_name).replace(base_brd_name, brd_name))
		targetfile.close()
		srcfile.close()
	
	# copy pemicro_connection_settings.ini if existed
	if os.path.exists(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "pemicro_connection_settings.ini"):
		shutil.copy(BASE_IDE_PATH  + '/' + base_brd_name + '/' + "pemicro_connection_settings.ini", WORKSPACE_PATH + '/' + "pemicro_connection_settings.ini")
elif ide_name == "kds":
	print "ERROR, kds is not ready"

# end
DisplayMsgExit("\n*** Successful ***")
