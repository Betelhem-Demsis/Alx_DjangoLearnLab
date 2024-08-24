from django.shortcuts import render

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import YourModel

@permission_required('yourapp.can_edit', raise_exception=True)
def edit_view(request, pk):
    instance = get_object_or_404(YourModel, pk=pk)
    return render(request, 'edit_template.html', {'instance': instance})

@permission_required('yourapp.can_create', raise_exception=True)
def create_view(request):
    return render(request, 'create_template.html')

@permission_required('yourapp.can_delete', raise_exception=True)
def delete_view(request, pk):
    instance = get_object_or_404(YourModel, pk=pk)
    instance.delete()
   
