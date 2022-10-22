from django.shortcuts import render

from .models import *

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_computers = Computer.objects.all().count()
    #num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_computers': num_computers,
        #'num_instances': num_instances,
        #'num_instances_available': num_instances_available,
        #'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



from django.views import generic

class ComputerListView(generic.ListView):
    model = Computer
    paginate_by = 10
    context_object_name = 'computer_list'   # your own name for the list as a template variable
    #queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    template_name = 'components/computer_list.html'  # Specify your own template name/location

class CpuListView(generic.ListView):
    model = Cpu
    paginate_by = 10
    context_object_name = 'cpu_list'   # your own name for the list as a template variable
    #queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    template_name = 'components/cpu_list.html' # Specify your own template name/location

class GpuListView(generic.ListView):
    model = Gpu
    paginate_by = 10
    context_object_name = 'gpu_list'   # your own name for the list as a template variable
    #queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    template_name = 'components/gpu_list.html' # Specify your own template name/location

class RamListView(generic.ListView):
    model = Ram
    paginate_by = 10
    context_object_name = 'ram_list'   # your own name for the list as a template variable
    #queryset = Computer.objects.filter(name__icontains='Core')[:5] # Get 5 books containing the title war
    template_name = 'components/ram_list.html' # Specify your own template name/location



from django.shortcuts import get_object_or_404

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
