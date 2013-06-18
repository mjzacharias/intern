from django.contrib import admin

from projects.models import Project
from tasks.models import Task
from django.contrib.auth.models import User

class TaskInline(admin.TabularInline):
	model = Task
	extra = 2

class ProjectAdmin(admin.ModelAdmin):
	fieldsets= [ 
		( None , { 'fields' : ['name','user'] } ),
		( 'Description' , { 'fields' : ['description',] , 'classes' : ['collapse'] }),
		( 'Date Information' , { 'fields' : ['start_date','end_date',] , 'classes' : ['collapse'] } ),
	]
	inlines = [TaskInline]
	list_display = [ 'name','user','end_date', ]
	# list_display = ( 'end_date', 'ending_recently', )
	list_filter = ['end_date']
	search_fields = ['name']

admin.site.register(Project,ProjectAdmin)