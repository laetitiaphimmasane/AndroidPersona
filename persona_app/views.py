from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Persona
import requests



class PersonaListView(View):
    template_name = 'persona_app/template_list.html'
    model = Persona

    def get(self, request):
        persona_list = self.model.objects.all().order_by('-id')
        return render(request, self.template_name, context={'persona_list': persona_list})

class PersonaDetailsView(View):
    template_name = 'persona_app/template_details.html'
    model = Persona

    def get(self, request, id):
        persona_details = self.model.objects.get(pk=id)
        return render(request, self.template_name, context= {'persona_details' : persona_details} )


class PersonaGenerate(View):
    new_persona= ""

    def get(self, request):
        r = requests.get(" https://randomuser.me/api?nat=fr")
        req = r.json()
        persona = req['results'][0]
        self.new_persona = Persona.objects.create(
            first_name = persona['name']['first'],
            last_name = persona['name']['last'],
            address_street = persona['location']['street']['name'],
            address_number = persona['location']['street']['number'],
            city = persona['location']['city'],
            country = persona['location']['country'],
            postcode = persona['location']['postcode'],
            email = persona['email'],
            username = persona['login']['username'],
            password = persona['login']['password'],
            age = persona['registered']['age'],
            picture = persona['picture']['thumbnail']
        )
        if r.status_code == requests.codes.ok:
            return redirect('url_persona_details', self.new_persona.id)
        #If r.status_code != 200
        return redirect('url_persona_list')




