# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# UID、头像(personalPhotoUrl String)、姓名(name String)、姓名拼音(pinyinName String)、花名(nickName String)、花名拼音(pinyinNick String)、工号(workNo String)、职位(postName String)、部门(deptName String)、工作状态(workStatus String A-在职 I-离职 W-入职前)、离职时间(gmtLeave Date)

class Profile(models.Model):

    UID = models.CharField(max_length=64)
    personalPhotoUrl = models.CharField(max_length=225, null=True, blank=True)
    username = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    pinyinName = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    nickName = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    pinyinNick = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    workNo = models.CharField(max_length=16)
    postName = models.CharField(max_length=64)
    deptName = models.CharField(max_length=64, db_index=True)
    workStatus = models.CharField(max_length=4, db_index=True)
    gmtLeave = models.DateTimeField(null=True, blank=True)

#    objects = ProfileManager()
