<div align="center">
<h1 align="center">
Auto-ShiXiBeiAn
</h1>
<p align="center">
🥰实习备案自动打卡解决方案🥰
</p>
<p align="center">
支持多用户、自定义位置与时间、微信消息推送
</br>
</p>
</br>
<a target="_blank" href="https://b23.tv/hsaDxKf">视频教程</a>
</div>
</br>






> 版权所有：
>
> 微信：XuanRan_Dev
>
> 邮箱：XuanRanDev@qq.com
>
> 如果此项目侵犯您的合法权益，可通过邮件联系我下架此项目。
>
> + https://github.com/XuanRanDev/Auto-ShiXiBeiAn
> + https://github.com/XuanRanDev/Auto-ZhiXiaoJiaYuan
> + https://github.com/XuanRanDev/Auto-ZhiXiaoJiaYuan-SCF
> + https://github.com/XuanRanDev/Auto-GongXueYun
> + https://github.com/XuanRanDev/Auto-GongXueYun-2
>
> 等项目，均采用GPL2.0开源协议开源，目的在于使更多人学习计算机网络和安全，根据GPL2.0协议，开发者不对软件的适用性或功能做出任何保证。
>
> 为了整个社区的良性发展，我们强烈建议学习人员做到以下几点：
>
> 所有的赞助均为支持开发，供于更多人学习测试与交流，**我们不鼓励、不赞成、不支持任何人，使用任何违规方式完成实习和打卡任务。**
>
> 同时，鉴于项目的特殊性，开发者可能在任何时间**停止更新**或**删除项目**。





## 前言

**1、请务必认真阅读此文档后继续！**

**2、在开始之前请帮我点一下右上角的star。**

**3、此项目仅限学习交流，禁止用于任何商业或违法用途！**

**4、此项目仅限学习交流，您必须在Fork或下载此仓库源码后的24小时内删除所有内容。**

**5、此项目仅限学习交流，学习或使用此项目造成任何损失均由个人承担。**

**6、如基于或参考此项目进行二次开发，请注明原作者并使用GPL2.0许可证**



版权所有：XuanRan

版权所有：XuanRan

版权所有：XuanRan


![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/XuanRanDev/Auto-ShiXiBeiAn?include_prereleases)
![GitHub](https://img.shields.io/github/license/XuanRanDev/Auto-ShiXiBeiAn)
![GitHub forks](https://img.shields.io/github/forks/XuanRanDev/Auto-ShiXiBeiAn)

</br>

## 目录

- [前言](#前言)
- [使用门槛](#使用门槛)
- [使用方法](#使用方法)
  - [Github Actions](#github-actions)
  - [使用自己的服务器部署](#使用自己的服务器部署)
- [修改自动打卡时间🎯](#修改自动打卡时间)
- [赞助支持](#赞助支持)
- [常见问题](#常见问题)
  - [打卡失败](#打卡失败)
  - [暂停自动打卡](#暂停自动打卡)
  - [修改配置文件](#修改配置文件)
  - [保持最新代码](#保持最新代码)

</br>
</br>

## 使用门槛

1、帮我点一下右上角的star（星星）

2、仅限个人学习交流使用，禁止任何平台或个人将此项目用于盈利或违法！



</br></br>

## 使用方法

### Github Actions

推荐指数：⭐⭐⭐⭐⭐


优点：适合没有自己服务器的人使用。


缺点： 每日打卡时间无法保证十分准时，拥有10-30分钟的误差。

</br>

1.点击Star后Fork本仓库🤪
![1.png](https://tc.xuanran.cc/2022/12/01/9b1d336235e28.png)
![2.png](https://tc.xuanran.cc/2022/12/01/2c1c3b427a14a.png)
</br>
2.准备配置文件🤔

如果想同时打卡多个用户,请再添加一个数据体就好了([如果还不理解点我](https://github.com/XuanRanDev/Auto-ShiXiBeiAn/wiki))

**注意：配置文件模板下方有配置含义，请务必参照配置含义填写**
```json
[
  {
    "enable": true,
    "alias": "张三",
    "phone": "18888888888",
    "password": "123456...",
    "deviceType": "Xiaomi|Mi 13|13",
    "deviceId": "设备ID",
    "randomLocation": true,
    "address": "打卡地址",
    "longitude": "位置经度",
    "latitude": "位置纬度",
    "pushKey": "推送Key"
  }
]
```

其配置含义如下：

| 参数名称 | 含义                                                         |
| -- | ------------------------------------------------------------ |
| enable | 是否启用该用户的打卡（true或false)                           |
| alias | 别名，用于在打卡日志中标识不同用户，可空。                   |
| phone | 手机号                                                       |
| password | 密码                                                         |
| deviceType | 设备类型,格式:手机品牌英文名称\|手机代号\|安卓系统版本,例如:Xiaomi\|Mi 13\|13 |
| deviceId | 设备ID,36位字母+数字组合,[点我获取随机ID](http://did.sxba.xuanran.cc)          |
| randomLocation   | 打卡位置浮动，启用后每次打卡系统将会在你原有的经纬度的基础之上删掉最后一位数字并随机加入一位数字，使每次打卡经纬度不同      |
| address | 打卡地址,例如中国河南省洛阳市xxxxx                           |
| longitude | 打卡位置经度,通过坐标拾取来完成，[传送门](https://jingweidu.bmcx.com/) |
| latitude | 打卡位置纬度,通过坐标拾取来完成，[传送门](https://jingweidu.bmcx.com/) |
| pushKey | 打卡结果微信推送，微信推送使用的是pushPlus，请到官网绑定微信([传送门](https://www.pushplus.plus/))，然后在发送消息里面把你的token复制出来粘贴到pushKey这项 |





</br>

3.配置Secret

填写完成后请复制如上配置文件，然后打开仓库的Settings->Secrets->Actions->New repository secret

Name填USERS

Secret填改好的配置文件

![3.png](https://tc.xuanran.cc/2022/11/13/2143b390f8199.png)
![5.png](https://tc.xuanran.cc/2022/12/01/36cadab52b21b.png)

4.运行测试

**以下部分图片复用了工学云自动打卡，除左上角forked from xxxx外与视频教程无其他区别**
![5.png](https://tc.xuanran.cc/2022/11/13/500e789b3dfec.png)
![6.png](https://tc.xuanran.cc/2022/11/13/1366e5e0ced97.png)
![7.png](https://tc.xuanran.cc/2022/11/13/2a2b4b7e01884.png)
![8.png](https://tc.xuanran.cc/2022/11/13/bd1cd3218f77a.png)
![9.png](https://tc.xuanran.cc/2022/11/13/33c6cec2e37ec.png)
![4.png](https://tc.xuanran.cc/2022/12/01/735c10732d2e0.png)
</br></br></br></br>

至此，自动打卡将会在每天8点左右自动运行打卡。😉


</br></br></br>

### 使用自己的服务器部署

推荐指数：⭐⭐⭐⭐⭐

优点：运行稳定、准时。

缺点：有一定的上手成本。

具体教程：

1、下载本仓库源码到你服务器。

2、在服务器中安装好Python环境。

3、运行命令来下载依赖。

```python
pip install requests
pip install pytz
pip install pycryptodome
```

4、在百度搜索：你的操作系统+ 定时任务，查看如何创建定时任务。

5、创建一个user.json配置文件在项目目录，并将配置文件放入其中

6、运行python Main.py测试

</br></br></br>


## 修改自动打卡时间🎯	

修改自动打卡时间需要了解Cron表达式的使用。😴
**修改打卡时间不要开浏览器翻译！！**


</br>
1.编辑sign.yml文件，找到图中我圈出的部分

![image-20221021093411661](https://tc.xuanran.cc/2022/11/10/5d81dcc0bff46.png)

</br>

2.编辑表达式

GitHub的cron表达式不支持精准到秒，所以从最左边开始，分别为：

分钟 小时 日 月份 星期

而且Github的服务器时间会比我们晚八个小时，所以在你需要打卡的时间-8配置到里面就行了

</br>

例如说在上午十点打卡就是:

```yml
- cron: "00 02 * * *"
```

**请注意，在修改打卡时间尽量不要设置在运行高峰期，例如说八点整九点整等，运行高峰期会造成任务启动有极高延迟，可设置为7点57分等非整点时间。**

</br>
</br>





## 赞助支持

如果此仓库帮助了你学到了新知识，你可以帮我买杯可乐，但如果你使用此项目产生任何盈利，请不要支持。

![赞助支持](https://tc.xuanran.cc/2022/11/20/b8f5ddc944634.png)


## 常见问题

### 打卡失败
如果遇到打卡失败，并且错误信息中含有HTTP、timed out字样的，原因在于连接实习备案服务器超时，目前没有很好的解决办法，经过测试，此错误出现率不高，如果遇到可手动重新运行下Actions。

### 暂停自动打卡
在Actions-Sign-右边三个点disable workflow
</br>

### 修改配置文件
Settings-Secrets-Actions-下面Repository secrets有个USERS，点击小箭头编辑，里面没内容是正常的，配置文件一旦保存将无法再被看到。
</br>

### 保持最新代码
随着职校家园的更新，自动打卡可能会在某个版本后失效，开发者会及时更新代码，但你Fork的代码并无法保证与主分支（我的代码）实时同步，此时需要手动同步代码，需要注意的是Github不会有任何通知告诉你代码过时或有新版发布，为此，你可以扫描下方二维码关注公众号，当有重要更新或调整时会在公众号发文提醒。

手动同步代码方法：
![微信截图_20221130142844.png](https://tc.xuanran.cc/2022/11/30/1dad103cbcd0a.png)

公众号：
![e87a1043ea8f4fada3bb99ba8e35767.jpg](https://tc.xuanran.cc/2022/12/02/d1b00d4d20886.jpg)





</br></br>
最后，帮我点下仓库的小星星，Thanks.

😀😀😀😀😀
