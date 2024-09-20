from django.contrib import admin

from .models import FinancialAssistanceResponse, FinancialAssistanceRequest

# Register your models here.
admin.site.register(FinancialAssistanceResponse)
admin.site.register(FinancialAssistanceRequest)
