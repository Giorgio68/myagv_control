#!/usr/local/bin/python3
# (c) Giorgio Salvemini 2024

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

pub = None
lidar_data = None

def callback(data): # get lidar data
  global lidar_data
  lidar_data = data.data
  
  return

def get_dir() -> int:
  global lidar_data
  
  return NotImplementedError

def publish_mov(x: float, y: float, theta: float) -> None:
  global pub
  
  twist = Twist()
  twist.linear.x = x; 
  twist.linear.y = y; 
  twist.linear.z = 0
  twist.angular.x = 0; 
  twist.angular.y = 0; 
  twist.angular.z = theta
  pub.publish(twist)
  
  return

def main():
  global pub
  rospy.init_node('myagv_teleop')
  pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
  rospy.Subscriber('ydlidar', String, callback)

  print(msg)

  try:
    while True:
      cmd = get_dir()
      if cmd == 0: # stop
        publish_mov(0, 0, 0)
      elif cmd == 1: # forward
        publish_mov(0.5, 0, 0)
      elif cmd == 2: # backward
        publish_mov(-0.5, 0, 0)
      elif cmd == 3: # left
        publish_mov(0, 0.5, 0)
      elif cmd == 4: # right
        publish_mov(0, -0.5, 0)
      elif cmd == 5: # left-revolve
        publish_mov(0, 0, 0.5)
      elif cmd == 6: # right-revolve
        publish_mov(0, 0, -0.5)

    except KeyboardInterrupt:
        print('Received CRTL-C, quitting...')

    finally:
        publish_mov(0, 0, 0)

if __name__ == '__main__':
    main()