from django.shortcuts import render, redirect
from .models import Network, Show

# Create your views here.
#initial index requests
def index(request):
    return redirect('/shows')
# First route after request
def new(request):
    return render(request, 'new.html')

#### Builds list of all shows
def all_shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

#### Single Show pages
# Sends selected show id for single show display
def one_show(request, id):
    context= {
        'curr_show': Show.objects.get(id=id)
    }
    return render(request, 'one_show.html', context)

# Sends selected show id for show edit form fill
def edit_show_page(request, id):
    context= {
        'curr_show': Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)


#### POST redirects for form fills and creation
# Create a new show but validating if network or show exists
def create_show(request):
    if request.method == "POST":

        # Check if network exists
        known_network = False
        input_network = request.POST['network']
        for network in Network.objects.all():
            if network.name == input_network:
                known_network = True

        # If network is new, create network object
        if known_network == False:
            working_network = Network.objects.create(name=input_network)
        else:
            working_network = Network.objects.get(name=input_network)
        
        # Check if Show object exists
        # for show in Show.objects.all():
        #     if show.title == request.POST['title']:
        #         return redirect('/shows/one_show')
        #     else:
                # Create Show object with 
        new_show = Show.objects.create(title=request.POST['title'], network=working_network, release_date=request.POST['release_date'], desc=request.POST['desc'])
        print(new_show.title)
        return redirect('/shows/'+str(new_show.id))
    print("Show was not created")
    return redirect('/shows/new')

# POST redirect from show_edit_page
def process_edit(request, id):
    if request.method == 'POST':
        # curr_network = Network.object.get(name=request.POST['network'])
        edit_show = Show.objects.get(id=id)
        edit_show.title = request.POST['title']
        # edit_show.network = Network.objects.get(name=request.POST['network'])
        # edit_show.network = curr_network
        edit_show.release_date = request.POST['release_date']
        edit_show.desc = request.POST['desc']
        edit_show.save()
        return redirect('/shows')

# Removes show from DB
def delete_show(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')