import MessageSender
m = MessageSender.MessageSender("Bark")
m.config({"apikey":"gpKSL4RQYEZyTiKyz9vtEe"})
# sckey: SCU59621Tfe85588030e0a45116714e3b47fd35d85d74d3e91354b
# apikey: gpKSL4RQYEZyTiKyz9vtEe
m.send({"title":"测试","content":"如果看到这条消息，代表iOS推送成功。"})