from business.activate import Activate


def test_act_aps():
    #1.实例化对象并从json模板文件中初始数据
    activate=Activate()
    #2.按需修改初始化数据
    activate.data.SERVICE.SERVICE_BODY.APPLICATION_NUMBER='202303130000001'
    #3.调用blaze接口
    response=activate.aps()
    #4.检查点
    #print(response.text)
    assert response.status_code==200
    assert activate.getproperty("ApplnMode")=="05"
    assert True
    