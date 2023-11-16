from django import forms

class AccountIDForm(forms.Form):
    account_ids = forms.CharField(widget=forms.Textarea, required=False)
    file = forms.FileField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        account_ids = cleaned_data.get('account_ids')
        file = cleaned_data.get('file')

        if account_ids:
            account_ids = [id.strip() for id in account_ids.split(';')]
            if len(account_ids) > 5:
                self.add_error('account_ids', '最多只能输入5个账户ID')
        elif file:
            if not file.name.endswith('.txt'):
                self.add_error('file', '只支持txt文件')
        else:
            raise forms.ValidationError('必须输入账户ID或上传文件')
        
from django import forms
from django.shortcuts import render

# 商品名称表单
class ProductForm(forms.Form):
    product_name = forms.CharField(label='商品名称', max_length=100)

# 关键词表单
class KeywordForm(forms.Form):
    keyword = forms.CharField(label='关键词', max_length=100)

# 账户ID表单
class AccountForm(forms.Form):
    account_ids = forms.CharField(label='账户ID', widget=forms.Textarea)

class SubmitForm(forms.Form):
    productid = forms.CharField(label='商品id', max_length=100)
    selected_keywords = forms.CharField(widget=forms.HiddenInput())
    account_ids = forms.CharField(label='账户ID', max_length=100)
    file = forms.FileField(label='上传txt文件', required=False)