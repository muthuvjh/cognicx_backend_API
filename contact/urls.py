from django.urls import path,include
from contact import views
urlpatterns = [
path('create_agent/', views.Agent_master_View.as_view()),
path('update_agent/<slug:pk>/', views.Agent_masterupdate_View.as_view()),
path('get_agentnew_id/', views.Agent_Gerate_New_Id.as_view()),
path('get_dashboard_data/', views.Dashboard_List.as_view()),
path('file_upload/', views.Agent_File_Upload_View.as_view()),
path('xl_datalist/<slug:agent_id>', views.Agent_File_dataList_View.as_view()),
path('export_data/', views.Export_Contact_data.as_view()),
path('export_data_view/', views.Export_Contact_Viewdata.as_view()),
path('getallcampaign/', views.Campaign_dataList_View.as_view()),

]