'''
import subprocess
result = subprocess.call(["ssh", "admin123@127.0.0.1", "ls"])
'''
import paramiko
filename="abc.txt"
def getUsage(filename):
    with open(filename, 'r') as my_file:
        r = my_file.read()
        ret = r.split()

    ip=ret[0]
    port=2025
    username=ret[1]
    password=ret[2]


    cmd="top -b -n 1 | grep " + ret[3]
    #cmd="uptime"

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)

    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    return resp

if __name__ == '__main__':
    result = getUsage(filename)
    print result
