from .models import Request

def add_request():
    Request.create()

def get_requests():
    return Request.select()