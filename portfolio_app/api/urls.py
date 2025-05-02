from django.urls import path, include
from portfolio_app.api import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>', views.CourseDetails.as_view(), name='course-detail'),

    path('proj-ui-imgs/', views.ProjectUIImgList.as_view(), name='proj-ui-img-list'),
    path('proj-ui-imgs/<int:projectInfoID>', views.ProjectUIImgDetails.as_view(), name='proj-ui-img-detail'),

    path('papers-and-presentations/', views.PaperAndPresentationList.as_view(), name='paper-and-pres-list'),
    path('papers-and-presentations/<int:pk>', views.PaperAndPresentationDetails.as_view(), name='paper-and-pres-detail'),

    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>', views.ProjectDetails.as_view(), name='project-detail'),

    path('project-info/<int:projectID>', views.ProjectInfoDetails.as_view(), name='project-info'),

    path('languages/', views.LanguageList.as_view(), name='language-list'),
]
