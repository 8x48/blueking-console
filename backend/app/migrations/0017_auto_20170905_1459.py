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
        ('app', '0016_auto_20170629_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='language',
            field=models.CharField(default=b'python', choices=[(b'python', b'Python'), (b'java', b'Java'), (b'php', b'PHP')], max_length=50, blank=True, null=True, verbose_name='\u8bed\u8a00'),
        ),
    ]
