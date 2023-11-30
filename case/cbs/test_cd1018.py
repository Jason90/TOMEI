from business.cbs.cd1018 import CD1018

def test_cd1018():
    #1.实例化对象并从json模板文件中初始数据
    cd=CD1018()
    #2.按需修改初始化数据
    cd.request.service.service_body.card_no='6259520600000063'
    #3.调用接口
    response=cd.query()
    #4.检查点
    assert response.service.service_header.rsp_code=='000000'
    assert response.service.service_body.cvv2 !='' 
    print(response.dumps())

    