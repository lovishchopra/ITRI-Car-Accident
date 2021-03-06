import os
import yoloCarAccident as yc

# yc.find('test.txt')

f1 = open('result2.txt','r')

i = 0
s = ""
for lines in f1:
	if(i<80000):
		s += lines
		i+=1
	else:
		f2 = open('test.txt','w')
		f2.write(s)
		f2.close()
		try:
			yc.find('test.txt')
		except ValueError:
			pass
		s = ""
		i = 0
		# break

# f2 = open('test.txt','w')
# f2.write(s)
# f2.close()
# yc.find('test.txt')