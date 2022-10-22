from django.contrib import admin
from .models import *

admin.site.register(SocketType)
admin.site.register(RamSlotType)
admin.site.register(StorageType)
# admin.site.register(Cpu)
# admin.site.register(Ram)
# admin.site.register(Gpu)
# admin.site.register(Psu)
# admin.site.register(Storage)
# admin.site.register(Motherboard)
# admin.site.register(CpuCooler)
#admin.site.register(Computer)

# Register your models here.

class CpuAdmin(admin.ModelAdmin):
    list_display = ('name', 'socket', 'cores', 'threads', 'performance', 'tdp')
    list_filter = ('name', 'socket', 'cores', 'threads', 'performance', 'tdp')

class RamAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'ramSlotType')
    list_filter = ('name', 'size', 'ramSlotType')

class GpuAdmin(admin.ModelAdmin):
    list_display = ('name', 'performance', 'vram', 'powerSupply')
    list_filter = ('name', 'performance', 'vram', 'powerSupply')
    
    def queryset(self, request, queryset):
        filt_powerSupply = request.GET.get('powerSupply')
        return queryset.filter(
                    powerSupply__range=self.powerSupply_dict[filt_powerSupply]
                )

class PsuAdmin(admin.ModelAdmin):
    list_display = ('name', 'power')
    list_filter = ('name', 'power')

class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'storageType')
    list_filter = ('name', 'capacity', 'storageType')

class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'socket', 'm2', 'slotsRam', 'ramSlotType')
    list_filter = ('name', 'socket', 'm2', 'slotsRam', 'ramSlotType')

class CpuCoolerAdmin(admin.ModelAdmin):
    list_display = ('name', 'tdp', 'socket')
    list_filter = ('name', 'tdp', 'socket')

# Register the admin class with the associated model
admin.site.register(Cpu, CpuAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Gpu, GpuAdmin)
admin.site.register(Psu, PsuAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(CpuCooler, CpuCoolerAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'motherboard', 'cpu', 'ram', 'gpu', 'psu', 'storage', 'cpuCooler')
    list_filter = ('name', 'motherboard', 'cpu', 'cpu__socket', 'motherboard__ramSlotType', 'ram', 'gpu', 'psu', 'storage', 'cpuCooler')
