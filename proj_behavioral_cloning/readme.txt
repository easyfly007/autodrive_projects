data
	all the training data provided udacity
data1_recover
	add the recover train data
data1_recover2
	add more recover train data
data2_track2
	data from track2
data1_recover3
	add more recover train data
data1_recover4
	add more recover train data

model_1.h5
	training using data, 5 epoches
loss:
train loss	val loss
0.0375		0.0378
0.0364		0.0373
0.0362		0.0367
0.0360		0.0368
0.0359		0.0369

model_2.h5
	training using data + data1_recover, 3 epoches
model_3.h5
	training using data + data1_recover + data1_recover2, 3 epoches
model_4.h5
	training using data + data1_recover + data1_recover2 + data2_track2, 3 epoches
model_5.h5
	training using data + data1_recover + data1_recover2, 3 epoches, left/right adjust 0.25
model_6.h5
	training using data + data1_recover *2 + data1_recover2 *2 + data1_recover3 *2
model_7.h5
	training using data + data1_recover4*2, epoches = 3, left/right adjust = 0.2


