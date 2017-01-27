#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>ADB Self Service Console Report"
echo "</title></head><body>"

##echo "<h1>General system information for host: $(hostname -s)</h1>"
echo "<h1>General system information for host: $(hostname)</h1>"
##echo ""

echo "<h1>Memory Info</h1>"
echo "<pre> $(free -m) </pre>"

echo "<h1>Disk Info:</h1>"
echo "<pre> $(df -h) </pre>"

echo "<h1>Logged in user</h1>"
echo "<pre> $(w) </pre>"

echo "<h1>List Directory: </h1>"

echo "<h.05> /mnt directory</h0.5>"
echo "<pre> $(ls -l /mnt) </pre>"

echo "<h.05> /home directory</h0.5>"
echo "<pre> $(ls -l /home) </pre>"

echo "<h.05> /tmp directory</h0.5>"
echo "<pre> $(ls -lR /tmp) </pre>"

echo "<center>Information generated on $(date)</center>"
echo "</body></html>"
