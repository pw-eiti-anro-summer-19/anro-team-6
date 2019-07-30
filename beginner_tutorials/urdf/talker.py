#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import math
from sensor_msgs.msg import JointState

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_intorpolation', anonymous=True)
    hz = 10
    rate = rospy.Rate(hz) # 10hz
    d = 0.0
    theta1 = 1.5
    theta2 = 0.5
    theta3 = 1.2
    time = 5
    movement_calc = time * hz
    theta1_tmp = 0
    theta2_tmp = 0
    theta3_tmp = 0

    theta1_inc = theta1/movement_calc
    theta2_inc = theta2/movement_calc
    theta3_inc = theta3/movement_calc
    while movement_calc>0:
	theta1_tmp = theta1_tmp + theta1_inc
        theta2_tmp= theta2_tmp + theta2_inc
        theta3_tmp = theta3_tmp + theta3_inc
        msg = JointState()
        msg.header.stamp = rospy.get_rostime()
        msg.name = ['joint_0', 'joint_1', 'joint_2']
        msg.position = [theta1_tmp,theta2_tmp,theta3_tmp]
        pub.publish(msg)
        rate.sleep()
        movement_calc = movement_calc - 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

