from django.contrib import admin
from .models import Note, Games, Sponsor
from accounts.models import UserProfile

# Register your models here.

class NoteInline(admin.StackedInline): #Demo StackedInline vs TabularInline
    model = Note
    fields = ('title',) 
    extra = 0
    
class SponsorAdmin(admin.ModelAdmin):
    inlines = [NoteInline,]
    
    model = Sponsor


#http://stackoverflow.com/questions/6479999/django-admin-manytomany-inline-has-no-foreignkey-to-error    
#https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models
class TaggedNoteInline(admin.TabularInline): 
    model = Note.Games.through
    extra = 0
    
class GamesAdmin(admin.ModelAdmin):
    inlines = [TaggedNoteInline,]
    model = Games

    

admin.site.register(Note)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(UserProfile)