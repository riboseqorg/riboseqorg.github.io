from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Data, Sample
from .forms import addNewSample

# Create your views here.
def index(response):
    return render(response, "main/home.html", {})


def db(response):
    ls = Data.objects.get(id=1)
    return render(response, "main/database.html", {'ls': ls })

def add(response):
    if response.method == "POST":
        form = addNewSample(response.POST)

        if form.is_valid():
            new = Sample(
                riboseq=Data.objects.get(id=1),
                sample_name=form.cleaned_data["sample_name"],
                sample_description=form.cleaned_data["sample_description"],
                cell_line=form.cleaned_data["cell_line"],
                library_type=form.cleaned_data["library_type"],
                treatment=form.cleaned_data["treatment"],
            )
            new.save()
        return HttpResponseRedirect("/db")

    form = addNewSample()
    return render(response, "main/add.html", {'form': form})
