from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import hashlib
import base64
import os
from PIL import Image
import urllib.request
import requests
# Create your views here.
def index(request):
    return render(request, "index.html")


def upload(request):
    p = request.FILES['image']
    bytes = p.read() # read file as bytes
    readable_hash = hashlib.md5(bytes).hexdigest()

    base64_bytes = base64.b64encode(bytes)
    base64_message = base64_bytes.decode('ascii')
    json = {
        "md5" : readable_hash,
        "base64" : base64_message,
    }
    return JsonResponse(json)

def api(request):
    url = request.GET.get('url')
    res = requests.get(url)
    if(res.status_code!=200):
        return JsonResponse({"error":"Image not found"})
    file = url.split("/")[-1]
    res.raw.decode_content=True
    p = open(file, "wb")
    p.write(res.content)
    p.close()
    p = open(file, "rb")
    bytes = p.read() # read file as bytes
    readable_hash = hashlib.md5(bytes).hexdigest()

    base64_bytes = base64.b64encode(bytes)
    base64_message = base64_bytes.decode('ascii')
    json = {
        "md5" : readable_hash,
        "base64" : base64_message,
    }
    os.remove(file)
    return JsonResponse(json)