import pytest
from lib.storage_lib import *
from lib.logger import *
from lib.connect import *
log=get_logger(__name__)
#@pytest.mark.usefixtures("setup")
def test_server_uptime1(setup):
    out=MainLib()

    log.info(out.get_server_uptime())
    assert True

def test_biosinfo(setup):
    out=MainLib()
    out1=out.get_biosinfo()
    if out1:
        assert True
        log.info("this is about biosinfo")
def test_usets(setup):
    out=MainLib()
    out1=out.get_users()
    if out1:
        assert True
        log.info("this is about users")

def test_partition(setup):
    out=MainLib()
    out2=out.create_partition("/dev/sdd","p","+10G")
    if out2:
        assert True
        log.info("this about create partition")