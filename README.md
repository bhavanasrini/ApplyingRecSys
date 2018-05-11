# ApplyingRecSys to Education Based System

Collaborative Filtering
hadoop jar hadoop-streaming-2.6.0.jar  -D mapred.reduce.tasks=1 -input gs://bucketccol/UserPrograms.csv -output /outputCF1 -mapper mapper.py -reducer reducer.py


hadoop jar hadoop-streaming-2.6.0.jar  -D mapred.reduce.tasks=0 -input gs://bucketccol/outputCF1/part-00000 -output /outputCF2 -mapper mapper.py  


Content Based

hadoop jar hadoop-streaming-2.6.0.jar  -D mapred.reduce.tasks=1 -input gs://bucketccol/pro.csv -output /outputCB1 -mapper mapper.py -reducer reducer.py

hadoop jar hadoop-streaming-2.6.0.jar  -D mapred.reduce.tasks=1 -D mapred.map.tasks=3 -input gs://bucketccol/outputCB1/part-00000 -output /outputCB2 -mapper mapper.py -reducer reducer.py 


Final Phase
hadoop jar hadoop-streaming-2.6.0.jar  -D mapred.reduce.tasks=1 -input gs://bucketccol/outputCF1 -output /output -mapper mapper.py -reducer reducer.py
