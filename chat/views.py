from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatDeClasse, MessageClasse, ChatB2B, MessageB2B

@login_required
def chat_de_classe_detail(request, chat_id):
    chat = get_object_or_404(ChatDeClasse, id=chat_id)
    messages = chat.messages.all().order_by('date_envoye')

    return render(request, 'chat/chat_detail.html', {
        'active_chat': chat,  # 👈 Vérifie que active_chat est bien envoyé
        'messages': messages,
        'chat_de_classe_list': ChatDeClasse.objects.all(),
        'chat_b2b_list': ChatB2B.objects.all(),
    })

@login_required
def chat_b2b_detail(request, chat_id):
    chat = get_object_or_404(ChatB2B, id=chat_id)
    messages = chat.messages.all().order_by('date_envoye')

    return render(request, 'chat/chat_detail.html', {
        'active_chat': chat,
        'messages': messages,
        'chat_de_classe_list': ChatDeClasse.objects.all(),
        'chat_b2b_list': ChatB2B.objects.all(),
    })

@login_required
def send_message_classe(request, chat_id):
    if request.method == "POST":
        chat = get_object_or_404(ChatDeClasse, id=chat_id)
        contenu = request.POST.get("contenu")
        if contenu:
            MessageClasse.objects.create(chat=chat, auteur=request.user, contenu=contenu)
        return redirect('chat:chat_de_classe_detail', chat_id=chat.id)

@login_required
def send_message_b2b(request, chat_id):
    if request.method == "POST":
        chat = get_object_or_404(ChatB2B, id=chat_id)
        contenu = request.POST.get("contenu")
        if contenu:
            MessageB2B.objects.create(chat=chat, auteur=request.user, contenu=contenu)
        return redirect('chat:chat_b2b_detail', chat_id=chat.id)

@login_required
def dashboard_chat(request):
    chat_de_classe_list = ChatDeClasse.objects.all()
    chat_b2b_list = ChatB2B.objects.all()

    # Sélectionner un chat actif par défaut
    active_chat = None
    messages = []

    if chat_de_classe_list.exists():
        active_chat = chat_de_classe_list.first()
    elif chat_b2b_list.exists():
        active_chat = chat_b2b_list.first()

    # Charger les messages du chat actif
    if active_chat:
        messages = active_chat.messages.all().order_by('date_envoye')

    return render(request, 'chat/dashboard_chat.html', {
        'chat_de_classe_list': chat_de_classe_list,
        'chat_b2b_list': chat_b2b_list,
        'active_chat': active_chat,
        'messages': messages,
    })
