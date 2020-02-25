# BOINC-STYLE program Description
# ===============================================
# this program is the simplest one
# ===============================================

import sys
import time
import random
import os
#======================= GLOBAL VARS  =============
#__CLOUDBOOK:GLOBAL__
number_of_agents=0



# =================================================
# MAIN function always falls into DU0 --> Agent0
#__CLOUDBOOK:MAIN__
def main():
	global boinc_dict
	os.system('cls')  # on windows
	#########################################
	#main program to execute by command line
	#=======================================
	print (" ")
	print (" ")
	print ("Welcome to BOINC program (V1.0)")
	print ("===============================")
	text=""
	while text=="":
		text=input ("Aproximate number of agents?:")
	
	global number_of_agents
	number_of_agents=int(text)

	
	du0_main_boinc_menu()

# ====================================================
#__CLOUDBOOK:LOCAL__
def local_T1():
	cad="\n hello, I am doing T1"
	du0_print (cad)

# =====================================================
#__CLOUDBOOK:LOCAL__
def local_T2():
	cad="\n hello, I am doing T2"
	du0_print (cad)
	

# =====================================================
#__CLOUDBOOK:DU0__
def du0_print(cad):
	print(cad)

# ====================================================
#__CLOUDBOOK:PARALLEL__
def parallel_do_task(task):
	if (task % 2 ==0):
		local_T1()
	else :
		local_T2()
	
# ======================================================
#__CLOUDBOOK:DU0__
def du0_interactive_run():
	global number_of_agents

	input("start? (press ENTER)")
	for i in range(number_of_agents):
		parallel_do_task(i) 

	print ("\n all agents launched \n")
	
	#__CLOUDBOOK:SYNC__
	print ("\n all agents finished \n")

#=====================================================
#__CLOUDBOOK:DU0__
def du0_main_boinc_menu():

	while (True):		
		#os.system('cls')  # on windows
		print("")
		print ("main menu options")
		print ("=================")
		print (" r: run agents")
		print (" x: exit")
		
		command=input ("command?:")
		if (command=="x"):
			sys.exit()
		elif (command=="r"):
			du0_interactive_run()
		
#=======================================================


main()