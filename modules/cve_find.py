#!/usr/bin/env python3
import shodan
import requests
import random
from bs4 import BeautifulSoup
import sys
from time import sleep


class Colors:
    OKBLUE = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


color_random = [Colors.CBLUE, Colors.CVIOLET, Colors.CWHITE, Colors.OKBLUE, Colors.CGREEN, Colors.WARNING,
                Colors.CRED, Colors.CBEIGE]
random.shuffle(color_random)


def entryy():
    x = color_random[0] + """
    ███████▀▀▀░░░░░░░▀▀▀███████
    ████▀░░░░░░░░░░░░░░░░░▀████
    ███│░░░░░░░░░░░░░░░░░░░│███
    ██▌│░░░░░░░░░░░░░░░░░░░│▐██
    ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
    ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
    ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
    ██▌░│██████▌░░░▐██████│░▐██
    ███░│▐███▀▀░░▄░░▀▀███▌│░███
    ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
    ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
    ████▄─┘██▌░░░░░░░▐██└─▄████
    █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
    ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
    █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████     CVE FIND TOOL
    ███████▄░░░░░░░░░░░▄███████   CODED BY TMRSWRR
    ██████████▄▄▄▄▄▄▄██████████    HAPPY HACKING                                                                   
\n"""

    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    oo = " " * 4 + 27 * "░█" + "\n\n"
    for c in oo:
        print(Colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    tt = " " * 4 + "█░" + " " * 13 + "WELCOME TO CVE-FIND TOOL" + " " * 13 + "█░" + "\n\n"
    for c in tt:
        print(Colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    xx = " " * 4 + 27 * "░█" + "\n\n"
    for c in xx:
        print(Colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)


def findCve():
    cc = "cve_list.txt"
    open(cc, 'w').close()
    apiKey = random.choice(open("key.txt").readlines()).replace('\n', '')
    api = shodan.Shodan(apiKey)
    target = input(Colors.CBLUE+"ex:targetsite.com\nPlease Enter target Url\t:")
    dnsResolve = ('https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + apiKey)
    try:
        resolved = requests.get(dnsResolve)
        hostIP = resolved.json()[target]
        host = api.host(hostIP)
        for item in host['vulns']:
            CVE = item.replace('!', '')
            print('Vulns: %s' % item, Colors.CBLUE)
            with open("aaa.txt", "a+") as f:
                f.write(CVE + "\n")
            exploits = api.exploits.search(CVE)
            for item in (exploits['matches']):
                if item.get('cve')[0] == CVE:
                    print(item.get('description'), Colors.CBEIGE)

    except Exception as err:
        print(err)


def exploitFind():
    try:
        with open("cve_list.txt", "r") as f:
            for i in f:
                aaa = i.rstrip("\n")
                for x in range(1, 2):
                    url = f"https://exploits.shodan.io/?q={aaa}&p={x}"
                    print(aaa)
                    headers_param = {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
                    r = requests.get(url, headers=headers_param)
                    s = BeautifulSoup(r.content, "lxml")
                    c = s.find_all("a", attrs={"class": "bold"})
                    count = 1
                    for j in c:
                        print(Colors.CRED + ">>>", Colors.OKBLUE + j["href"], Colors.CGREEN + j.text)
                        count += 1
    except:
        print("Please check the target!!!", Colors.CRED)


entryy()
findCve()
exploitFind()