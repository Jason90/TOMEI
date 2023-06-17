from business.act.ac1001 import AC1001


def test_act_risk():
    #1.实例化对象并从json模板文件中初始数据
    act=AC1001()
    #2.按需修改初始化数据
    act.request.SERVICE.SERVICE_BODY.APPLICATION_NUMBER='2023031310000131'
    #3.调用blaze接口
    response=act.query()
    #4.检查点
    assert response.SERVICE.SERVICE_HEADER.RSPCODE=='000000'

    print(response.dumps())
    # assert response.status_code==200
    # assert act.getproperty("ApplnMode")=="05"
    # assert True
    