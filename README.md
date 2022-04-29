# DATA 586 | Project | Log Anomaly Detection

Group Members:
- Anqi Li
- Evelyn Sugihermanto

## Files
- [EDA.ipynb](/docs/EDA.ipynb)
- [log_anomaly_report.pdf](/docs/log_anomaly_report.pdf)


## 1. Raw Log Data (HDFS_1)

The Raw data was too big to be uploaded to Github. So, we have attached a link to the original log file below. This raw data is supposed to be placed in the /parse/raw_data folder.
- HDFS_1: https://github.com/logpai/loghub/tree/master/HDFS

## 2. Parse Data


We adopt Drain and IPLoM (Iterative Partitioning Log Mining) from the open-source tool [Logparser]((https://github.com/logpai/logparser)) to parse the log messages into log keys and to compare their performance on the final detection accuracy. The script used to parse the model can be found below:
- [parser_drain.py](/parse/parser_drain.py)
- [parser_iplom.py](/parse/parser_iplom.py)

## 3. Process

After parsing the raw HDFS_1 log data, we split the parsed data into training and testing set. The script to split the data into training and testing set can be found below:
- [training_test_split.py](/parse/training_test_split.py)

Then we process the model using the TF-IDF along with the sliding window method to generate the numerical feature matrix. The script to process the model can be found below:
- [process.py](/process/process.py)

## 4. Model

We adopted a CNN model which is modified based on the classic LeNet-5 convolutional network [21] provided in lab3. In total, the model contains 6 layers. 2 out of these 6 layers are convolutional layers (C1, C3), which are connected by two maximum pooling layers (S2 & S4). The penultimate layer is a fully connected layer (F6), which is followed by the final output layer. The details are summarized below: 
-	The two convolutional layers are with 2x2 kernels, and are 16 and 32 filters respectively. 
-	The two max pooling layers are with 2x2 kernels. 
-	There are two MLP hidden layers with 120 and 84 nodes respectively. 
-	The whole network uses tanh sigmoid as activation function. 
-	The output layer uses softmax function with output labels representing normal and anomalous. 

The notebooks used to run the model can be found below:
- [CNN_LeNet5_drain.ipynb](/model/CNN_LeNet5_drain.ipynb)
- [CNN_LeNet5_iplom.ipynb](/model/CNN_LeNet5_iplom.ipynb)


## 5. Results

|     Parsing model    |     Dataset    |     Accuracy    |     Precision    |     Recall      |
|----------------------|----------------|-----------------|------------------|-----------------|
|     Drain            |     Train      |     0.999803    |     0.995558     |     0.998178    |
|                      |     Test       |     0.999900    |     1.0          |     0.993949    |
|     IPLoM            |     Train      |     0.999769    |     0.995329     |     0.997253    |
|                      |     Test       |     0.999925    |     1.0          |     0.995461    |


## Attributions
- https://github.com/logpai/loghub/tree/master/HDFS
- https://github.com/logpai/logparser

