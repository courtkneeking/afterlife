from django.conf.urls import url
from . import views 


urlpatterns = [
	url(r'^$', views.index),
	url(r'^add$', views.add),
	url(r'^submit$', views.submit),
	url(r'^display/(?P<subject_id>\d+)$', views.display),
	url(r'^addfriend', views.addfriend),
	url(r'^addcondolence', views.addcondolence),
	url(r'^addstory', views.addstory),
	url(r'^addimage', views.addimage),
	url(r'^edit/(?P<subject_id>\d+)$', views.edit),
	url(r'^deletestory$', views.deletestory),
	url(r'^deleteimage$', views.deleteimage),
	url(r'^deletefriend$', views.deletefriend),
	url(r'^deletecondolence$', views.deletecondolence),
	url(r'^deletecondolence$', views.deletecondolence),
	url(r'^editpage$', views.editpage),
	url(r'^slideshow$', views.displayslideshow),
]
