from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord

# Register to be used with admin interface
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)