from django.db import models


class Article(models.Model):
    """
    所有的 model 必须继承自django.db.models
    类 Aticle 表示 Blog 的文章，一个类被 diango 映射成数据库中对应的一个表，表名即类名
    类的属性（field），比如下面的 title、body 等对应着数据库表的属性列
    """
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    # 草稿状态和发布状态

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 文章创建时间 设定auto_now_add参数为真，则在文章被创建时会自动添加创建时间
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # 文章最后一次编辑时间，auto_now=True表示每次修改文章时自动添加修改的时间

    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    # choices选项会使该field在被渲染成form时被渲染为一个select组件
    # 两个状态，一个是Draft（草稿），一个是Published（已发布)
    # select组件会有两个选项：Draft 和 Published。但是存储在数据库中的值分别是'd'和'p'

    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前54个字符")
    # 文章摘要，help_text 在该 field 被渲染成 form 是显示帮助信息

    views = models.PositiveIntegerField('浏览量', default=0)
    # 阅览量，PositiveIntegerField存储非负整数

    likes = models.PositiveIntegerField('点赞数', default=0)
    # 点赞数

    topped = models.BooleanField('置顶', default=False)
    # 是否置顶，BooleanField 存储布尔值（True或者False），默认（default）为False

    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
    # 文章的分类，ForeignKey即数据库中的外键。
    # 外键:一对多的关系  即一篇文章对应一个分类，而一个分类下可能有多篇文章
    # on_delete=models.SET_NULL表示删除某个分类（category）后该分类下所有的Article的外键设为null（空）

    def __str__(self):
        # 主要用于交互解释器显示表示该类的字符串
        return self.title

    class Meta:
        # Meta 包含一系列选项
        # ordering 表示排序, - 号表示逆序。即当从数据库中取出文章时，其是按文章最后一次修改时间逆序排列的
        ordering = ['-last_modified_time']


class Category(models.Model):
    """
    存储分类信息-文章
    """
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
