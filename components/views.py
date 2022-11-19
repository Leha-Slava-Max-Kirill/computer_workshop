from django.views import generic
from django.shortcuts import get_object_or_404
from distutils import core
from email.errors import ObsoleteHeaderDefect
from urllib import request
from django.shortcuts import render
from django.utils.http import base36_to_int, int_to_base36, urlencode

from .models import Ram, Cpu, Computer, Gpu
# Import ListView module
# Import Product module
# Import Q module


#from django.utils.translation import ugettext as _


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    num_computers = Cpu.objects.all().count()
    context = {
        'num_computers': num_computers,
    }
    return render(request, 'index.html', context=context)


# def get_cores(request):
#     if request.method == "POST":
#         form = GetCores(request.POST)
#         if form.is_valid():
#             num_computers = Cpu.objects.filter(cores=form.cores)
#     else:
#         form = GetCores(request.POST)
#         num_computers = Cpu.objects.all()
#     data = [str(cpu.name) for cpu in num_computers]
#     context = {'num_computers': data, }
#     return render(request, 'components/cpus_filtered_by_cores.html', context=context)


class GetCoresListView(generic.ListView):
    model = Cpu
    queryset = Cpu.objects.all()
    context_object_name = 'cpus_list'
    template_name = "components/cpus_filtered_by_cores.html"

    def get(self, request, *args, **kwargs):
        cpus = self.get_queryset()
        # if request.GET.get('cores'):
        cores = request.GET.get('cores')
        cpus_list = cpus.filter(cores=cores)
        return render(request, self.template_name, {'cpus_list': cpus_list})

class ComputersSearchDetailView(generic.DetailView):
    model = Computer
    paginate_by = 10
    queryset = Computer.objects.all()
    context_object_name = 'computer'
    template_name = "components/computer_list.html"

    def get(self, request, *args, **kwargs):
        computers = self.get_queryset()
        computer_name = request.GET.get('computer_name')
        computer = computers.filter(name=computer_name)
        return render(request, "components/computer_detail.html", {'computer': computer})


class ComputersFilteredListView(generic.ListView):
    model = Computer
    paginate_by = 10
    queryset = Computer.objects.all()
    context_object_name = 'computer_list'
    template_name = "components/computer_list.html"

    def get(self, request, *args, **kwargs):
        computers = self.get_queryset()
        # if request.GET.get('cores'):
        cpu_cores_start = request.GET.get('cpu_cores_start')
        cpu_cores_end = request.GET.get('cpu_cores_end')

        cpu_threads_start = request.GET.get('cpu_threads_start')
        cpu_threads_end = request.GET.get('cpu_threads_end')

        cpu_performance_start = request.GET.get('cpu_performance_start')
        cpu_performance_end = request.GET.get('cpu_performance_end')

        #motherboard_slotsRam_start = request.GET.get('motherboard_slotsRam_start')
        #motherboard_slotsRam_end = request.GET.get('motherboard_slotsRam_end')

        gpu_performance_start = request.GET.get('gpu_performance_start')
        gpu_performance_end = request.GET.get('gpu_performance_end')

        gpu_vram_start = request.GET.get('gpu_vram_start')
        gpu_vram_end = request.GET.get('gpu_vram_end')

        psu_power_start = request.GET.get('psu_power_start')
        psu_power_end = request.GET.get('psu_power_end')

        #storage_capacity_start = request.GET.get('storage_capacity_start')
        #storage_capacity_end = request.GET.get('storage_capacity_end')

        computer_list = computers.filter(cpu__cores__range=[cpu_cores_start, cpu_cores_end],
                                         cpu__threads__range=[cpu_threads_start, cpu_threads_end],
                                         cpu__performance__range=[cpu_performance_start, cpu_performance_end],
                                         #motherboard__slotsRam__range=[motherboard_slotsRam_start, motherboard_slotsRam_end],
                                         gpu__performance__range=[gpu_performance_start, gpu_performance_end],
                                         gpu__vram__range=[gpu_vram_start, gpu_vram_end],
                                         psu__power__range=[psu_power_start, psu_power_end],
                                         #storage__capacity__range=[storage_capacity_start, storage_capacity_end]
                                         )
        return render(request, self.template_name, {'computer_list': computer_list})

  # def get_queryset(self):
  #     get = self.request.GET.copy()
  #     if(len(get)):
  #         get.pop('page')
  #     self.baseurl = urlencode(get)
  #     model = Cpu
  #     self.form = GetCores(self.request.GET)
  #     filters = model.get_queryset(self.request.GET)
  #     if len(filters):
  #         model = model.objects.filter(filters)
  #     else:
  #         model = model.objects.all()
  #     return model


# def get_context_data(self):
#     #context = super(GetCoresListView, self).get_context_data()
#     context['form'] = self.form
#     context['baseurl'] = self.baseurl
#     return context


class ComputerListView(generic.ListView):
    model = Computer
    paginate_by = 10
    # your own name for the list as a template variable
    context_object_name = 'computer_list'
    # queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'components/computer_list.html'


class CpuListView(generic.ListView):
    model = Cpu
    paginate_by = 10
    # your own name for the list as a template variable
    context_object_name = 'cpu_list'
    # queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'components/cpu_list.html'


class GpuListView(generic.ListView):
    model = Gpu
    paginate_by = 10
    # your own name for the list as a template variable
    context_object_name = 'gpu_list'
    # queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'components/gpu_list.html'


class RamListView(generic.ListView):
    model = Ram
    paginate_by = 10
    # your own name for the list as a template variable
    context_object_name = 'ram_list'
    # queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'components/ram_list.html'


class ComputerDetailView(generic.DetailView):
    model = Computer

    def computer_detail_view(request, primary_key):
        computer = get_object_or_404(Computer, pk=primary_key)
        return render(request, 'components/computer_detail.html', context={'computer': computer})


class CpuDetailView(generic.DetailView):
    model = Cpu

    def cpu_detail_view(request, primary_key):
        cpu = get_object_or_404(Cpu, pk=primary_key)
        return render(request, 'components/cpu_detail.html', context={'cpu': cpu})


class GpuDetailView(generic.DetailView):
    model = Gpu

    def gpu_detail_view(request, primary_key):
        gpu = get_object_or_404(Gpu, pk=primary_key)
        return render(request, 'components/gpu_detail.html', context={'gpu': gpu})


class RamDetailView(generic.DetailView):
    model = Ram

    def ram_detail_view(request, primary_key):
        ram = get_object_or_404(Ram, pk=primary_key)
        return render(request, 'components/ram_detail.html', context={'ram': ram})
