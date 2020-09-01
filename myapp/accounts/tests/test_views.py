from django.contrib.auth import get_user_model
from django.core.files.uploadfile import SimpleUploadedFile
from django.test import TestCase

class TestUploadView(TestCase):
    """UploadViewのテスト"""
    fixtures = ['test_views.json']

    @classmethod
    def setUpClass(cls):
        # オーバーライドする場合は最初に　super().setUpClass() を呼び出す
　　　　super().setUpClass()
        # TODO: 何らかの事前準備処理

    @classmethod