import threading, paramiko
import sys
import os
 
class ssh:
    shell = None
    client = None
    transport = None
 
    def __init__(self, address, username, password):
        print("Connecting to server on ip", str(address) + ".")
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)
        self.transport = paramiko.Transport((address, 22))
        self.transport.connect(username=username, password=password)
 
        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()
 
    def closeConnection(self):
        if(self.client != None):
            self.client.close()
            self.transport.close()
 
    def openShell(self):
        self.shell = self.client.invoke_shell()
 
    def sendShell(self, command):
        if(self.shell):
            self.shell.send(command + "\n")
        else:
            print("Shell not opened.")
 
    def process(self):
        global connection
        while True:
            # Print data when available
            if self.shell != None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)
                strdata = str(alldata, "utf8")
                strdata.replace('\r', '')
                print(strdata, end = "")
                if(strdata.endswith("$ ")):
                    print("\n$ ", end = "")

sshUsername = "student"
sshPassword = "caesar"
sshServer = "65.0.124.36"
k=int(input())

connection = ssh(sshServer, sshUsername, sshPassword)
connection.openShell()
connection.sendShell('Cryvengers')
os.system("sleep 1")
connection.sendShell('Cryvengers@pkm')
os.system("sleep 1")
connection.sendShell('5')
os.system("sleep 1")
connection.sendShell('go')
os.system("sleep 1")
connection.sendShell('wave')
os.system("sleep 1")
connection.sendShell('dive')
os.system("sleep 1")
connection.sendShell('go')
os.system("sleep 1")
connection.sendShell('read')
os.system("sleep 0.5")
text = "gsjgktipfolqgfmq"
pvals=[]
for i in range(0,8):
    for j in range(0,16):
        pvals.append(chr(i+ord("f"))+chr(j+ord("f")))
if(k!=0):
    fptr1=open("ipassword1.txt")
    p1=fptr1.readline()
else:
    p1=""

for i in pvals:
    inp=p1+i
    connection.sendShell(inp)
    os.system("sleep 0.5")
    connection.sendShell('c')
    os.system("sleep 0.5")
#while True:
 #   command = input('$ ')
 #   if command.startswith(" "):
 #       command = command[1:]
 #   if command == 'exit':
 #       connection.sendShell('quit')
 #       break
 #   connection.sendShell(command)
connection.closeConnection()
