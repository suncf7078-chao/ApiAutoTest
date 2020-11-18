'''
注册的测试脚本（pytest）
'''
import pytest
from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


# 注册失败
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def fail_data(request):
    return request.param


# 注册成功
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def fail_data1(request):
    return request.param


# 重复注册
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_repeat.yaml"))
def fail_data2(request):
    return request.param


# 注册失败
def test_register_fail(fail_data, url, baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")
    r = Member.register(url, baserequests, fail_data['casedata'])
    assert str(r.json()['msg']) == str(fail_data['expect']['msg'])
    assert str(r.json()['status']) == str(fail_data['expect']['status'])
    assert str(r.json()['code']) == str(fail_data['expect']['code'])


# 注册成功
def test_register_pass(fail_data1, url, db, baserequests):
    print(f"测试数据为：{fail_data1['casedata']}")
    print(f"预期结果为：{fail_data1['expect']}")
    phone = fail_data1['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserequests, fail_data1['casedata'])
    # #检查响应结果
    assert str(r.json()['msg']) == str(fail_data1['expect']['msg'])
    assert str(r.json()['status']) == str(fail_data1['expect']['status'])
    assert str(r.json()['code']) == str(fail_data1['expect']['code'])
    # 检查实际有没有注册成功
    r = Member.getList(url, baserequests)
    assert phone in r.text
    # 清理环境根据手机号删除注册用户
    DbOp.deleteUser(db, phone)


# 重复注册
def test_register_repeat(fail_data2, url, baserequests, db):
    print(f"测试数据为：{fail_data2['casedata']}")
    print(f"预期结果为：{fail_data2['expect']}")
    Member.register(url, baserequests, fail_data2['casedata'])
    r = Member.register(url, baserequests, fail_data2['casedata'])
    assert str(r.json()['msg']) == str(fail_data2['expect']['msg'])
    assert str(r.json()['status']) == str(fail_data2['expect']['status'])
    assert str(r.json()['code']) == str(fail_data2['expect']['code'])
    phone = fail_data2['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)