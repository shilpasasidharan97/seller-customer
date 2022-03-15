from dataclasses import field
from pyexpat import model
import re
from xml.dom.minidom import Attr
from django import forms

from common.models import Customer, Seller


class CustomerRegForm(forms.ModelForm):
    # gender=(
    #     ('m','Male'),
    #     ('f','Female'),
    # )

    cust_name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    cust_email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':'form-control'}))
    cust_phone_no=forms.CharField(label='Phone number',widget=forms.TextInput(attrs={'class':'form-control'}))
    cust_password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # cust_email=forms.CharField(label='Name',widget=forms.RadioSelect(choices=gender))
    # cust_email=forms.CharField(label='Name',widget=forms.Select(choices=gender))
    class Meta:
        model=Customer
        fields=('cust_name','cust_email','cust_phone_no','cust_password')
        # field='__all__'
        # exclude=('cust_id',)


    def clean_cust_password(self):
        psw=self.cleaned_data['cust_password']

        if len(psw)<8 :
            raise forms.ValidationError('Password should be minimum 8 characters')
        return psw

    def clean_cust_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email=self.cleaned_data['cust_email']
        if not re.match(regex, email):
           raise forms.ValidationError('Not valid')
        return email



class SellerRegForm(forms.ModelForm):
    seller_name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    seller_email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':'form-control'}))
    seller_phone_no=forms.CharField(label='Phone number',widget=forms.TextInput(attrs={'class':'form-control'}))
    account_holder=forms.CharField(label='Account Holder Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    
    account_number=forms.CharField(label='Account Number',widget=forms.TextInput(attrs={'class':'form-control'}))
    IFSC_code=forms.CharField(label='IFSC',widget=forms.TextInput(attrs={'class':'form-control'}))

    seller_password=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=Seller
        fields=('seller_name','seller_email','seller_phone_no','account_holder','IFSC_code','seller_password')

    def clean_seller_password(self):
        psw=self.cleaned_data['seller_password']

        if len(psw)<8 :
            raise forms.ValidationError('Password should be minimum 8 characters')
        return psw
    
    