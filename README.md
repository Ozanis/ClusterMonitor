<h1>Description</h1>
Client-server service for collecting telemetry over TLS. Meaning CPU load, num of cores, RAM, HDD, boot tine, network using. Logging, multithreading and TLS-encryption are included

<h2>Related works</h2>

1. <a href = https://github.com/Ozanis/TelemetryAgent >C++ version</a>


</h2>Requirements</h2>

* Python 3.3-3.7 (3.7 convenient)
* OpenSSL and pyOpenSSL
* Psutil
* UFW
* SQL (in development state)
* Docker (in development also)

<h2>Content</h2>

* Client-side
* Server-side
* Bash-script for solving dependencies
* Bash daemon set-up


<h2>Comments</h2> 

1. You can run both applications as systemd services using provided bash script
2. Running server-side is possible using bash-script also.
3. Also provided simple UFW-controller to reject wrong connectors
4. Enabled push-notifications about critical processes
