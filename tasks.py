import math;
import time;
import calendar;
import string;
import sys, traceback;
import pickle;

def display_date():
	localtime = time.asctime( time.localtime(time.time()) )
	print "TODAY :", localtime	
	localtime =  str(localtime)
	localtime = localtime[4:11] + localtime[19:]
	return localtime
 
def display_calendar(year, month):
	cal = calendar.month(year, month)
	print "Calendar:"
	print cal
	print " "
		

def display_tasks(file_tsk, date):
	print " "
	print "Tasks for", date
	i = 1
	for tasks in file_tsk:
	 	i = str(i)
		print i + ". " + tasks
		i = int(i)
		i = i + 1
	print " "		

def del_tsk(dic_tsk, tsk_lst, tsk_num, date):
	if tsk_num == "all":
		del dic_tsk[date]
		print "Wow, you're productive!"
	else:
		tsk_num = int(tsk_num)
		finished = tsk_lst.pop(tsk_num-1)
		print "You've completed " + finished
	
	print " "

def get_list(dic_tsk, date):
	return dic_tsk.get(date)

def get_input(dic_tsk, tsk_lst, date):
	choice = raw_input("Calendar(C), Write task(W), Finished task(F), Exit(X): ")	
	if choice =='C':
		try: 
               		 month = int(raw_input("search month #: "))
			 year = int(raw_input("search year: "))
		except IndexError:
                        print("Not a valid time value")
                except ValueError:
                        print("Not a valid time value")
                print " "
		try:
               		 display_calendar(year, month)
		except IndexError:
			print("Not a valid time value")
			get_input(dic_tsk, tsk_lst, date)
		date = str(raw_input("Choose date to add tasks: "))				
		dic_tsk = create_task(dic_tsk, tsk_lst, date)
		tsk_lst = get_list(dic_tsk, date)
		display_tasks(tsk_lst, date)

        if choice =='W':
                dic_tsk = create_task(dic_tsk, tsk_lst, date);
		tsk_lst = get_list(dic_tsk, date)
                display_tasks(tsk_lst, date);
	
	if choice == 'F':
		to_del = str(raw_input("Which task is completed (# or all)? "))
		del_tsk(dic_tsk, tsk_lst, to_del, date)

	print "DIC: ", dic_tsk
	print " "
        if choice == 'X':
		save_dic(dic_tsk)
                exit(0)	

	get_input(dic_tsk, tsk_lst, date)
	print " "	
def create_task(dic_tsk, tsk_lst, date):
	task = str(raw_input("New task: "))
	if date in dic_tsk:
		tsk_lst.append(task)
		dic_tsk[date] = tsk_lst
	else:
		tsk_lst = []
		tsk_lst.append(task)
		dic_tsk[date] = tsk_lst
	return dic_tsk

def save_dic(dic_tsk):
	  svd_file = open('dic_file.pk1', 'wb')
          pickle.dump(dic_tsk, svd_file)
          svd_file.close()		

def unpickle():
	dic_again = open('dic_file.pk1','rb')
	dic_tsk = pickle.load(dic_again)
	return dic_tsk

def main():
	tsk_lst = []
	try:
		dic_tsk = unpickle()
	except IOError:  
		dic_tsk = {}
	date = display_date()
	print " "
	get_input(dic_tsk, tsk_lst, date)
main()
