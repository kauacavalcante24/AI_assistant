from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Usuário',
        null=True,
        blank=True
    )
    message = models.TextField(verbose_name='Mensagem')
    response = models.TextField(verbose_name='Resposta')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    class Meta:
        verbose_name = 'Conversa'
        verbose_name_plural = 'Conversas'

    def __str__(self):
        return f'{self.user}: {self.message}'
