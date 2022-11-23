# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - 蓝鲸桌面 (BlueKing - bkconsole) available.
Copyright (C) 2022 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.

We undertake not to change the open source license (MIT license) applicable

to the current version of the project delivered to anyone in the future.
"""

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkcore', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentsystem',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='userauthtoken',
            name='app_code',
            field=models.CharField(max_length=128, verbose_name='\u84dd\u9cb8\u667a\u4e91\u5e94\u7528\u7f16\u7801'),
        ),
    ]
