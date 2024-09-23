"""
This home page view file
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from stm_generator.models import DataTypes
from stm_generator.models import HomePageLinks, FileForm
from stm_generator.forms import UploadFileForm


from stm_generator.utils import handle_uploaded_file
# Create your views here.


def home(request):
    """
    This is Home Page
    """
    hp_link_context = get_home_page_links(request)
    return render(request, "pages/home.html", hp_link_context)


def get_list_of_data_types_supported(request):
    """
    This function returns list of data types supported by stm generator.
    :param request:
    :return:
    """
    data_types = DataTypes.objects.all()
    context = {
        "data_types": data_types
    }
    return render(request, "pages/supported_data_types.html", context)


def insert_supported_data_types(request, data):
    """
    This function inserts records in data type table
    :return:
    """
    print(data)
    # data_type_insert = DataTypes(data_type='VARCHAR', integer_limit='255')
    # data_type_insert.save()
    print("saved record data")


def get_home_page_links(request):
    """
    :return:
    """
    home_page_links = HomePageLinks.objects.filter(active=1)
    context = {
        "home_page_links": home_page_links
    }
    return context


def upload_file(request):
    if request.method == "POST":
        # form = UploadFileForm(request.POST, request.FILES)
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            form.save()
            # handle_uploaded_file(uploaded_file)
            context = {'file_name': uploaded_file.name , "" : ""}
            return render(request, 'pages/upload_successful.html', context)
    else:
        form = FileForm()
    return render(request, "pages/upload_file.html", {"form": form})


def insert_stm(request):
    """
    :param request:
    :return:
    """