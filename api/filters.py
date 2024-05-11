import django_filters
from .models import Study

class StudyFilter(django_filters.FilterSet):
    class Meta:
        model = Study
        fields = "__all__"
