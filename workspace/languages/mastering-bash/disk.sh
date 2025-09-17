#!/bin/bash

echo "The total disk allocation for this system is: "
echo -e "\n"
df -H
echo -e "\n"
df -H | grep /$ | awk '{print "Space left on root partition: " $4}'
echo "The space left disk: ${disk_space}"
disk_space=$(df -H | grep /$ | awk '{print $4}')
echo "The space left disk: ${disk_space}"
