from termcolor import colored
import time
import random
import string

remove1,remove2,remove3,remove4,remove5,remove6= 0,0,0,0,0,0
while(1==1):
	for j in range(1,156):
		if(j%5==0):
			remove1=random.choice(range(1,25))
		if(j%10==0):
			remove2=random.choice(range(26,52))
		if(j%15==0):
			remove3=random.choice(range(53,75))
		if(j%20==0):
			remove4=random.choice(range(76,102))
		if(j%25==0):
			remove5=random.choice(range(102,125))
		if(j%30==0):
			remove6=random.choice(range(125,156))
		i1=random.choice(list(map(chr, range(0, 255))))
		i2=random.choice(list(map(chr, range(0, 255))))
		i3=random.choice(list(map(chr, range(0, 255))))

		i4=random.choice(list(map(chr, range(0, 255))))
		i5=random.choice(list(map(chr, range(0, 255))))
		i6=random.choice(list(map(chr, range(0, 255))))
		print(' '*remove1,colored(i1,'green',attrs=["bold"]),end='')
		print(' '*remove2,colored(i2,'green'),end='')
		print(' '*remove3,colored(i3,'green'),end='')
		print(' '*remove4,colored(i4,'green'),end='')
		print(' '*remove5,colored(i5,'green'),end='')
		print(' '*remove6,colored(i6,'green'))
		time.sleep(0.09)
