from business.cbs.cr0021 import CR0021
#借记卡状态查询
def test_cr0021():
    #1.实例化对象并从json模板文件中初始数据
    cd=CR0021()
    #2.按需修改初始化数据
    # cd.request.service_body.card_no='6217524515900001429'
    #3.调用接口
    response=cd.query()
    #4.检查点
    print(response.dumps())
    assert response.service_header.rsp_code=='000000'
    assert response.service_body.result_code =='00' 
    assert response.service_body.info[0].active =='Active' 


    