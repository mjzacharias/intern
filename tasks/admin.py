# from django.contrib import admin
# from tasks.models import Task

# class TaskAdmin(admin.ModelAdmin):
#     fieldsets= [ 
#         ( None , {'fields' : ['name','priority']} ),
#         ( 'Description' , {'fields' : ['description'], 'classes' : ['collapse']} ),
#         ( 'Date Information' , {'fields' : ['start_date','end_date',] , 'classes' : ['collapse']} ),
#         ( 'Task Relations' , {'fields' : ['project','user',] , 'classes' : ['collapse']} ),
#     ]
#     list_display = ( 'name','end_date','priority', )
#     list_filter = ['end_date','project','user']
    
# admin.site.register(Task,TaskAdmin)
#  