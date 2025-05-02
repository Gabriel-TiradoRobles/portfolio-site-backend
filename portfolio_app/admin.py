from django.contrib import admin
from portfolio_app.models import Courses, Projects, PapersAndPresentations, ProjectUIImages, ProjectInfo, Languages

# Register your models here.
admin.site.register(Courses)
admin.site.register(Projects)
admin.site.register(PapersAndPresentations)
admin.site.register(ProjectUIImages)
admin.site.register(ProjectInfo)
admin.site.register(Languages)