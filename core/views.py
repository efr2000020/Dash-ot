from django.shortcuts import render
from .models import Node 
from .forms import NodeForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Node

def landing_page(request):
    return render(request, 'landing.html')


def node_list(request):
    nodes = Node.objects.all()
    return render(request, "node_list.html", {"nodes": nodes})

def add_node(request):
    if request.method == "POST":
        form = NodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("node_list")
    else:
        form = NodeForm()
    return render(request, "node_form.html", {"form": form})

def delete_node(request, node_id):
    node = get_object_or_404(Node, id=node_id)
    if request.method == "POST":
        node.delete()
        return redirect("node_list")
    return render(request, "node_confirm_delete.html", {"node": node})