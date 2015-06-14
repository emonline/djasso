from django.shortcuts import render, redirect
from myasso.models import Adherent, Association
from myasso.forms import AdherentForm

# Create your views here.
def adherents(request, asso_slug=None):
    if not asso_slug :
        members = Adherent.objects.all().select_related('association')
    else :
        members = Adherent.objects.filter(association__slug=asso_slug).select_related('association')
    return render(request, 'adherents.html', {'members':members})

def associations(request, asso_slug=None):
    if not asso_slug:
        associations = Association.objects.all()
    else :
        associations = Association.objects.filter(slug=asso_slug)
    return render(request, 'associations.html', {'associations':associations})

def createAdherentForm(request, member_id=None):
    if not member_id:
        form = AdherentForm()
    else :
        adherent = Adherent.objects.get(id=member_id)
        form = AdherentForm(instance=adherent)
    return render(request, 'adherentform.html', {'form':form, 'member_id':member_id})

def saveAdherent(request, member_id=None):
    if member_id:
        instance = Adherent.objects.get(id = member_id)
    else :
        instance = None
    form = AdherentForm(request.POST, instance = instance)
    member = form.save()
    return redirect('/adherents/%d' %member.id)

def viewAdherent(request, member_id=None):
    if not member_id:
        return redirect('/adherents')
    else :
        member = Adherent.objects.get(id=member_id)
        return render(request, 'adherentview.html', {'member':member, 'member_id':member_id})