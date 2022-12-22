from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from fit.models import Post 
from fit.forms import UsuarioForm
from django.urls import reverse_lazy
from fit.models import Perfil
from django.shortcuts import get_object_or_404
import math
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")


tdee = 0
def add(request):

    
    genero = int(request.POST["genero"])
    anos = str(request.POST["anos"])
    altura = str(request.POST["altura"])
    peso = str(request.POST["peso"])
    atividade = int(request.POST["atividade"])


    if anos == "" or altura == "" or peso == "":
            return render(request,"calculadora.html")

    anos = float(request.POST["anos"])
    altura = float(request.POST["altura"])
    peso = float(request.POST["peso"])
    imc = round(peso / (altura/100*altura/100),1)


    if genero == 1:
        tmb = round(float((13.67*peso)+(5*altura)-(6.76* anos)+66.5))
        if atividade ==1:
            tdee = round(float(tmb*1.2))
        elif atividade ==2:
            tdee = round(float(tmb*1.375))
        elif atividade ==3:
            tdee = round(float(tmb*1.55))
        elif atividade ==4:
            tdee =round(float(tmb*1.725))
        else:
            tdee = round(float(tmb*1.9))

        tdee_semana = round(float(tdee*7))
        tdee_sedentario = round(float(tmb*1.2))
        tdee_ExeLeve = round(float(tmb*1.375))
        tdee_ExeMOderado = round(float(tmb*1.55))
        tdee_ExePesado = round(float(tmb*1.725))
        tdee_atleta = round(float(tmb*1.9))

        



    else:
        tmb = round(float((9.56*peso)+(1.85*altura)-(4.68* anos)+66.5))
        if atividade ==1:
            tdee = round(float(tmb*1.2))
        elif atividade ==2:
            tdee = round(float(tmb*1.375))
        elif atividade ==3:
            tdee = round(float(tmb*1.55))
        elif atividade ==4:
            tdee =round(float(tmb*1.725))
        else:
            tdee = round(float(tmb*1.9))

        tdee_semana = round(float(tdee*7))
        tdee_sedentario = round(float(tmb*1.2))
        tdee_ExeLeve = round(float(tmb*1.375))
        tdee_ExeMOderado = round(float(tmb*1.55))
        tdee_ExePesado = round(float(tmb*1.725))
        tdee_atleta = round(float(tmb*1.9))

        
    BFPm = round(float((1.20 * imc) + (0.23 * anos) - 16.2))
    ffmim =  round(float( peso * (1-(BFPm/100)) ))
    BFPh = round(float((1.20 * imc) + (0.23 * anos) - 5.4))
    ffmi =  round(float((peso*(1-(BFPh/100)))/altura*altura))
    cutting = round(float(tdee - 500))
    bulking = round(float(tdee + 500))
    manutenção1= round(float(tdee*0.55)/4)
    manutenção2= round(float(tdee*0.25)/4)
    manutenção3= round(float(tdee*0.20)/9)
    cutting1= round(float(cutting*0.55)/4)
    cutting2= round(float(cutting*0.25)/4)
    cutting3= round(float(cutting*0.20)/9)
    bulking1= round(float(bulking*0.55)/4)
    bulking2= round(float(bulking*0.25)/4)
    bulking3= round(float(bulking*0.20)/9)

    manutenção11= round(float(tdee*0.45)/4)
    manutenção21= round(float(tdee*0.25)/4)
    manutenção31= round(float(tdee*0.30)/9)
    cutting11= round(float(cutting*0.45)/4)
    cutting21= round(float(cutting*0.25)/4)
    cutting31= round(float(cutting*0.30)/9)
    bulking11= round(float(bulking*0.45)/4)
    bulking21= round(float(bulking*0.25)/4)
    bulking31= round(float(bulking*0.30)/9)

    manutenção111= round(float(tdee*0.45)/4)
    manutenção211= round(float(tdee*0.35)/4)
    manutenção311= round(float(tdee*0.20)/9)
    cutting111= round(float(cutting*0.45)/4)
    cutting211= round(float(cutting*0.35)/4)
    cutting311= round(float(cutting*0.20)/9)
    bulking111= round(float(bulking*0.45)/4)
    bulking211= round(float(bulking*0.35)/4)
    bulking311= round(float(bulking*0.20)/9)



        
    tupla = (tdee,tdee_semana,tmb,tdee_sedentario,tdee_ExeLeve,tdee_ExeMOderado,tdee_ExePesado,
    tdee_atleta,imc,BFPm,ffmim,BFPh,ffmi,cutting,bulking,
    manutenção1,manutenção2,manutenção3,cutting1,cutting2,cutting3,bulking1,bulking2,bulking3,
    manutenção11,manutenção21,manutenção31,cutting11,cutting21,cutting31,bulking11,bulking21,bulking31,
    manutenção111,manutenção211,manutenção311,cutting111,cutting211,cutting311,bulking111,bulking211,bulking311)
    return render(request,"output.html", {"tupla":tupla})

def user(request):
    return render(request,"user.html")
    
def signup(request):
    return render(request,"sign-up.html")

def calculadora(request):
    id =  request.user.id
    objeto = Perfil.objects.filter(usuario__id = id )

    variaveis = objeto.values()
    #print(variaveis['genero'])
    global peso
    peso =1
    global altura
    altura =1
    global genero
    genero =1
    global anos
    anos =1
    global atividade
    atividade =1
    for valores in objeto.values():
        
        genero = valores['genero']
        anos = valores['idade']
        peso = valores['peso']
        altura = valores['altura']
        atividade = valores['atividade_fisica']  
    

    imc = round(float(float(peso) / (float(altura)/100*float(altura)/100)),1)


    if genero == "Masculino":
        tmb = round(float((13.67*float(peso))+(5*float(altura))-(6.76* float(anos))+66.5))
        if atividade =="sedentario":
            tdee = round(float(tmb*1.2))
        elif atividade =="levemente ativo":
            tdee = round(float(tmb*1.375))
        elif atividade =="moderadamente":
            tdee = round(float(tmb*1.55))
        elif atividade =="muito ativo":
            tdee =round(float(tmb*1.725))
        else:
            tdee = round(float(tmb*1.9))

        tdee_semana = round(float(tdee*7))
        tdee_sedentario = round(float(tmb*1.2))
        tdee_ExeLeve = round(float(tmb*1.375))
        tdee_ExeMOderado = round(float(tmb*1.55))
        tdee_ExePesado = round(float(tmb*1.725))
        tdee_atleta = round(float(tmb*1.9))

        



    else:
        tmb = round(float((9.56*float(peso))+(1.85*float(altura))-(4.68* float(anos))+66.5))
        if atividade ==1:
            tdee = round(float(tmb*1.2))
        elif atividade ==2:
            tdee = round(float(tmb*1.375))
        elif atividade ==3:
            tdee = round(float(tmb*1.55))
        elif atividade ==4:
            tdee =round(float(tmb*1.725))
        else:
            tdee = round(float(tmb*1.9))

        tdee_semana = round(float(tdee*7))
        tdee_sedentario = round(float(tmb*1.2))
        tdee_ExeLeve = round(float(tmb*1.375))
        tdee_ExeMOderado = round(float(tmb*1.55))
        tdee_ExePesado = round(float(tmb*1.725))
        tdee_atleta = round(float(tmb*1.9))

        
    BFPm = round(float((1.20 * imc) + (0.23 * float(anos)) - 16.2))
    ffmim =  round(float( float(peso) * (1-(BFPm/100)) ))
    BFPh = round(float((1.20 * imc) + (0.23 * float(anos)) - 5.4))
    ffmi =  round(float((float(peso)*(1-(BFPh/100)))/float(altura)*float(altura)))
    cutting = round(float(tdee - 500))
    bulking = round(float(tdee + 500))
    manutenção1= round(float(tdee*0.55)/4)
    manutenção2= round(float(tdee*0.25)/4)
    manutenção3= round(float(tdee*0.20)/9)
    cutting1= round(float(cutting*0.55)/4)
    cutting2= round(float(cutting*0.25)/4)
    cutting3= round(float(cutting*0.20)/9)
    bulking1= round(float(bulking*0.55)/4)
    bulking2= round(float(bulking*0.25)/4)
    bulking3= round(float(bulking*0.20)/9)

    manutenção11= round(float(tdee*0.45)/4)
    manutenção21= round(float(tdee*0.25)/4)
    manutenção31= round(float(tdee*0.30)/9)
    cutting11= round(float(cutting*0.45)/4)
    cutting21= round(float(cutting*0.25)/4)
    cutting31= round(float(cutting*0.30)/9)
    bulking11= round(float(bulking*0.45)/4)
    bulking21= round(float(bulking*0.25)/4)
    bulking31= round(float(bulking*0.30)/9)

    manutenção111= round(float(tdee*0.45)/4)
    manutenção211= round(float(tdee*0.35)/4)
    manutenção311= round(float(tdee*0.20)/9)
    cutting111= round(float(cutting*0.45)/4)
    cutting211= round(float(cutting*0.35)/4)
    cutting311= round(float(cutting*0.20)/9)
    bulking111= round(float(bulking*0.45)/4)
    bulking211= round(float(bulking*0.35)/4)
    bulking311= round(float(bulking*0.20)/9)



        
    tupla = (tdee,tdee_semana,tmb,tdee_sedentario,tdee_ExeLeve,tdee_ExeMOderado,tdee_ExePesado,
    tdee_atleta,imc,BFPm,ffmim,BFPh,ffmi,cutting,bulking,
    manutenção1,manutenção2,manutenção3,cutting1,cutting2,cutting3,bulking1,bulking2,bulking3,
    manutenção11,manutenção21,manutenção31,cutting11,cutting21,cutting31,bulking11,bulking21,bulking31,
    manutenção111,manutenção211,manutenção311,cutting111,cutting211,cutting311,bulking111,bulking211,bulking311)


    return render(request,"calculadora.html", {'tupla':tupla})

def blog(request):
    posts = Post.objects.all()
    return render(request,"blog.html", {'posts':posts})

def sobrenos(request):
    return render(request,"sobre-nos.html")

def postagemblog(request, post_id):
    post =Post.objects.get(pk=post_id)
    return render(request,"postagem-blog.html",{'post':post})

class UsuarioCreate(CreateView):
    template_name = "sign-up.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Docente")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url


    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['botao'] = "cadastro"

        return context


class PerfilUpdate(UpdateView):
    template_name = "atualizar.html"
    model = Perfil
    fields = ['genero','idade','peso','altura','atividade_fisica']
    success_url = reverse_lazy("calculadora")
    


    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil,usuario=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context["botao"] = "atualizar"

        return context

        ###