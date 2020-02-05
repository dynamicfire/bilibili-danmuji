# 弹幕鸡
#### 用于从bilibili直播中报弹幕的Python脚本

## 依赖环境
1. 依赖环境：Python 2.7 到 3.7 版本。
2. 从 腾讯云控制台 开通语音合成产品。
3. 获取AppID, SecretID以及SecretKey

## 截图
![1](https://raw.githubusercontent.com/dynamicfire/bilibili-danmuji/master/screenshot.png)

## 相关配置
在 danmu.py 中，第24行：
```python
class Danmu():
    def __init__(self):
        self.url = "https://api.live.bilibili.com/ajax/msg"
        self.headers ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0",
            "Referer": "https://live.bilibili.com/901625?spm_id_from=333.334.b_62696c695f6c697665.13",
            }
        self.data = {
            "roomid":"_", #将'_'替换为你想要的抓取弹幕直播间的roomid
            "csrf_token":"",	
            "csrf":"",	
            "visit_id":""
            }
```
roomid处填入想要的抓取弹幕直播间的roomid

在 conf/tcloud_auth.ini 中，填入获取的AppID, SecretID以及SecretKey

---
# danmuji
#### A simple python script that reads danmu (bullet-screen comments) from bilibili live broadcast aloud

## Environment
1. Pyhton 2.7 to 3.7
2. Activate TTS products from Tencent Cloud Console.
3. Get AppID, SecretID and SecretKey

## Screenshot
![1](https://raw.githubusercontent.com/dynamicfire/bilibili-danmuji/master/screenshot.png)

## Configuration
Line 24, danmu.py:
```python
class Danmu():
    def __init__(self):
        self.url = "https://api.live.bilibili.com/ajax/msg"
        self.headers ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0",
            "Referer": "https://live.bilibili.com/901625?spm_id_from=333.334.b_62696c695f6c697665.13",
            }
        self.data = {
            "roomid":"_", #replace '_' with roomid
            "csrf_token":"",    
            "csrf":"",  
            "visit_id":""
            }
```
Fill in the 'roomid' with the desired room id

In conf/tcloud_auth.ini, fill in the AppID, SecretID and SecretKey