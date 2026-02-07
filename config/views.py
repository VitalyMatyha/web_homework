from django.http import HttpResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def contacts_view(request):
    html_path = BASE_DIR / 'contacts.html'

    with open(html_path, encoding='utf-8') as file:
        html = file.read()

    return HttpResponse(html, content_type='text/html')
