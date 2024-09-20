from django.contrib import admin

from .models import OwnershipDocumentRequest, OwnershipDocumentResponse

# Register your models here.
admin.site.register(OwnershipDocumentResponse)
admin.site.register(OwnershipDocumentRequest)