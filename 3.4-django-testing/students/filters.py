from django_filters import filterset
from students.models import Course


class CourseFilter(filterset.FilterSet):
    class Meta:
        model = Course
        fields = ["id", "name"]
