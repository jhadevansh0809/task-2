from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.UserList.as_view(),name='users'),
    path('userswithname/',views.UsersWithName.as_view(),name='userswithname'),
    path('userdetail/',views.UserDetail.as_view(),name='userdetail'),
    path('organisations/',views.OrganisationView.as_view(),name='organisations'),
    path('organisationdetail/',views.OrganisationDetail.as_view(),name='organisationdetail'),
    path('createupdatepermissions/',views.CreateUpdatePermissionsView.as_view(),name='createupdatepermissions'),
    path('deletepermissions/',views.DeletePermissionsView.as_view(),name='deletepermissions'),
    path('permissionslist/',views.PermissionsListView.as_view(),name='permissionslist'),
]