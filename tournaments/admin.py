from django.contrib import admin
from .models import Certificate, CertificateUser, Tournament,TournamentUser

# Register your models here.
admin.site.register(Certificate)
admin.site.register(CertificateUser)
admin.site.register(Tournament)
admin.site.register(TournamentUser)
