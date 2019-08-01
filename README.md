<h1>Description</h1>
Client-server service for collecting telemetry over TLS. Meaning CPU load, num of cores, RAM, HDD. Logging and TLS-encryption included

<h2>Related works</h>

1. <a href = https://github.com/Ozanis/TelemetryAgent >C++ version</a>
2. <a href = https://github.com/Ozanis/LinuxNetworkDiagnostic> LinuxNetworkDiagnostic </a>


</h2>Requirements</h2>

* Python 3.3-3.7 (3.7 convenient)
* OpenSSL
* Psutil
* PyQT(5)

<h2>Content</h2>

* Client-side
* Server-side
* Bash-script for solving dependencies
* Bash daemon set-up
* PyQT wrapper setup interface 

<h2>Comments</h2> 

1. You can run both applications as systemd services using provided bash script
2. Running server-side is possible using bash-script also.