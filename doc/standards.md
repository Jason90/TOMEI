##Python 编程规范-接口自动化测试

1. 项目名称
   TOMEI：Test object model external interface=面向对象的接口自动化测试框架

2. 开发工具
    vscode+github+pytest

3. 源码管理
   https://github.com/Jason90/TOMEI.git
   origin

4. 项目依赖
    - 外部依赖包统一放到packages.txt文件中
    - 更新依赖信息文件命名：
    `pip freeze >./doc/packages.txt`
    - 安装依赖包命令：
    `pip install -r ./doc/packages.txt`

5. 测试框架
    参见architecture.yuml

6. 命名规范
   |对象|命名规范|备注|
   |----|----|----|
   |文件夹|首字母小写|camel|
   |文件|首字母小写|camel|
   |类|首字母大写|Pascal|
   |方法|首字母小写|camel|


