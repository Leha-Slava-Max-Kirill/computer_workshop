from django.db import models
from django.urls import reverse



# LAYER ONE



class SocketType(models.Model):
    """Model representing a socket type for cpu, motherboard and cpu cooler."""
    name = models.CharField(max_length=40, help_text='Enter a socket type (e.g. LGA 1700)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class RamSlotType(models.Model):
    """Model representing a ram slot."""
    name = models.CharField(max_length=40, help_text='Enter a ram slot type (e.g. DDR1)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class StorageType(models.Model):
    """Model representing a ram slot."""
    name = models.CharField(max_length=40, help_text='Enter a storage type (e.g. SDD)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name



# LAYER TWO



class Cpu(models.Model):
    """Model representing a CPU."""
    name = models.CharField(max_length=40, help_text='Enter a CPU name (e.g. intel core i5)')
    socket = models.ForeignKey('SocketType', on_delete=models.SET_NULL, null=True)
    cores = models.IntegerField()
    threads = models.IntegerField()
    performance = models.IntegerField()
    tdp = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, socket type={self.socket}, cores={self.cores}, threads={self.threads}, performance={self.performance}, tdp={self.tdp}'
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('cpu-detail', args=[str(self.id)])

class Motherboard(models.Model):
    """Model representing a Motherboard."""
    name = models.CharField(max_length=40, help_text='Enter a Motherboard name')
    socket = models.ForeignKey('SocketType', on_delete=models.SET_NULL, null=True)
    m2 = models.IntegerField()
    slotsRam = models.IntegerField()
    ramSlotType = models.ForeignKey('RamSlotType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, socket type={self.socket}, m2={self.m2}, slotsRam={self.slotsRam}, ramSlotType={self.ramSlotType}'
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('motherbord-detail', args=[str(self.id)])

class Ram(models.Model):
    """Model representing a RAM."""
    name = models.CharField(max_length=40, help_text='Enter a RAM name')
    size = models.IntegerField()
    ramSlotType = models.ForeignKey('RamSlotType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, size={self.size}, ramSlotType={self.ramSlotType}'
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('ram-detail', args=[str(self.id)])

class Gpu(models.Model):
    """Model representing a GPU."""
    name = models.CharField(max_length=40, help_text='Enter a GPU name')
    performance = models.IntegerField()
    vram = models.IntegerField()
    powerSupply = models.IntegerField()
   
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, performance={self.performance}, vram={self.vram}, powerSupply={self.powerSupply}'
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('gpu-detail', args=[str(self.id)])

class Psu(models.Model):
    """Model representing a GPU."""
    name = models.CharField(max_length=40, help_text='Enter a PSU name')
    power = models.IntegerField()
  
    def __str__(self):
        return f'{self.name}, power={self.power}'
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('psu-detail', args=[str(self.id)])

class Storage(models.Model):
    """Model representing a Storage."""
    name = models.CharField(max_length=40, help_text='Enter a Storage name')
    capacity = models.IntegerField()
    storageType = models.ForeignKey('StorageType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}, capacity={self.capacity}, storageType={self.storageType}'
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('storage-detail', args=[str(self.id)])

class CpuCooler(models.Model):
    """Model representing a Storage."""
    name = models.CharField(max_length=40, help_text='Enter a CPU cooler name')
    tdp = models.IntegerField()
    socket = models.ForeignKey('SocketType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}, tdp={self.tdp}, socketType={self.socket}'
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('cpucooler-detail', args=[str(self.id)])



# LAYER THREE



class Computer(models.Model):
    """Model representing a fully assembled computer."""
    name = models.CharField(max_length=200, help_text='Enter a socket type (e.g. Vasyas computer)')

    cpu = models.ForeignKey('Cpu', on_delete=models.SET_NULL, null=True)
    motherboard = models.ForeignKey('Motherboard', on_delete=models.SET_NULL, null=True)
    ram = models.ForeignKey('Ram', on_delete=models.SET_NULL, null=True)
    gpu = models.ForeignKey('Gpu', on_delete=models.SET_NULL, null=True)
    psu = models.ForeignKey('Psu', on_delete=models.SET_NULL, null=True)
    storage = models.ForeignKey('Storage', on_delete=models.SET_NULL, null=True)
    cpuCooler = models.ForeignKey('CpuCooler', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this computer."""
        return reverse('computer-detail', args=[str(self.id)])