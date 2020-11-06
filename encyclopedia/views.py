from django.shortcuts import render
from django.http import Http404

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry and entry is not None:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry
        })
    raise Http404("Entry doesn't exist!")
