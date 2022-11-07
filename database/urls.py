from django.urls import path
from .views import DoctorDetailView, \
                   DoctorsListView, \
                   PatientDetailView, \
                   PatientsListView, \
                   VisitDetailView, \
                   home_page

urlpatterns = [
        path('', home_page, name='home'),
        path('doctors_list/', DoctorsListView.as_view(), name='doctors_list'),
        path('patients_list/', PatientsListView.as_view(), name='patients_list'),
        path('patient/<int:pk>', PatientDetailView.as_view(), name='patient'),
        path('doctor/<int:pk>', DoctorDetailView.as_view(), name='doctor'),
        path('visit/<int:pk>', VisitDetailView.as_view(), name='visit'),

]
