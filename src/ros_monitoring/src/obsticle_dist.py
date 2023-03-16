#!/usr/bin/env python3
import rospy
import sys
import json
import yaml
import websocket
from threading import *
from rospy_message_converter import message_converter
from monitor.msg import *
from std_msgs.msg import String

ws_lock = Lock()
dict_msgs = {}
from std_msgs.msg import String

pubtf = rospy.Publisher(name = 'tf', data_class = String, latch = True, queue_size = 1000)
def callbacktf(data):
	global ws, ws_lock
	rospy.loginfo('monitor has observed: ' + str(data))
	dict = message_converter.convert_ros_message_to_dictionary(data)
	dict['topic'] = 'tf'
	dict['time'] = rospy.get_time()
	ws_lock.acquire()
	while dict['time'] in dict_msgs:
		dict['time'] += 0.01
	ws.send(json.dumps(dict))
	dict_msgs[dict['time']] = data
	ws_lock.release()
	rospy.loginfo('event propagated to oracle')
pub_dict = { 'tf' : pubtf}
msg_dict = { 'tf' : "std_msgs/String"}
def monitor():
	global pub_error, pub_verdict
	with open(log, 'w') as log_file:
		log_file.write('')
	rospy.init_node('obsticle_dist', anonymous=True)
	pub_error = rospy.Publisher(name = 'obsticle_dist/monitor_error', data_class = MonitorError, latch = True, queue_size = 1000)
	pub_verdict = rospy.Publisher(name = 'obsticle_dist/monitor_verdict', data_class = String, latch = True, queue_size = 1000)
	rospy.Subscriber('tf_mon', String, callbacktf)
	rospy.loginfo('monitor started and ready')
def on_message(ws, message):
	global error, log, actions
	json_dict = json.loads(message)
	if json_dict['verdict'] == 'true' or json_dict['verdict'] == 'currently_true' or json_dict['verdict'] == 'unknown':
		if json_dict['verdict'] == 'true' and not pub_dict:
			rospy.loginfo('The monitor concluded the satisfaction of the property under analysis, and can be safely removed.')
			ws.close()
			exit(0)
		else:
			logging(json_dict)
			topic = json_dict['topic']
			rospy.loginfo('The event ' + message + ' is consistent and republished')
			if topic in pub_dict:
				pub_dict[topic].publish(dict_msgs[json_dict['time']])
			del dict_msgs[json_dict['time']]
	else:
		logging(json_dict)
		if (json_dict['verdict'] == 'false' and actions[json_dict['topic']][1] >= 1) or (json_dict['verdict'] == 'currently_false' and actions[json_dict['topic']][1] == 1):
			rospy.loginfo('The event ' + message + ' is inconsistent..')
			error = MonitorError()
			error.topic = json_dict['topic']
			error.time = json_dict['time']
			error.property = json_dict['spec']
			error.content = str(dict_msgs[json_dict['time']])
			pub_error.publish(error)
			if json_dict['verdict'] == 'false' and not pub_dict:
				rospy.loginfo('The monitor concluded the violation of the property under analysis, and can be safely removed.')
				ws.close()
				exit(0)
		if actions[json_dict['topic']][0] != 'filter':
			if json_dict['verdict'] == 'currently_false':
				rospy.loginfo('The event ' + message + ' is consistent ')
			topic = json_dict['topic']
			if topic in pub_dict:
				pub_dict[topic].publish(dict_msgs[json_dict['time']])
			del dict_msgs[json_dict['time']]
		error = True
	pub_verdict.publish(json_dict['verdict'])

def on_error(ws, error):
	rospy.loginfo(error)

def on_close(ws):
	rospy.loginfo('### websocket closed ###')

def on_open(ws):
	rospy.loginfo('### websocket is open ###')

def logging(json_dict):
	try:
		with open(log, 'a+') as log_file:
			log_file.write(json.dumps(json_dict) + '\n')
		rospy.loginfo('event logged')
	except:
		rospy.loginfo('Unable to log the event.')

def main(argv):
	global log, actions, ws
	log = 'home/user/curiosity_mars_rover_ws/log_files/obsticle_dist.txt' 
	actions = {
		'tf' : ('filter', 1)
	}
	monitor()
	websocket.enableTrace(False)
	ws = websocket.WebSocketApp(
		'ws://127.0.0.1:9090',
		on_message = on_message,
            
		on_error = on_error,
		on_close = on_close,
		on_open = on_open)
	ws.run_forever()

if __name__ == '__main__':
	main(sys.argv)