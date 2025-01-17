
# İntikam21 Framework

<p align="center">
  <img src="https://github.com/Intikam21kurucu/intmages/blob/main/lv_0_20250104175232.gif" alt="Gitter chat">
</p>

 
![Supported OS](https://img.shields.io/badge/Supported%20OS-Linux-yellow.svg)
![License](https://img.shields.io/badge/license-BSL--1.0-blue.svg)
![FRAMEWORK SÜRÜMÜ](https://img.shields.io/badge/FRAMEWORK%20SÜRÜMÜ-İntikam21--Framework%20console%20v4.1.09--dev--bbf096e-green.svg)
 
![Python](https://img.shields.io/badge/Python-3-green.svg)
![Exploits](https://img.shields.io/badge/EXPLOIT-2456-red.svg)
![Build](https://img.shields.io/badge/BUILD-1079-red.svg)
![Modules](https://img.shields.io/badge/modules-589-red.svg) 

**We are editing this repo!**



İntikam21 hiçbir sorumluluğu kabul etmez yaptığınız hersey size ozgudur😀

-----------------------------------------------

 # Instructions

**Please do the following before running the program:**

**1.After terbuild.sh is finished:**

````
source ~/.bashrc
````

**2. If intframework has been added to /usr/opt/intframework /usr/opt, then:**

````
cd $PREFIX/opt/
mkdir -p intframework-termux
mv $PREFIX/opt/* $PREFIX/opt/intframework-termux
````

**3. Before running intconsole:**

````
cd $INTFRAMEWORK_PATH
mv inttable/inttable $PREFIX/lib/python3.12/
````

**4. If you want to use inttable:**

````
import inttable.inttable as inttable

inttable.core.activate("root")
inttable.console.run("command")
````



  
 

 


# EKRAN GÖRÜNTÜSÜ 

system photos:
![İntikam21 photos:](https://github.com/Intikam21kurucu/intframework/blob/d5cb19b49875d0eb9a949c379202999d5c609e22/Photos/IMG_20241008_184826.jpg) 

![Photo2](https://github.com/Intikam21kurucu/intframework/blob/%C4%B0ntframeworkV4/IMG_20241027_122034.jpg)
![Github Badge](https://github.com/Intikam21kurucu/intframework/blob/%C4%B0ntframeworkV4/IMG_20240916_191945.jpg)

# İNSTALL TERMUX
````apt update && apt upgrade
pkg update && pkg upgrade
pkg install python3
pkg install git
pip3 install requests
git clone https://github.com/intSpLoiT/intframework-termux
cd intframework-termux 

chmod +x terbuild.sh

./terbuild.sh
````










# Examples

```
int4 (modular) > use network_scan
[*] Module selected: network_scan
int4 module(network_scan) > show optiosn
[-] Invalid command. Type 'help' for available commands.
int4 module(network_scan) > show options
[*] Available options for module: network_scan
fs: None
timeout: None
int4 module(network_scan) > set timeout 0.1
[*] timeout = 0.1
int4 module(network_scan) > run
Network Scanner
IP Address    | Device Name        | Status
---------------------------------------------
192.168.5.1     | Network Scan       | Port Active, Ping Active, Subprocess Ping Successful, HTTP Active
192.168.5.3     | Unknown Device       | Inactive
192.168.5.5     | Unknown Device       | Inactive
192.168.5.6     | Unknown Device       | Inactive
192.168.5.8     | Unknown Device       | Inactive
192.168.5.4     | Unknown Device       | Inactive
192.168.5.7     | Unknown Device       | Inactive
192.168.5.11    | Unknown Device       | Inactive
192.168.5.10    | Unknown Device       | Inactive
192.168.5.2     | Unknown Device       | Inactive
192.168.5.9     | Unknown Device       | Inactive
192.168.5.12    | Unknown Device       | Inactive
192.168.5.13    | Unknown Device       | Inactive
192.168.5.14    | Unknown Device       | Inactive
192.168.5.15    | Unknown Device       | Inactive
192.168.5.16    | Unknown Device       | Inactive
192.168.5.17    | Unknown Device       | Inactive
192.168.5.18    | Unknown Device       | Inactive
192.168.5.19    | Unknown Device       | Inactive
192.168.5.20    | Unknown Device       | Inactive
192.168.5.21    | Unknown Device       | Inactive
192.168.5.22    | Unknown Device       | Inactive
192.168.5.23    | Unknown Device       | Inactive
192.168.5.24    | Unknown Device       | Inactive
```
**using inthandler**
```
int4 (exploiter) > use multi/handler
Exploit 'multi/handler' selected.
int4 exploit(multi/handler) > run
python: can't open file '/storage/emulated/0/intframework/modules/exploits/multi.handler': [Errno 2] No such file or directory
int4 exploit(multi/handler) > back
int4 exploit(multi/handler) > reset
Options for multi/handler reset to default.
int4 exploit(multi/handler) > run
Exploit file is not defined for this exploit.
int4 exploit(multi/handler) > set FILENAME multi/handler/inthandler.py
FILENAME set to multi/handler/inthandler.py.
int4 exploit(multi/handler) > run
Listening on 0.0.0.0:4444
Connection from ('127.0.0.1', 34170)
İntShell > Connection from ('127.0.0.1', 34172)
h
İntShell > GET / HTTP/1.1
Host: 0.0.0.0:4444
Connection: keep-alive
Accept-Language: ******
Upgrade-Insecure-Requests: 1
User-Agent: anonymous
Referer: android-app://com.google.android.googlequicksearchbox/
Accept-Encoding: gzip, deflate


İntShell >
```



