from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$',views.renderpolls,name = 'polls'),
		url(r'^dashboard',views.renderdashboard,name='dashboard'),
        url(r'^notifications',views.rendernotifications,name='notifications'),
		url(r'^table1',views.rendertable1,name = 'table1'),
		url(r'^table2',views.rendertable2,name = 'table2'),
		url(r'^table',views.rendertable,name = 'table'),
		url(r'^template',views.rendertemplate,name = 'template'),
		url(r'^user',views.renderuser,name = 'user'),
        url(r'^add_project',views.renderadd_project,name = 'add_project'),
		url(r'^index',views.renderindex,name = 'index'),
		
		]
