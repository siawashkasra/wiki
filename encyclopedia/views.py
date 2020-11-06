from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", 
        {"entries": util.list_entries(), "search": False}
        )

def entry(request, title):
    entry = util.get_entry(title)
    if entry and entry is not None:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(entry),
        })
    raise Http404("Entry doesn't exist!")

def search(request):
    if queryExact(request.GET.get('q', False)):
        return redirect('entry', title= queryExact(request.GET.get('q', False)))

    return render(request, "encyclopedia/index.html", {
            "entries": querySub(request.GET.get('q', False)), 
            "search": True
            })

def querySub(query):
    result_list = []
    for title in util.list_entries():
        if str(query.lower()) in title.lower():
            result_list.append(title)
    return result_list

def queryExact(query):
    for title in util.list_entries():
        if str(query.lower()) == title.lower():
            return title
    return False

def create(request):
    return render(request, 'encyclopedia/create.html')

def save(request):
    title = request.POST.get('title', False)
    content = request.POST.get('markdown', False)
    if queryExact(title):
        messages.error(request, queryExact(title))
        return redirect('create')
    util.save_entry(title, content)
    return redirect('index')