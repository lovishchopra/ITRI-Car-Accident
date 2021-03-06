import StringIO as io
import json
import time

# data = '{"filename":"results/result_00000002.jpg","tag":[{"person":32,"left":373,"right":515,"top":81,"bot":388},{"person":31,"left":439,"right":556,"top":65,"bot":384}]}'
# data = '{"filename":"results/result_00000056.jpg","tag":[{"car":28,"left":370,"right":719,"top":362,"bot":475}]}'

def same_Object(index,data1,data2,epsilon):

	# jsonData=json.loads(io.StringIO((data).decode("utf-8")))
	jsonData1 = json.loads(data1)
	jsonData2 = json.loads(data2)

	# print(jsonData['tag'])
	# print(len(jsonData['tag']))

	# Array of first Frame
	left_arr1 = []
	right_arr1 = []
	top_arr1 = []
	bot_arr1 = []

	# Array of second frame
	left_arr2 = []
	right_arr2 = []
	top_arr2 = []
	bot_arr2 = []

	# Updating Array of first Frame
	for i in xrange(len(jsonData1['tag'])):
		try:
		
			if(jsonData1['tag'][i]['car']):

				left_arr1 += [jsonData1['tag'][i]['left']]
				right_arr1 += [jsonData1['tag'][i]['right']]
				top_arr1 += [jsonData1['tag'][i]['top']]
				bot_arr1 += [jsonData1['tag'][i]['bot']]
				
				# print(jsonData['tag'][i])
		
		except:
			continue

	# Updating Array of second Frame
	for i in xrange(len(jsonData2['tag'])):
		try:
		
			if(jsonData2['tag'][i]['car']):

				left_arr2 += [jsonData2['tag'][i]['left']]
				right_arr2 += [jsonData2['tag'][i]['right']]
				top_arr2 += [jsonData2['tag'][i]['top']]
				bot_arr2 += [jsonData2['tag'][i]['bot']]
				
				# print(jsonData['tag'][i])
		
		except:
			continue


	for i in xrange(len(left_arr1)):
		for j in xrange(len(left_arr2)):

			b1 = abs(left_arr1[i] - left_arr2[j]) < epsilon
			b2 = abs(right_arr1[i] - right_arr2[j]) < epsilon
			b3 = abs(top_arr1[i] - top_arr2[j]) < epsilon
			b4 = abs(bot_arr1[i] - bot_arr2[j]) < epsilon

			if (b1 and b2 and b3 and b4):
				index += 1
				print index, ' :'
				print jsonData1['tag'][i]
				print jsonData1['tag'][i]

	return index

def club_Array(arr):

	j = 0

	for i in xrange((len(arr)-1)):
		temp1 = arr[j]
		temp2 = arr[j+1]
		if (temp2 - temp1) < 40 :
			arr.remove(temp1)
		else:
			j += 1

def track_Object(line_arr):

	index = 0

	for i in range(len(line_arr) - 1):
		print i
		
		index = same_Object(index,line_arr[i],line_arr[i+1],50)

	return


file = open('result.txt', 'r')

line_arr = []

for line in file:
	# check_Overlap(line)
	line_arr += [line]



# for i in xrange(len(line_arr)):
# 	# print i
# 	if check_Overlap(i,line_arr[i]):
# 		print i

track_Object(line_arr)