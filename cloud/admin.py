from django.contrib import admin
from cloud.models import Accounts,Users,Containers,ContainerUser
# Register your models here.
class ContainersAdmin(admin.TabularInline):
    model = Containers
    extra = 2
class AccountsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Account Information',{'fields': ['account_name','account_key']}),

    ]
    inlines = [ContainersAdmin]
    list_display = ('account_name', 'account_key')
class ContainerUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ContainerUser Information',{'fields':['user','container','create_date']})
    ]
    list_display = ('user','container')
class UsersAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Users Information',{'fields': ['name','email','user','password','create_date']}),
    ]
    list_display = ('name','email','user','create_date')
admin.site.register(Accounts,AccountsAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(ContainerUser,ContainerUserAdmin)


