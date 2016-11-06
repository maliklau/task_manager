import math;
import time;
import calendar;
import string;
import sys, traceback;

def display_date():
	localtime = time.asctime( time.localtime(time.time()) )
	print "TODAY :", localtime

def display_calendar(year, month):
	cal = calendar.month(year, month)
	print "Calendar:"
	print cal
	print " "
	
def display_tasks(file_tsk):
	print " "
	print "Tasks for (day)"
	i = 1
	for tasks in file_tsk:
	 	i = str(i)
		print i + ". " + tasks
		i = int(i)
		i = i + 1
	print " "		

def del_tsk(tsk_lst, tsk_num):
	if tsk_num == "all":
		for tasks in tsk_lst:
			tsk_lst.remove(tasks)
		print "Wow, you're productive!"
	else:
		tsk_num = int(tsk_num)
		finished = tsk_lst.pop(tsk_num-1)
		print "You've completed " + finished
	
	print " "

def get_input(tsk_lst):
	choice = raw_input("Calendar(C), Write task(W), Finished task(F), Exit(X): ")	
	if choice =='C':
                month = int(raw_input("search month #: "))
                year = int(raw_input("search year: "))
                print " "
                display_calendar(year, month)

        if choice =='W':
                #new_file = open("tasks.txt",'w')
                new_file = create_task(tsk_lst);
                display_tasks(new_file);
	
	if choice == 'F':
		to_del = str(raw_input("Which task is completed (# or all)? "))
		del_tsk(tsk_lst, to_del)

        if choice == 'X':
                exit(0)	

	get_input(tsk_lst)
	print " "
	
def create_task(tsk_lst):
	task = str(raw_input("New task: "))
	tsk_lst.append(task)
	return tsk_lst

def main():
	tsk_lst = []
	display_date()
	print " "
	get_input(tsk_lst)

main()
