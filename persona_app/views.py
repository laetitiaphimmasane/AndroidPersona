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
    payload = ""
    
    def get(self, request):
        r = requests.get("https://randomuser.me/api?nat=fr")
        personna = r.json['results'][0]
        print(personna)
    def post(self, request, data_a_poster):
        def post(self, request, data_a_poster):
        ##ici les données du form        
        payload = {'first_name': data_a_poster.name.first,
                   'last_name' : data_a_poster.name.last,
                   }
        r = requests.post("http://httpbin.org/post",data=payload)
        # if r.status_code == requests.codes.ok :
