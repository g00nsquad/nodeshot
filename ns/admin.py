from django.contrib import admin
from ns.models import * 

class NodeAdmin(admin.ModelAdmin):
    list_display  = ('name', 'owner', 'status', 'added', 'updated')
    list_filter   = ('status', 'added', 'updated')
    search_fields = ('name', 'owner', 'email', 'cap')
    save_on_top = True
admin.site.register(Node, NodeAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display  = ('name', 'node', 'type', 'added', 'updated')
    list_filter   = ('added', 'updated', 'node')
    search_fields = ('name', 'type')
    save_on_top = True
admin.site.register(Device, DeviceAdmin)

admin.site.register(Interface)
admin.site.register(HNAv4)
admin.site.register(Link)