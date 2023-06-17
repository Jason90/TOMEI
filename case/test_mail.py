from business.mail import Mail

def test_sendmail():
    #1.实例化对象并从json模板文件中初始数据
    mail=Mail()
    #2.按需修改初始化数据
    print(mail.request.mail.title)
    mail.request.mail.title="new title"
    mail.request.mail.to[0].name="Wenzi"
    #3.执行发送邮件等业务逻辑
    result=mail.send()
    #4.检查点
    assert result