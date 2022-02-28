import miraicle

my_qq = 1164528260         # 你的 QQ 号

@miraicle.scheduled_job(miraicle.Scheduler.every().day.at('8:30'))
def morning(bot: miraicle.Mirai):
    bot.send_friend_msg(qq=my_qq, msg='早上好, 该起床了')

@miraicle.scheduled_job(miraicle.Scheduler.every().day.at('23:30'))
def night(bot: miraicle.Mirai):
    bot.send_friend_msg(qq=my_qq, msg='该睡觉了')