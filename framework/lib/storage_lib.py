"""
*************************************************************************
@Purpose :: This module is an API to connect remote Linux host and get the repsonse

@Author         ::

@revision History

@DATE [ DD/MM/YYYY]               @Name                   @Remarks

30-10-2022                       winteck                 Adding New modules for testing product
"""
import re
import sys
from os.path import dirname, abspath
from lib import logger
from lib.connect import exec_cmd

sys.path.append(dirname(dirname(abspath(__file__))))

log = logger.get_logger(__name__)


class MainLib:
    def _init_(self):
        pass
    def get_server_uptime(self):
        """
        This method is used to get all the drives list
        :return:
        """
        server_uptime = exec_cmd("uptime")
        return server_uptime
    def get_cpuinfo(self):
        cpuinfo=exec_cmd("lscpu")
        match_cpu=re.search("Model name:\s+(.*)",cpuinfo)
        if match_cpu:
            return match_cpu.group(1)

    def get_biosinfo(self):
        biosinfo=exec_cmd("dmidecode -t bios")
        out=re.search("\s+Version:\s+([0-9]{1}\.[0-9]{1}\.[0-9]{1})",biosinfo)
        if out:
            return out.group(1)
    def get_users(self):
        userinfo=exec_cmd("users")
        return userinfo
    def raid_create(self):
        userinfo=exec_cmd("mdadm --create /dev/md5 --level=1 --raid-devices=2 /dev/sdb /dev/sdc")
        if userinfo:
            print('raid created successfully')
    def get_drives(self):
        drives=exec_cmd("lsblk")
        drivelist=re.findall("sd[a-z]{1}",drives)
        list=[]
        for i in drivelist:
            #print(i)
            list.append(f"/dev/{i}")
        return list
    def get_servercompany(self):
        servername=exec_cmd("dmidecode -t chassis")
        out=re.search('\s+M[a-z]+:\s+(.+)',servername)
        if out:
            return out.group(1)
    def get_memoryofchip(self):
        mem=exec_cmd("dmideode -t memory")
        out=re.serach('\s+Size:\s+([0-9]{1}\s+[A-Z]{2})$',mem)
        if out:
            return out.group(1)
    def get_drivefw(self,drive_name):
        fw=exec_cmd(f"smartctl -a {drive_name}")
        out=re.search("Revision:\s+(.+)",fw)
        if out:
            return out.group(1)
    def create_partition(self,drive_name,partition_type,size):
        partition=exec_cmd(f"echo -e 'n\n{partition_type}\n\n\n{size}\nw\n' | fdisk {drive_name}")
        if partition:
            return "success"


    def create_raid(self,raidname,raid_level,no_of_drives,*drive):
        create=exec_cmd(f"mdadm --create {raidname} --level={raid_level} --raid-devices={no_of_drives} {drive}")
        if create:
            print("sucess")
        else:
            print("unsucessful")


    def check_raid(self,raidname):
        check=exec_cmd(f"mdadm --details {raidname}")
        out=exec_cmd("lsblk")
        out1= re.search("md0",out)
        if out1:
            return "raid created"
        else:
            print("raid is not there")
            return False

    def get_pci(self):
        pci=exec_cmd("lspci")
        out=re.search('.+Host\s+[a-z]*\:(.+)',pci)
        if out:
            return out.group(1).strip()
    def get_ip(self):
        ip=exec_cmd("ifconfig")
        out=re.search("\s+inet+\s(\d{3}\.\d{3}\.\d*\.\d*)",ip)
        if out:

            print("this is ipaddress")
            return out.group(1)
    def drive_capacity(self,drive_name):
        capacity=exec_cmd(f"lsblk {drive_name}")
        out=re.search('[a-z]{3}.+([0-9]{3}\.[0-9]*G)',capacity)
        if out:
            return out.group(1)
    def check_fio(self,name,drivename,arg,size,num,enginename,time):
        performance=exec_cmd(f"fio --name={name} --filename={drivename} --rw={arg} --blocksize={size} --iodepth={num} --ioengine={enginename}"
                             f"--runtime={time}")
        out=re.search("r.+IOPS=([0-9]{3}k)",performance)
        if out:
            print('performance is done')
            return True
        else:
            return False


if __name__=='__main__':
    obj1 = MainLib()
    #print(obj1.get_server_uptime())

    #print(obj1.get_cpuinfo())

    #print(obj1.get_biosinfo())

    #print(obj1.get_drives())




    #print(obj1.get_servercompany())

    #print(obj1.get_drivefw())

    #print(obj1.create_partition("/dev/sdd","p","+10G"))
    #print(obj1.create_raid("/dev/md2",1,2,"/dev/sdc","/dev/sdd"))

    #print(obj1.get_ip())
    #print(obj1.check_raid("/dev/md0"))
    #print(obj1.get_pci())
    #print(obj1.drive_capacity("/dev/sdd"))
    print(obj1.check_fio('file1','/dev/sdd','read','4kb',32,'libaio','1m'))