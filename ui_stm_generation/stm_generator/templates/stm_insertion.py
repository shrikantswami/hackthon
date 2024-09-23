from django.views.generic import DetailView, UpdateView
from stm_generator.models import Cohort, Student



class StudentUpdateView(UpdateView):
    template_name = 'form.html'
    model = Student
    slug_field = 'id'
    slug_url_kwarg = 'id'
    fields = ('name', 'age', 'active', 'cohort', 'ride', 'fav_color', 'fav_snack', 'fav_activity')


class CohortDetailView(DetailView):
    template_name = 'cohort_detail.html'
    model = Cohort
    slug_field = 'id'
    slug_url_kwarg = 'id'
