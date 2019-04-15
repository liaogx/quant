#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):  # AbstractUser是Django的默认用户表，使用自定义用户表需要在settings中设置AUTH_USER_MODEL
    """
    用户信息表
    必填字段包括：username, gender, mobile, email
    """
    gender = models.PositiveSmallIntegerField(choices=((0, '男'), (1, '女')), default=0, verbose_name='性别')
    birthday = models.DateField(blank=True, null=True, verbose_name='出生年月日')
    address = models.CharField(max_length=50, blank=True, null=True, verbose_name='地址')
    id_card = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name='身份证号')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    email2 = models.EmailField(max_length=50, unique=True, blank=True, null=True, verbose_name='备用邮箱')
    qq = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name='QQ号')
    wechat = models.CharField(max_length=30, unique=True, blank=True, null=True, verbose_name='微信ID')
    valid_time = models.DurationField(default=timedelta(days=14), verbose_name='有效时间')  # 默认给用户14天有效期
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    REQUIRED_FIELDS = ['email', 'mobile']

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username  # 解决一个非常隐蔽的BUG：为保证能正常登录DRF
