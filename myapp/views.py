from django.shortcuts import render, redirect
from myapp.models import Professor
from myapp.forms import ProfessorForm

def index(request):
    return render(request, "index.html")

def crud(request):
    if request.user.is_authenticated == False:
        return redirect("login")
    profs = Professor.objects.all()
    pacote = {"professores": profs}
    return render(request, "crud.html", pacote)

def createP(request):
    form = ProfessorForm(request.POST or None)
    pacote = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/crud")
    return render(request, "formProf.html", pacote)

def updateP(request, id):
    update = True
    prof = Professor.objects.get(pk=id)
    form = ProfessorForm(request.POST or None, instance = prof)
    pacote = {"form": form, "update": update}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/crud")
    return render(request, "formProf.html", pacote)

def delP(request, id):
    prof = Professor.objects.get(pk=id)
    prof.delete()
    return redirect("/crud")

def listagem(request):
    profs = Professor.objects.all()
    search = request.GET.get('search')
    if search:
        profs = Professor.objects.filter(nome__icontains=search)
    pacote = {"professores": profs, "search": search}
    return render(request, "listagem.html", pacote)

def consulta(request):
    return render(request, "consulta.html")

def sobre(request):
    return render(request, "sobre.html")
