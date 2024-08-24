import paramiko
import pytest
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from lib.connect import exec_cmd
from lib.logger import *
from lib.storage_lib import MainLib


log=get_logger(__name__)
sys.path.insert(0,'C:\\python\\pycharm\\framework\\lib')

#sys.path.append(dirname(dirname(abspath(__file__))))

@pytest.fixture(scope="class",autouse=True)
def setup():
    log.info("before connected the server")
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("192.168.0.106", username="winteck", password="Winteck@2024")


    # obj=MainLib()
    # log.info("this is before test")
    #drive_list=obj.get_drives()
    #log.info(f"drives list before test are {drive_list}")
    yield client
    log.info("cleanup")
    log.info("after test execution")
    client.close()
    #drive_list=obj.get_drives()
    #log.info(f"drives list before test are {drive_list}")


