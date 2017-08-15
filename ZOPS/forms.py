#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
# __author__ = 'wangweijun'
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=True)