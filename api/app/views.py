from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import base64
# Create your views here.
def index(request):
    return render(request, "index.html")


def upload(request):
    p = request.FILES['image']
    bytes = p.read() # read file as bytes
    readable_hash = hashlib.md5(bytes).hexdigest()

    base64_bytes = base64.b64encode(bytes)
    base64_message = base64_bytes.decode('ascii')

    mid = "data:image/png;base64," + base64_message
    return render(request, "show.html", {"path":mid})