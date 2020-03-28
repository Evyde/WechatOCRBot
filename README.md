# 微信OCR机器人
- ## 简介
    这是一个基于Python的，对微信电脑端客户端进行OCR识别以便进行自动化操作的机器人。

  
- ## 功能
    - [ ] 自动适应分辨率
    - [ ] 自动调整窗口位置
    - [ ] 识别消息
    - [ ] 回复指定消息
    - [ ] 转发消息
    - [ ] 对指定消息进行其他渠道转发（如Bark，Telegram等）
    
- ## 项目结构
    - Forward.py
    
        负责对消息进行转发。
    
    - main.py
    
        程序主逻辑。
       
    - MessageSender.py
        
        消息转发接口，后期扩展发送方式可以对这个文件进行修改。
    
        该类可扩展，故设置了一个`__init__(method)`方法用以选择发送方法，支持smtp邮件发送，ServerChan微信推送，控制台输出和iOS端的软件Bark推送，关于ServerChan的介绍，请移步[ServerChan](http://sc.ftqq.com)，关于Bark的介绍，请移步[Bark](https://github.com/Finb/Bark/)。
        
        1. `MessageSender.__init__(method)`，该方法传入一个`method`文本，可从`serverChan`、`smtp`、`console`、`Bark`中选一个。
        2. `MessageSender.config(config)`，该方法传入一个`config`字典，以下是两种方式的配置字典格式：
            1.  ServerChan
            
                格式：`{"SCKEY":"你的SCKEY"}`。
            
            2.  SMTP
            
                格式：`{"host":"主机IP或域名","port":"端口，一般是25","fromAddr":"用以发送的邮箱","toAddr":"接收邮箱","fromName":"发送者名称","toName":"接收者名称", "user": "用户名", "pwd": "密码"}`。
         
            3.  Console
                无需配置，config方法直接return
            
            4. Bark
                格式：`{"apiKey": "你的APIKEY"}`
        3. `MessageSender.send(msg)`，发送消息，发送失败会在控制台输出日志，不会抛出异常。
        4. `MessageSender.getMethod()`，返回发送的方法。
    
        5.  Class `ServerChan`负责向ServerChan发送消息。
            1. `ServerChan.__init__(text)`，传入SCKEY。
            2. `ServerChan.send(msg)`，发送消息（支持Markdown格式），直接返回发送状态。
    
        6.  Class `SMTPSender`负责通过SMTP发送消息。
            1. `SMTPSender.__init__(list)`，传入上述配置字典。
            2. `SMTPSender.send(msg)`，发送消息，直接返回发送成功的文本。
            
        7.  Class `ConsoleSender`负责通过控制台输出消息。
            1. `ConsoleSender.send(msg)`，发送消息，直接返回发送成功的文本。
            
        8.  Class `BarkSender`负责通过Bark发送消息。
            1. `BarkSender.__init__(apikey)`，传入APIKEY。
            2. `BarkSender.send(msg)`，发送消息，直接返回发送状态。