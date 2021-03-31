"""gs1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from api import views
from  rest_framework.routers import  DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# for view set
# creating router object
router = DefaultRouter()
# registering viewset with router
router.register('sviewsetapi',views.StudentViewset, basename='s')

# for Model view set
# creating router object
mrouter = DefaultRouter()
# registering viewset with router
mrouter.register('sviewsetapi',views.StudentModelViewSet, basename='st')

# For Read Only model
# creating router object
mrouter_o = DefaultRouter()
# registering viewset with router
mrouter_o.register('sviewsetapi',views.StudentReadOnlyModelViewSet, basename='stu')

# for Auth Api
# creating router object
authapirouter = DefaultRouter()
# registering viewset with router
authapirouter.register('sviewsetapi',views.StudentAuthView, basename='stud')

# for Session Api
# creating router object
sessionapirouter = DefaultRouter()
# registering viewset with router
sessionapirouter.register('sviewsetapi',views.StudentSession, basename='stude')

# for Rest Serializer Relation
realtion_router = DefaultRouter()
realtion_router.register('singer', views.SingerViewset, basename = 'singer')
realtion_router.register('song', views.SongViewset, basename= 'song')

# for Hyprlink Model Serializer
hyper_router = DefaultRouter()
hyper_router.register('hyperstu', views.StudentHyperViewset, basename = 'student')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', views.student_detail),
    path('stuinfo/', views.student_list),
    path('stucreate/', views.student_create),
    path('studentapi/', views.student_api),
    path('studentmapi/', views.StudentMAPI.as_view()),
    path('stuapi/', views.student_api),

    # for good b
    path('studapi/', views.studentb_api),
    path('studapi/<int:pk>', views.studentb_api),
    
    # for class based api
    path('classapi/', views.StudentClassAPI.as_view()),
    path('classapi/<int:pk>', views.StudentClassAPI.as_view()),

    # for generic api
    path('genericapi/', views.StudentList.as_view()),
    path('genericapicreate/', views.StudentCreate.as_view()),
    path('genericapiretrieve/<int:pk>', views.StudentRetrive.as_view()),
    path('genericapiupdate/<int:pk>', views.StudentUpdate.as_view()),
    path('genericapidelete/<int:pk>', views.StudentDelete.as_view()),
    path('genericpatch/<int:pk>', views.StudentPatch.as_view()),

    # for generic api for group
    path('genericlc/', views.StuLC.as_view()),
    path('genericrud/<int:pk>', views.StuRUD.as_view()),

    #for concreate view class
    path('cslist/', views.CsList.as_view()),
    path('cscreate/', views.CsCreate.as_view()),
    path('csretrieve/<int:pk>', views.CsRetrieve.as_view()),
    path('csupdate/<int:pk>', views.CsUpdate.as_view()),
    path('csdelete/<int:pk>', views.Csdelete.as_view()),

    #for concreate view class in group
    path('cslistcreate/', views.CsListCreate.as_view()),
    path('csrud/<int:pk>', views.CsRUD.as_view()),
    
    # for view set
    path('', include(router.urls)),

    # for Model view set
    path('model', include(mrouter.urls)),

    # for Read Only Model view set
    path('modelonly', include(mrouter_o.urls)),

    # for class based auth
    path('authapi', include(authapirouter.urls)),

    # for class based session
    path('sessionapi', include(sessionapirouter.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    # for function based authentication permission
    path('fpermission/', views.studentb_api_permission),
    path('fpermission/<int:pk>', views.studentb_api_permission),

    # for obtain auth token
    path('gettoken/', obtain_auth_token),

    # for obtain auth token custom response
    path('customtoken/', CustomAuthToken.as_view()),

    # for simple jwt token
    path('jwtapitoken/', TokenObtainPairView.as_view(), name = 'jwttoken'),
    path('jwtrefreshtoken/', TokenRefreshView.as_view(), name = 'jwttoken_refresh'),
    path('jwtverifytoken/', TokenVerifyView.as_view(), name = 'jwttoken_verify'),

    # for filtering
    path('filterstu/', views.StuL.as_view(), name= 'filtr'),

    # for Rest Serializer Relation
    path('relation/', include(realtion_router.urls)),

    # for Hyperlink model Serializer
    path('hyper/', include(hyper_router.urls)),

]
