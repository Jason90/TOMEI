import pytest as pytest

from business.blz.blaze import Blaze
from util import sqlutil


@pytest.mark.parametrize(
    "tel_status, tel_status_msg",
    [
        ("1", "正常使用"),
        ("2", "停机"),
        ("3", "在网但不可用"),
        ("4", "在网（已销号）"),
        ("-1", "已查无数据"),
        ("-2", "查询异常"),
        ("111", ""),  # 长度超过限制
        # (1, ""),  # 类型错误
        # (None, ""),  # 空值
        ("", ""),  # 空值
        ("5", ""),  # 枚举值之外的值

    ])
def test_blaze_gtz_mobile_detail_mobile_stat(tel_status, tel_status_msg):
    # 1.实例化对象并从json模板文件中初始数据
    blaze = Blaze()
    # 2.按需修改初始化数据
    # blaze.request.applicationNumber = '202403181109931'
    # todo:xml soap标签无法通过对象属性方式访问
    # blaze.request.Envelope.Body.Query.applicationNumber ='202403181109931'
    blaze.request["soap:Envelope"]["soap:Body"]["Query"]["applicationNumber"] = "202403201109942"
    print(blaze.request)

    PostGreSqlUtils = sqlutil.PostGreSqlUtils()
    sql1 = "UPDATE t_dc_mobile_stat SET tel_status_msg = '" + tel_status_msg + "', tel_status= '" + tel_status + "' WHERE pid ='2024032014100551'"
    PostGreSqlUtils.execute_sql(sql1, tel_status, tel_status_msg)

    # 3.调用blaze接口
    response = blaze.query()
    # 4.检查点
    assert blaze.res.status_code == 200, 'Blaze接口通信正常'
    assert blaze.has_element("Applicant"), 'Blaze响应缺少申请人节点'
    # assert blaze.has_element("CustomerAmt"),'Blaze响应缺少客户额度信息'
    assert blaze.has_element("CustomerAmt"), 'Blaze响应缺少客户额度信息'
    assert blaze.has_element("JBXDetail"), 'Blaze响应缺少金宝信'
    # assert blaze.has_element("DiaryNotes"),'Blaze响应缺少日志信息'
    assert blaze.has_element("RelatedPerson"), 'Blaze响应缺少联系人信息'
    assert blaze.has_element("FICODetail"), 'Blaze响应缺少Fico评分'
    assert blaze.has_element("WhiteList"), 'Blaze响应缺少白名单'
    # assert blaze.has_element("PurchaseRetail"),'Blaze响应缺少零售信息'
    assert blaze.has_element("GZTEduDetail"), 'Blaze响应缺少学历信息'
    assert blaze.has_element("Instinct"), 'Blaze响应缺少反欺诈信息'
    assert blaze.has_element("PRIDetail"), 'Blaze响应缺少内评信息'

    assert blaze.has_element("GZTMobileDetail"), 'Blaze响应缺少手机在网信息'
    assert blaze.get_property("NewTelstatus") == tel_status, 'Blaze响应值不正确'

    assert blaze.has_element("TheFirstCheckDetail"), 'Blaze响应缺少征信衍生信息'
    # assert blaze.has_element("UnionpayDetail"),'Blaze响应缺少银联卡校验信息'
    assert blaze.has_element("InviteCustomerDetail"), 'Blaze响应缺少邀约办卡'
    # assert blaze.has_element("PAIEstimateDetail"), 'Blaze响应缺少消费能力'!!!!!!
    # assert blaze.has_element("MeiTuanDetail"),'Blaze响应缺少美团信息'
    # assert blaze.has_element("Vehicles"),'Blaze响应缺少汽车信息'
    # assert blaze.has_element("VehicleParking"),'Blaze响应缺少汽车信息'
    # assert blaze.has_element("VehicleDetails"),'Blaze响应缺少汽车信息'
    # assert blaze.has_element("VehicleMortgageLoan"),'Blaze响应缺少汽车信息'
    assert blaze.has_element("CRMRetail"), 'Blaze响应缺少存款信息'
    # assert blaze.has_element("ShareHolder"),'Blaze响应缺少法人信息'
    # assert blaze.has_element("Enterprise"),'Blaze响应缺少企业信息'
    assert blaze.has_element("InterfaceInfo"), 'Blaze响应缺少接口调用信息'
    assert blaze.has_element("WholeImage"), 'Blaze响应缺少影像资料信息'
    # assert blaze.has_element("HrbSecInsurance"),'Blaze响应缺少社保信息'
    assert blaze.has_element("BaiRongDetail"), 'Blaze响应缺少百融信息'
    # assert blaze.has_element("ExistCardHolderApp"),'Blaze响应缺少已持卡信息'
    # assert blaze.has_element("RelPersonExistCardHolderApp"),'Blaze响应缺少附属卡信息'
    assert blaze.has_element("PbocReport "), 'Blaze响应缺少人行信息'
    assert blaze.has_element("RelPersonPbocReport"), 'Blaze响应缺少附属卡\关联人\担保人人行信息'
    assert blaze.has_element("HRBBOutput"), 'Blaze响应缺少输出结果集'
    assert blaze.has_element("Strategy"), 'Blaze响应缺少策略随机数'

    assert blaze.get_property("ApplnMode") == "08", 'Blaze响应缺少发卡模式元素'
    print("Blaze接口自动化测试通过")
