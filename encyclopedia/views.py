from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import re
import random
import markdown2


# Home Page
def index(request):
    # This lists existing entries in encyclopedia
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def rand(request):
    # selects a title at random
    title = random.choice(util.list_entries())

    # takes the user to the random page
    return HttpResponseRedirect(reverse("wiki_entry", args=[title]))


def search(request):
    # Check if the 'q' parameter exists in the request.GET dictionary
    if 'q' in request.GET:
        # Retrieve the search string from the 'q' parameter
        q = request.GET['q']
        # Checks if there is an entry
        entry = util.get_entry(q)

        # If an entry exists, return the page
        if entry:
            return HttpResponseRedirect(reverse("wiki_entry", args=[q]))

        # If not, show possible pages
        else:
            entries = util.list_entries()
            possibilities = []
            string = re.compile("(?i)(" + q + ")")
            for entry in entries:
                if string.search(entry):
                    possibilities.append(entry)

            # Shows possible pages (i.e., pages where that substring is present) or "no results found"
            return render(
                request,
                "encyclopedia/search.html",
                {"string": q, "possibilities": possibilities},
            )
    else:
        # Handle the case where 'q' parameter is not present in the request
        # Return an error response or redirect to a search page with a message
        return HttpResponse("No search query provided.")



def entry(request, entry_name):
    # Gets Markdown content for the given Entry
    content = util.get_entry(entry_name)

    # If the above variable isn't None, return the entry page
    if content:
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": entry_name, "content": markdown2.markdown(content)},
        )

    # If not, show an error page
    else:
        return render(
            request,
            "encyclopedia/wrong.html",
            {"message": "This page cannot be found but you can create it."},
        )


class NewForm(forms.Form):
    # Adds new form for page
    title = forms.CharField(
        label="Title:",
        widget=forms.TextInput(attrs={"class": "form-control w-75 mb-2"}),
    )
    textarea = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control w-75"}),
        label="Description:",
    )


def new(request):
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():
            # Isolate the content from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            markdown = form.cleaned_data["textarea"]

            # Check if this entry already exists, if it does, return an error
            if util.get_entry(title):
                return render(
                    request,
                    "encyclopedia/wrong.html",
                    {"message": "This entry already exists."},
                )
            # If not, saves new entry and redirects to the new page
            else:
                util.save_entry(title, markdown)
                return HttpResponseRedirect(reverse("wiki_entry", args=[title]))

    # Show new page form if not coming from a POST request
    else:
        return render(request, "encyclopedia/new.html", {"form": NewForm()})


class EditForm(forms.Form):
    # Edit form in page
    edit_content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "cols": "90"}),
        label="Description:",
    )


def edit(request, title):
    # Prepopulates edit form with the markdown content of that title
    form = EditForm(initial={"edit_content": util.get_entry(title)})

    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        update = EditForm(request.POST)

        # Check if form data is valid (server-side)
        if update.is_valid():
            # Isolate the content from the 'cleaned' version of form data
            newcontent = update.cleaned_data["edit_content"]

            # Saves new entry and redirects to the edited page
            util.save_entry(title, newcontent)
            return HttpResponseRedirect(reverse("wiki_entry", args=[title]))

    else:
        return render(request, "encyclopedia/edit.html", {"title": title, "form": form})
