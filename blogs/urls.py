"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 1. 导入系统的logging
import logging
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
# 2. 获取日志器
logger = logging.getLogger('django')

def log(request):
    # 3. 使用日志器
    logger.info('info')
    return HttpResponse('test')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', log),
]