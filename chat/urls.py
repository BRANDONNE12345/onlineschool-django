from django.urls import path
from .views import chat_de_classe_detail, chat_b2b_detail, send_message_classe, send_message_b2b, dashboard_chat

app_name = 'chat'

urlpatterns = [
    path('dashboard/', dashboard_chat, name='dashboard_chat'),
    path('classe/<int:chat_id>/', chat_de_classe_detail, name='chat_de_classe_detail'),
    path('classe/<int:chat_id>/send/', send_message_classe, name='send_message_classe'),
    path('b2b/<int:chat_id>/', chat_b2b_detail, name='chat_b2b_detail'),
    path('b2b/<int:chat_id>/send/', send_message_b2b, name='send_message_b2b'),
]
