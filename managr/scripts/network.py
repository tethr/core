__author__ = "Samuel Carlisle"
__copyright__ = "Copyright 2012"
__credits__ = ["Samuel Carlisle"]
__license__ = "GPL Affero"
__version__ = "3"
__maintainer__ = "Samuel Carlisle"
__email__ = "samuelcarlisle@gmail.com"
__status__ = "Development"

'''
 _____    _   _          
|_   _|  | | | |         
  | | ___| |_| |__  _ __ 
  | |/ _ \ __| '_ \| '__|
  | |  __/ |_| | | | |   
  \_/\___|\__|_| |_|_|   


This file is part of Tether.

network.py is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

network.py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Affero Public License
along with network.py.  If not, see <http://www.gnu.org/licenses/>.
'''
import os
import urllib2

"""Run a command and capture it's output string, error string and exit status"""
class Command(object):
    def __init__(self, command):
        self.command = command

    def run(self, shell=True):
        import subprocess as sp
        process = sp.Popen(self.command, shell = shell, stdout = sp.PIPE, stderr = sp.PIPE)
        self.pid = process.pid
        self.output, self.error = process.communicate()
        self.failed = process.returncode
        return self

    @property
    def returncode(self):
        return self.failed

def dbusWifi():
    return 

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.113.99',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

'''
def ping():
	os.system("")
'''
route = Command("route").run()
ifconfig = Command("ifconfig").run()
ping = Command("ping 8.8.8.8 -c5").run()
online = internet_on()

print "Content-Type: text/html"
print
print """\
<html>
<head><title>Route, Ifconfig and Ping</title></head>

<body>
"""
print "<h2>route</h2>"
print "<br>"
print route.output
print "<br>"
print "<h2>ifconfig</h2>"
print "<br>"
print ifconfig.output
print "<br>"
print "<h2>ping</h2>"
print "<br>"
print ping.output
print "<br>"
print "<h2>online</h2>"
print "<br>"
print ("Is the system connected to the internet? %s" % online)
print "</body>"
print "</html>"