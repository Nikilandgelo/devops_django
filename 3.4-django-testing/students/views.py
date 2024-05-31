from rest_framework.viewsets import ModelViewSet
from students.filters import CourseFilter
from students.models import Course
from students.serializers import CourseSerializer

class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter
    