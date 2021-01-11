from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


'''
def entry(request, entry):
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, print("No data"))
    else:
        return render(request, "encyclopedia/entries.html", {
            "entryTitle": entry
        })
'''


def entry(request, entry):
    Title = util.get_entry(entry)
    if Title is None:
        return render(request, "encyclopedia/nopage.html")
    else:
        return render(request, "encyclopedia/entries.html", {
            "EntryTitle": entry
        })
