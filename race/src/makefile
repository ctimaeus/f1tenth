#!/bin/bash
race:
	. ~/race/devel/setup.bash

serial:
	make race && rosrun rosserial_python serial_node.py /dev/ttyACM0

lidar:
	make race && rosrun urg_node urg_node _ip_address:=192.168.0.10

control:
	make race && rosrun race control.py

dist:
	make race && rosrun race dist_finder.py

kill:
	make race && rosrun race kill.py

talker:
	make race && rosrun race talker.py
