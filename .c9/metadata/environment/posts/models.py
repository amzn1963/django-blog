{"filter":false,"title":"models.py","tooltip":"/posts/models.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":25},"end":{"row":17,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"6b919d8e9fd111f9fe1272a778f349aaa822e3b6","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":26},"action":"remove","lines":["# -*- coding: utf-8 -*-","from __future__ import unicode_literals","","from django.db import models","","# Create your models here."],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":25},"action":"insert","lines":["from django.db import models","from django.utils import timezone","","","class Post(models.Model):","    \"\"\"","    A single Blog post","    \"\"\"","    title = models.CharField(max_length=200)","    content = models.TextField()","    created_date = models.DateTimeField(auto_now_add=True)","    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)","    views = models.IntegerField(default=0)","    tag = models.CharField(max_length=30, blank=True, null=True)","    image = models.ImageField(upload_to=\"img\", blank=True, null=True)","","    def __unicode__(self):","        return self.title"],"id":3}]]},"timestamp":1567385887566}