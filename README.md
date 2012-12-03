Tethr
=====

Connecting Communities

Warnings
--------

#### This is the first release and is not well documented or tested. Don't hesitate to submit issues on the github tracker!
#### Let us know on the tracker if you have suggestions!  

What is Tethr
--------------

### Overview

Tethr connects community members with low-cost appropriate and open technology, link them to the global Internet in multiple cost-effective ways and brings apps to places where always-on is not yet an option.

### How does it work?

#### Local Networks
Tethr deploys local networks that can be accessed not only by wifi but also through standard mobile technologies. This means that any cell phone or connected device user can connect and communicate with other members of the local network. Since it's private and local infrastructure it doesn't depend on commercial providers, in other words : it's free to use.

#### Multi-channel Internet Uplink  
Tethr can connect to the Internet in more ways than any existing device on the market, but more importantly it connects in ways that are locally relevant and cost-effective. Tethr helps communities connect to the global network only when it makes sense.

#### Applications
Tethr supports all the applications the connected world uses and love. From instant communication to real-time collaboration, mapping to browsing, file sharing to blogging : it's all there always-locally-on and ready to be synchronized with the Cloud.

Features
--------

### Networking

TODO

### Tethr Applications
Tethr currently implements the following features:
* File Sharing : Connect to Tethr in your browser, drag and drop multiple files and start uploading. Tethr will make sure your files are securely synchronised to the cloud as soon as it sees an Internet connection.
* Manager : Monitor the Tethr box's vital functions.

Dependencies
------------

* Python 2.7
* virtualenv
* nginx
* uwsgi
* Flask
* pirsyncd

Tethr also synchronises to a cloud based rsync over ssh daemon.

Installation
------------

* apt-get install nginx uwsgi-plugin-python uwsgi-plugin-http uwsgi-core python-pip python-flask python-virtualenv
* virtualenv /var/tethr/venv
* mkdir /var/log/tethr
* Add the ssh key to the rsync destination 'authorized_keys' file
* /var/tethr/managr/scripts/pirsyncd # start the Tethr file synchronisation script

Testing
-------

* http://tethr.local # try uploading a file.
* http://tethr.local/managr # clicking on all links should bring results.
* /var/tethr/managr/scripts/pirsyncd -k status # check the status of the file synchronisation daemon

