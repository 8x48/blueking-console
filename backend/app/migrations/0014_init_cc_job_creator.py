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

from django.db import migrations


def load_data(apps, schema_editor):
    """
    添加 作业平台和配置平台的创建者
    """
    App = apps.get_model("app", "App")

    # 添加 作业平台和配置平台的创建者
    App.objects.filter(code__in=['bk_cc', 'bk_job']).update(creater=u"蓝鲸智云")


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20170519_0243'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
