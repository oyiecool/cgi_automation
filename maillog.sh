#!/bin/sh
#this captures the mails as executed by ec2 

tail -f /var/log/maillog | grep "rtomimbang.contractor@adb.org" >> /tmp/contractor.txt
