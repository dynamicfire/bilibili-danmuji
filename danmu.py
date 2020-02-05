# -*- coding: utf-8 -*-
import requests
import time
import wave
import json
import base64
import time
import collections

from request_util import request, authorization
from pydub import AudioSegment
from pydub.playback import play

old_list = []
old_metalist = []
class Danmu():
    def __init__(self):
        self.url = "https://api.live.bilibili.com/ajax/msg"
        self.headers ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0",
            "Referer": "https://live.bilibili.com/901625?spm_id_from=333.334.b_62696c695f6c697665.13",
            }
        self.data = {
            "roomid":"_", #replace '_' with roomid #将'_'替换为你想要的抓取弹幕直播间的roomid
            "csrf_token":"",	
            "csrf":"",	
            "visit_id":""
            }

    def tts_process(self,text):
	    req = request()
	    req.init()
	    auth = authorization()
	    auth.init()

	    #request_data = collections.OrderedDict()
	    request_data = dict()
	    request_data['Action'] = 'TextToStreamAudio'
	    request_data['AppId'] = auth.AppId
	    request_data['Codec'] = req.Codec
	    request_data['Expired'] = int(time.time()) + auth.Expired
	    request_data['ModelType'] = req.ModelType
	    request_data['PrimaryLanguage'] = req.PrimaryLanguage
	    request_data['ProjectId'] = req.ProjectId
	    request_data['SampleRate'] = req.SampleRate
	    request_data['SecretId'] = auth.SecretId
	    request_data['SessionId'] = req.SessionId
	    request_data['Speed'] = req.Speed
	    request_data['Text'] = text
	    request_data['Timestamp'] = int(time.time())
	    request_data['VoiceType'] = req.VoiceType
	    request_data['Volume'] = req.Volume

	    signature = auth.generate_sign(request_data = request_data)
	    header = {
	        "Content-Type": "application/json",
	        "Authorization": signature
	    }
	    url = "https://tts.cloud.tencent.com/stream"

	    r = requests.post(url, headers=header, data=json.dumps(request_data), stream = True)
	    i = 1
	    filename = 'test.wav'
	    wavfile = wave.open(filename, 'wb')
	    wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
	    for chunk in r.iter_content(1000):
	        if (i == 1) & (str(chunk).find("Error") != -1) :
	            print(chunk)
	            return 
	        i = i + 1
	        wavfile.writeframes(chunk)
	        
	    wavfile.close()
	    try:
	    	song = AudioSegment.from_wav("test.wav")
	    	play(song)
	    except:
	    	print("[System] 跳过该条")
	    
	    
        
    def text_danmu(self,html):
        global old_list, old_metalist
        temp_list = []
        temp_metalist = []
        for text in html["data"]["room"]:
            temp_list.append(text["text"])
            temp_metalist.append(text["timeline"] + " " + text["nickname"])
            
        if temp_list == old_list and temp_metalist == old_metalist:
            pass
        else:
            for text_number in range (1,11):
                if "".join(temp_list[:text_number]) in "".join(old_list) and "".join(temp_metalist[:text_number]) in "".join(old_metalist):
                    pass
                else:
                    try:
                        print (temp_metalist[text_number-1] + ": " + temp_list[text_number-1])
                    except:
                        pass
                    else:
                        self.tts_process(temp_list[text_number-1])
            old_list = temp_list[:]
            old_metalist = temp_metalist[:]
            
    def get_danmu(self):
        html = requests.post(url=self.url,headers=self.headers,data=self.data)
        html.json()
        self.text_danmu(eval(html.text))

danmuji = Danmu()
while True:
    danmuji.get_danmu()
    time.sleep(1)
    #每1秒钟调用一个刷新弹幕