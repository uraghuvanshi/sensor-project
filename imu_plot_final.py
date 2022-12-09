# !usr/bin/python

# import rosbag
from bagpy import bagreader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
import time

#ENTER THE PATH TO YOUR ROSBAG BELOW
test_bag=bagreader('/home/uday/foxglove_long.bag')

imudata=test_bag.message_by_topic(topic="/sensors/odometry/imu/correction")
imuread=pd.read_csv(imudata)

#FOR TEST BAG
df=pd.DataFrame(imuread,columns=["Time","using_correction","imu_difference"]).astype(float)
finaltime=[]
for i in df["Time"]:
    finaltime.append(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(i-18000)))


# print(df["imu_difference"])
# print(len(df["using_correction"]))


#PLOTTING IMU_CORRECTION WITH TIME
plt.figure(1)
plt.suptitle("Plotting imu_correction with time",fontweight='bold')
plt.plot(finaltime,df["using_correction"],c='g'),plt.grid()
plt.xlabel('Time')
plt.ylabel("Imu correction")
plt.xticks([finaltime[0],finaltime[len(finaltime)//2],finaltime[len(finaltime)-1]])
plt.xticks(rotation=60)

#PLOTTING IMU_DIFFERENCE WITH TIME
plt.figure(2)
plt.suptitle("Plotting imu difference with time", fontweight='bold')
plt.plot(finaltime,df["imu_difference"],c='b'),plt.grid()
plt.xlabel('Time')
plt.ylabel("Imu difference")
plt.xticks([finaltime[0],finaltime[len(finaltime)//2],finaltime[len(finaltime)-1]])
plt.xticks(rotation=60)
plt.show()