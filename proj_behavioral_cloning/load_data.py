import csv
import cv2
def loadImages(data_dir, islinux = True):
	print('begin loading img from', data_dir)
	lines = []
	with open(data_dir + '/driving_log.csv') as csvfile:
		reader = csv.reader(csvfile)
		for line in reader:
			lines.append(line)

	images = []
	measurements = []
	for line in lines[1:]:
		# as the image is from windows, use \\ as separator
		measurement = float(line[3])
		measurements.append(measurement)

		# center 
		fullname = line[0]             
		if islinux: #linux
			filename = fullname.split('/')[-1]
		else: # windows
			filename = fullname.split('\\')[-1]
		current_path = data_dir + '/IMG/' + filename
		image = cv2.imread(current_path)
		images.append(image)

		#left camera
		measurements.append(measurement + 0.2)
		fullname = line[1]
		if islinux:
			filename = fullname.split('/')[-1]
		else:
			filename = fullname.split('\\')[-1]
		current_path = data_dir + '/IMG/' + filename
		image = cv2.imread(current_path) # data in BGR order
		images.append(image)

		#right camera
		measurements.append(measurement - 0.2)
		fullname = line[1]
		if islinux:
			filename = fullname.split('/')[-1]
		else:
			filename = fullname.split('\\')[-1]
		current_path = data_dir + '/IMG/' + filename
		image = cv2.imread(current_path)
		images.append(image)
	print('finished loading img from', data_dir)

	return images, measurements
