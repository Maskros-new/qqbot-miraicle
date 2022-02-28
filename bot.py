import miraicle
from plugins import *

# @miraicle.Mirai.receiver('GroupMessage')
# def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
#     bot.send_group_msg(group=msg.group, msg='Hi~')
#
#
# @miraicle.Mirai.receiver('FriendMessage')
# def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
#     bot.send_friend_msg(qq=msg.sender, msg='别私信老子')


qq = 1234567890           # 你登录的机器人 QQ 号
verify_key = '1234567890'     # 你在 setting.yml 中设置的 verifyKey
port = 8080                 # 你在 setting.yml 中设置的 port (http)

bot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)
bot.set_filter(miraicle.GroupSwitchFilter(r'config\group_switch.json'))
bot.set_filter(miraicle.BlacklistFilter(r'config\blacklist.json'))
bot.run()