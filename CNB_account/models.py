from django.db import models


class User(models.Model):
    username = models.CharField('用户名', max_length=50)
    password = models.CharField('密码', max_length=50)
    email = models.EmailField()

    def __str__(self):
        # 主要用于交互解释器显示表示该类的字符串
        return self.username
