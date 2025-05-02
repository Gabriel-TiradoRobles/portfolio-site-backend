# from django.shortcuts import render
# from portfolio_app.models import Course
# from django.http import JsonResponse

# # Create your views here.
# def course_list(request):
#     courses = Course.objects.all()
#     data = { 'courses': list(courses.values()) }

#     return JsonResponse(data)

# def course_detail(request, pk):
#     course = Course.objects.get(pk=pk)
#     data = {
#         'courseCode': course.courseCode,
#         'courseName': course.courseName
#     }

#     return JsonResponse(data)