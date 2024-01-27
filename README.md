# SQLBlind_Flow_Crack
自带GUI的SQL盲注流量一把梭小工具尝试版

>本工具作用为对CTF常见的SQL流量包（pcap、pcapng等）进行一把梭**尝试**，采用GUI的形式方便使用

**欢迎各位大佬将工具无法尝试解出的流量文件通过issues+网盘链接的形式进行提供**

————————————————————————————————————————————————

2024/1/27 更新

1.出现flag、ctf等关键词将高亮显示

2.修复某类常见流量无法提取的问题
————————————————————————————————————————————————

## 使用帮助
**由于本工具使用了pyshark库，需要使用者手动配置自己shark.exe路径，方法如下：**

(1).根据路径指引找到自己pyshark库所在位置
![image](https://github.com/Mumuzi7179/SQLBlind_Flow_Crack/assets/74121593/c91a4545-0e1f-4b60-9270-009e6abb8b77)

(2).找到该路径下的config.ini文件，修改路径即可
![image](https://github.com/Mumuzi7179/SQLBlind_Flow_Crack/assets/74121593/c44ac15f-c602-4f79-b824-3a9f6fabf8b2)

安装依赖库并使用国内源加速：
`pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

执行`python3 gui.pyw`或双击`gui.pyw`即可（双击没有效果见文末）

![演示](https://github.com/Mumuzi7179/SQLBlind_Flow_Crack/assets/74121593/b92baf1a-e34f-454c-bfcb-61432e9e0671)

什么？双击没有效果，大概率是本机装有多个python导致冲突了

1.按下Win + R，输入regedit，然后按Enter打开注册表编辑器。

2.导航到HKEY_CLASSES_ROOT\.pyw。确保该键的默认值设置为Python.NoConFile或类似值。

3.导航到HKEY_CLASSES_ROOT\Python.NoConFile\shell\open\command。

4.确保该键的默认值为"C:\Users\Laptop\AppData\Local\Programs\Python\Python39\pythonw.exe" "%1" %*（根据实际Python安装路径调整）。

