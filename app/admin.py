from django.contrib import admin
from app.models import JobPost

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display= ('__str__','title','salary','date')
    list_filter=('date','salary','expiry')
    search_fields=('title','description')
    search_help_text="Write in your query and hit enter"
    fieldsets=(
        ('Basic Information',{
            'fields':('title','description')
        }),
        ('More Information',{
            'classes':('collapse',),
            'fields':('expiry','salary','slug')
        })
        
        
    )
admin.site.register(JobPost,JobAdmin)
