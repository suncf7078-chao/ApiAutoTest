"""
登录
"""
import pytest
from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


# 登录成功
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data1(request):
    return request.param


# 测试前置和后置
@pytest.fixture()
def register(setup_data, url, baserequests, db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除
    DbOp.deleteUser(db, phone)


def test_login(login_data1, url, baserequests,register):
    print(f"测试数据为：{login_data1['casedata']}")
    print(f"预期结果为：{login_data1['expect']}")
    r = Member.login(url, baserequests, login_data1['casedata'])
    assert str(r.json()['msg']) == str(login_data1['expect']['msg'])
    assert str(r.json()['status']) == str(login_data1['expect']['status'])
    assert str(r.json()['code']) == str(login_data1['expect']['code'])
