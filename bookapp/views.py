from django.shortcuts import render

from .models import Book
from .forms import BookForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

# homepage = render(request, "homepage.html")


def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "book_list.html", context)

def book_detail(request, pk):
    return render(request, "book_detail.html")


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "book_create.html", {"form": form})




def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "book_update.html", {
        "form": form,
        "book": book
    })



def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookdelete.html")
