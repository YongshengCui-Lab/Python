import random
from MyQR import myqr
myqr.run(
    words = 'https://www.weibo.com/u/1975337123?refer_flag=0000015010_&from=feed&loc=avatar',
    version = 5,
    level = 'H',
    picture = 'b.jpg',
    colorized = True,
    contrast = 1.0,
    brightness = 1.0,
    save_name = 'c.png',
    )