from business.act.ac1002 import AC1002


def test_act_aps():
    #1.实例化对象并从json模板文件中初始数据
    act=AC1002()
    #2.按需修改初始化数据
    act.request.SERVICE.SERVICE_BODY.APPLICATION_NUMBER='202303131000012'
    #3.调用blaze接口
    response=act.query()
    #4.检查点
    assert response.SERVICE.SERVICE_HEADER.RSPCODE=='000000'

    print(response.dumps())
    # assert response.status_code==200
    # assert act.getproperty("ApplnMode")=="05"
    # assert True
    