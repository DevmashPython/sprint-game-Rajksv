import time
import msvcrt

finish=10
count=0

print "Start: "

s_time=time.time()

while 1:
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print "-->",
	else :
		print"wrong key,you lose!"
		break
	if count==finish:
		break
print "\n"
count=0
while 1:
	key=msvcrt.getch()
	if key=='s':
		count=count+1
		print "				       |\n",
	else :
		print"wrong key,you lose!"
		break
	if count==finish:
		break
count=0
while 1:
	key=msvcrt.getch()
	if key=='d':
		count=count+1
	if count==1 :
		print "				       -->",
	elif count!=1 :
		print "-->",
	else :
		print"wrong key,you lose!"			
	if count==finish:
			break
time_elapsed=time.time() - s_time
print "\nGame over. Time taken: " + str(time_elapsed) + ' seconds'


'''
1. Mention controls for the game.
2. The program should exit after wrong key is pressed.
3. mention when to turn right and down
'''
