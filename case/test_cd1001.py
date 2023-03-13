from business.cd1001 import CD1001

#todo: 目录结构增加cbs，或模块增加test_cbs_cd1001
def test_cds_cd1001():
    #1.实例化对象并从json模板文件中初始数据
    cd=CD1001()
    #2.按需修改初始化数据
    cd.data.service.service_body.card_no='62595280************'
    #3.调用blaze接口
    response=cd.query()
    #4.检查点
    #print(response.text)
    assert response.status_code==200
    assert cd.getproperty("ApplnMode")=="05"
    assert True
    