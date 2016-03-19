import sys
from time import sleep
from os import system

print('############# Drive the robot ###########');
print('forward : z');
print('backward : s');
print('left : q');
print('right : d');

time = int(sys.argv[1]);

while(True):
	cmd = raw_input('waiting for order : ')

	if(cmd == 'z'):
		print('forward');
		system("python forward.py " + str(time));
	
	if(cmd == 's'):
                print('backward');
		system("python backward.py " + str(time));

	if(cmd == 'q'):
                print('left');
		system("python left.py " + str(time));

	if(cmd == 'd'):
                print('right');
		system("python right.py " + str(time));

