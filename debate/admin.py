from django.contrib import admin
from debate.models import Statement
from debate.models import Argument
from debate.models import ArgumentFor
from debate.models import ArgumentPart

# admin.site.register(Statement)

#TODO: make the admin interface nice (it may be impossible to do nice things in django

#TODO: add field that calculates correctness to the admin interface


class ArgumentPartAdmin(admin.ModelAdmin):
    fields = ['statment']

admin.site.register(ArgumentPart, ArgumentPartAdmin)

class ArgumentPartInline(admin.TabularInline):
    model = ArgumentPart
    extra = 3
    
class ArgumentAdmin(admin.ModelAdmin):
    fields = ['pub_date']
    inlines = [ArgumentPartInline]

admin.site.register(Argument, ArgumentAdmin)

 
class ArgumentForAdmin(admin.ModelAdmin):
    fields = ['argument']
 
admin.site.register(ArgumentFor, ArgumentForAdmin)
 
class ArgumentForInline(admin.StackedInline): #TODO: make admin.TabularInline
    model = ArgumentFor
    extra = 3
 
class StatementAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'text']
    inlines = [ArgumentForInline]
 
admin.site.register(Statement, StatementAdmin)
