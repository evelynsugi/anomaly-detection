# count rows
with open('raw_data/HDFS.log', "r") as file:
    nrow=0
    for line in file:
        nrow += 1

# Set the ratio 80/20
train_index = int(nrow*.8)

# For training set
# read the first 80% lines
trainset = []
with open('raw_data/HDFS.log', "r") as file:
    n=0
    for line in file:
        if n < train_index:
            trainset.append(line)
            n += 1
        else: break 

# write to the training file `HDFS_train.log`
with open('raw_data/HDFS_trainset.log', 'x') as file:
    for i in trainset:
        file.write(i)
        
# For test set
# read the last 20% lines
testset = []
with open('raw_data/HDFS.log', "r") as file:
    n=0
    for line in file:
        n += 1
        if n >= train_index:
            testset.append(line)
# write to the test file `HDFS_test.log`
with open('raw_data/HDFS_testset.log', 'x') as file:
    for i in testset:
        file.write(i)