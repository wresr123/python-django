from django.forms import ModelForm
from django import forms
from task.models import Client, Manufacturer
from django.utils.translation import gettext_lazy as _

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'password', 'name', 'telephone', 'company', 'position']
        labels = {
            'email': _('이메일'),
            'password': _('비밀번호'),
            'name': _('이름'),
            'telephone': _('휴대전화'),
            'company': _('회사명'),
            'position': _('직급'),
        }
        widgets = {
        }
        help_texts = {
        }
        error_messages = {
            'telephone': {
                'max_length': _('- 없이 숫자만 입력해주세요. (최대 11자리)')
            },
        }



class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['email', 'password', 'name', 'telephone', 'company']
        labels = {
            'email': _('이메일'),
            'password': _('비밀번호'),
            'name': _('이름'),
            'telephone': _('휴대전화'),
            'company': _('회사명'),
        }
        error_messages = {
            'telephone': {
                'max_length': _('- 없이 숫자만 입력해주세요. (최대 11자리)')
            },
        }

