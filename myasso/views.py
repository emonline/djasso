from django.shortcuts import render
from myasso.models import Adherent, Association

# Create your views here.
def adherents(request, asso_slug=None):
    if not asso_slug :
        members = Adherent.objects.all().select_related('association')
    else :
        members = Adherent.objects.filter(association__slug=asso_slug).select_related('association')
        import pdb; pdb.set_trace()
    return render(request, 'adherents.html', {'members':members})

def associations(request, asso_slug=None):
    if not asso_slug:
        associations = Association.objects.all()
    else :
        associations = Association.objects.filter(slug=asso_slug)
    return render(request, 'associations.html', {'associations':associations})
