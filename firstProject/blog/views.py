# -*- coding: utf-8 -*-
from django.shortcuts import render#関数ベースビューを使うときには必要みたい

from django.views.generic.base import TemplateView



# Create your views here.

class IndexView(TemplateView):
    '''
    Attributes:
        template_name:
    '''
    #print('index.html Classで実行') #こっちでは出力されない
    template_name = 'index.html'

class ContactView(TemplateView):
    '''
    Attributes:
        template_name:
    '''
    #print('contact.html Classで実行') #こっちでは出力されない
    template_name = 'contact.html'


#関数ベースビュー
def IndexV(request):
    print('index.html 関数ビューで実行') 
    return render(request, 'index.html')

#関数ベースビュー
def ContactV(request):
    print('contact.html 関数ビューで実行') 
    return render(request, 'contact.html')