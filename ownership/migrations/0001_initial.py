# Generated by Django 5.1.1 on 2024-09-20 11:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnershipDocumentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_of_identity', models.ImageField(upload_to='OwnershipDocumentRequest/proof_of_identity/')),
                ('lease_agreement', models.ImageField(blank=True, null=True, upload_to='OwnershipDocumentRequest/lease_agreement/')),
                ('housing_certificate', models.ImageField(blank=True, null=True, upload_to='OwnershipDocumentRequest/housing_certificate/')),
                ('purchase_contract', models.ImageField(blank=True, null=True, upload_to='OwnershipDocumentRequest/purchase_contract/')),
                ('title_deed', models.ImageField(blank=True, null=True, upload_to='OwnershipDocumentRequest/title_deed/')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('request_status', models.CharField(default='pending', max_length=100)),
                ('refugee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OwnershipDocumentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_date', models.DateField(auto_now_add=True)),
                ('response_status', models.CharField(blank=True, max_length=100, null=True)),
                ('document_ownership', models.ImageField(blank=True, null=True, upload_to='OwnershipDocumentResponse/document_ownership/')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ownership.ownershipdocumentrequest')),
            ],
        ),
    ]
