from business.cbs.cd1001 import CD1001

def test_cd1001():
    #1.实例化对象并从json模板文件中初始数据
    cd=CD1001()
    #2.按需修改初始化数据
    cd.request.service.service_body.card_no='6259520600000063'
    #3.调用blaze接口
    response=cd.query()
    #4.检查点
    print(response.dumps())
    assert response.service.service_header.rsp_code=='000000'
    assert '新卡' in response.service.service_body.cust_name 
    print("CD1001接口自动化测试通过")
    