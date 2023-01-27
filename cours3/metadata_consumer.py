#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import MapMetaData
def callback(data):
#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	print ("resolution:",data.resolution,"width:",data.width,"height:",data.height,"Pose:",data.origin)    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("map_metadata", MapMetaData, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
