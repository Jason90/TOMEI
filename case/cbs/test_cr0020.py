from business.cbs.cr0020 import CR0020

def test_cr0020():
    #1.实例化对象并从json模板文件中初始数据
    cd=CR0020()
    #2.按需修改初始化数据
    cd.request.service_body.card_no='6259528085002611'
    #3.调用接口
    response=cd.query()
    #4.检查点
    assert response.service_header.rsp_code=='000000'
    assert response.service_body.cvv2 !='' 
    print(response.dumps())

    