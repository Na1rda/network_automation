import paramiko
from getpass import getpass
import time

#ip = raw_input("Please enter your IP address: ")
username = raw_input("Introduceti username: ")
password = getpass()

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f=open("loopbacks")

for line in f:
    try:
        print "Se acceseaza hostul: " + line
        HOST=line.strip()
#        remote_conn_pre=paramiko.SSHClient()
#        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(HOST, port=22, username=username,
                                password=password,
                                look_for_keys=False, allow_agent=False)


        remote_conn = remote_conn_pre.invoke_shell()
        output = remote_conn.recv(65535)
        print output

        remote_conn.send("show ip int brief\n")
        time.sleep(.5)
        output = remote_conn.recv(65535)
        print output

        remote_conn.send("conf t\n")
        time.sleep(.5)
        output = remote_conn.recv(65535)
        print output

        remote_conn.send("end\n")
        time.sleep(.5)
        output = remote_conn.recv(65535)
        print output

        remote_conn.send("exit\n")
        time.sleep(.5)
        output = remote_conn.recv(65535)
        print output

    except:
        print("Hostul " + str(HOST) + " e down.")
