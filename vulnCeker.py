#!/usr/bin/env python2
#-*- coding: utf-8 -*-
__author__ = '-={InYourG00D feat Sultan}=-'
import requests, sys

def file_open(file_name):
    list = []
    file = open(file_name,"r")
    file_in = file.readlines()
    for value in file_in:
        if value not in " ":
            list.append(value.replace("\n", ""))
        else:
            pass
    file.close()
    return list

def checker(vuln_list):
    error_list = file_open("error.conf")
    sites = []
    value = False
    for vuln in vuln_list:
        sites.append(vuln+"'")
    for site in sites:
        try:
            request = requests.get(url=site.encode("UTF-8"))
            source_code = str(request.content)
            for error in error_list:
                if error in source_code:
                    value = True
                    break
                elif error not in source_code:
                    value = False
                    continue
            if value == True:
                print("[*] {} ==[> Vuln Found.".format(site))
            elif value == False:
                print("[-] {} ==[> Vuln Not Found.".format(site))
        except requests.ConnectionError:
            print("[!] {} ==[> Connection Error!".format(site))
    print("{}".format("#" *50))

def banner():
    banner = """{}
(\_____/)Sqli Vuln Checker
 (=°~°~) by:InYourG00DfeatSULTAN
(")___(")TEAM:S.T.C-LNX#CREW-BUFT
How To Use: \n \t python2 vulnCeker.py list
{}""".format("#"*50, "#"*50)
    return banner

if __name__ == "__main__":
    try:
        print(banner())
        target_file = file_open(sys.argv[1])
        checker(target_file)
        sys.exit()
    except IndexError:
        print("Tolong masukin list yg mau diChecker.\n")
        sys.exit()
    except KeyboardInterrupt:
        print("Tq Dah mampir :V\n")
        sys.exit()
