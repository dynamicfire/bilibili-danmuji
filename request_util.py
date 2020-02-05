# -*- coding:utf-8 -*-
import configparser
import urllib
import base64
import hmac
import hashlib
import requests

auth_file_path = "./conf/tcloud_auth.ini"
param_file_path = "./conf/request_parameter.ini"

class authorization:
    AppId = 0
    SecretId = ""
    SecretKey = ""
    Expired = 3600
    conf=configparser.ConfigParser()
    def init(self):
        #print("init")
        self.conf.read("./conf/tcloud_auth.ini", encoding="UTF-8")
        self.AppId = self.conf.getint("authorization", "AppId")
        self.SecretId = self.conf.get("authorization", "SecretId")
        self.SecretKey = self.conf.get("authorization", "SecretKey")
        #print(self)

    def verify_param(self):
        if len(str(self.AppId)) == 0:
             print('AppId can not empty')
        if len(str(self.SecretId)) == 0:
             print('SecretId can not empty')
        if len(str(self.SecretKey)) == 0:
             print('SecretKey can not empty')

    def init_auth(self, appid, secret_id, secret_key):
        self.AppId = appid
        self.SecretId = secret_id
        self.SecretKey = secret_key

    def generate_sign(self, request_data):
        url = "tts.cloud.tencent.com/stream"
        sign_str = "POST" + url + "?"
        sort_dict = sorted(request_data.keys())
        for key in sort_dict:
            sign_str = sign_str + key + "=" + urllib.parse.unquote(str(request_data[key])) + '&'
        sign_str = sign_str[:-1]
        sign_bytes = sign_str.encode('utf-8')
        key_bytes = self.SecretKey.encode('utf-8')
        #print(sign_bytes)
        authorization = base64.b64encode(hmac.new(key_bytes, sign_bytes, hashlib.sha1).digest())
        return authorization.decode('utf-8')

class request:
    Text = "五一小长假去哪里玩啊"
    Action = "TextToStreamAudio"
    Codec = "pcm"
    Expired = 0
    ModelType = 0
    PrimaryLanguage = 1
    ProjectId = 0
    SampleRate = 8000
    SessionId = "123"
    Speed = 2
    VoiceType = 1
    Volume = 5
    conf=configparser.ConfigParser()
    def init(self):
        #print("init")
        self.conf.read("./conf/request_parameter.ini", encoding="UTF-8")
        self.Text = self.conf.get("parameter", "Text")
        self.Action = self.conf.get("parameter", "Action")
        self.Codec = self.conf.get("parameter", "Codec")
        self.Expired = self.conf.getint("parameter", "Expired")
        self.ModelType = self.conf.getint("parameter", "ModelType")
        self.PrimaryLanguage = self.conf.getint("parameter", "PrimaryLanguage")
        self.ProjectId = self.conf.getint("parameter", "ProjectId")
        self.SampleRate = self.conf.getint("parameter", "SampleRate")
        self.SessionId = self.conf.get("parameter", "SessionId")
        self.Speed = self.conf.getint("parameter", "Speed")
        self.VoiceType = self.conf.getint("parameter", "VoiceType")
        self.Volume = self.conf.getint("parameter", "Volume")
        #print(self)

    def verify_param(self):
        if len(str(self.Action)) == 0:
             print('Action can not empty')
        if len(str(self.SampleRate)) == 0:
             print('SampleRate is not set, assignment default value 16000')
             self.SampleRate = 16000

    def init_param(self, text, action, codec, expired, model_type, prim_lan, project_id, sample_rate, session_id, speed, voice_type, volume):
        self.Action = action
        self.Text = text
        self.Codec = codec
        self.Expired = expired
        self.ModelType = model_type
        self.PrimaryLanguage = prim_lan
        self.ProjectId = project_id
        self.SampleRate = sample_rate
        self.SessionId = session_id
        self.Speed = speed
        self.VoiceType = voice_type
        self.Volume = volume

    
