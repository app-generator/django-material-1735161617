# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Empresa(models.Model):

    #__Empresa_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Empresa_FIELDS__END

    class Meta:
        verbose_name        = _("Empresa")
        verbose_name_plural = _("Empresa")


class Colaborador(models.Model):

    #__Colaborador_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    funcao = models.ForeignKey(TipoColaborador, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    turno = models.CharField(max_length=255, null=True, blank=True)

    #__Colaborador_FIELDS__END

    class Meta:
        verbose_name        = _("Colaborador")
        verbose_name_plural = _("Colaborador")


class Tipocolaborador(models.Model):

    #__Tipocolaborador_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Tipocolaborador_FIELDS__END

    class Meta:
        verbose_name        = _("Tipocolaborador")
        verbose_name_plural = _("Tipocolaborador")


class Veiculo(models.Model):

    #__Veiculo_FIELDS__
    placa = models.CharField(max_length=255, null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    disponivel = models.BooleanField()

    #__Veiculo_FIELDS__END

    class Meta:
        verbose_name        = _("Veiculo")
        verbose_name_plural = _("Veiculo")


class Tipoveiculo(models.Model):

    #__Tipoveiculo_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Tipoveiculo_FIELDS__END

    class Meta:
        verbose_name        = _("Tipoveiculo")
        verbose_name_plural = _("Tipoveiculo")


class Turno(models.Model):

    #__Turno_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)
    inicio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fim = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Turno_FIELDS__END

    class Meta:
        verbose_name        = _("Turno")
        verbose_name_plural = _("Turno")


class Servico(models.Model):

    #__Servico_FIELDS__
    equipe = models.CharField(max_length=255, null=True, blank=True)
    data_inicio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data_fim = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Servico_FIELDS__END

    class Meta:
        verbose_name        = _("Servico")
        verbose_name_plural = _("Servico")


class Equipe(models.Model):

    #__Equipe_FIELDS__
    colaboradores = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    veiculos = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    #__Equipe_FIELDS__END

    class Meta:
        verbose_name        = _("Equipe")
        verbose_name_plural = _("Equipe")


class Roteirizacao(models.Model):

    #__Roteirizacao_FIELDS__
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    destino = models.CharField(max_length=255, null=True, blank=True)
    data_hora_inicio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data_hora_fim = models.DateTimeField(blank=True, null=True, default=timezone.now)
    distancia_km = models.IntegerField(null=True, blank=True)

    #__Roteirizacao_FIELDS__END

    class Meta:
        verbose_name        = _("Roteirizacao")
        verbose_name_plural = _("Roteirizacao")


class Custo(models.Model):

    #__Custo_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)
    valor = models.BooleanField()
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    #__Custo_FIELDS__END

    class Meta:
        verbose_name        = _("Custo")
        verbose_name_plural = _("Custo")


class Projecaotrabalho(models.Model):

    #__Projecaotrabalho_FIELDS__
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    estimativa_tempo_horas = models.IntegerField(null=True, blank=True)
    estimativa_custo = models.IntegerField(null=True, blank=True)

    #__Projecaotrabalho_FIELDS__END

    class Meta:
        verbose_name        = _("Projecaotrabalho")
        verbose_name_plural = _("Projecaotrabalho")



#__MODELS__END
