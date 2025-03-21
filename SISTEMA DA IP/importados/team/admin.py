# team/admin.py
from django.contrib import admin
from .models import TeamMember, Evaluation

admin.site.register(TeamMember)
admin.site.register(Evaluation)
