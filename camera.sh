#!/bin/bash
while :;
 do sudo python RPi_Camera.py;
 sudo rm capture/*;
 sudo rm capture/crop/*;
 sudo rm capture/clean/*;
 sleep 300;
 done
