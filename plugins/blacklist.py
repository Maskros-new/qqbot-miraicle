import miraicle

@miraicle.Mirai.filter('BlacklistFilter')
def blacklist(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.BlacklistFilter):
    if msg.plain == '拉黑我':
        flt.append(msg.sender)
    elif msg.plain == '我错了':
        flt.remove(msg.sender)