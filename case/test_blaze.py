from business.blaze import Blaze



def test_blaze():
    #1.实例化对象并从json模板文件中初始数据
    blaze=Blaze()
    #2.按需修改初始化数据
    blaze.data.sourceCode='stag1'
    #3.调用blaze接口
    response=blaze.query()
    #4.检查点
    #print(response.text)
    assert response.status_code==200
    assert blaze.getproperty("ApplnMode")=="05"
    assert True
    