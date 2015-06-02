# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 09:08:44 2015

@author: Rafael
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:03:37 2015

@author: RGM
"""

from random import randint
from random import choice

placar_jogador=0
placar_computador=0
 
eu = ["papel", "pedra", "lagarto", "spock", "tesoura",]

while placar_jogador<3 or placar_computador <3:
    escolha_jogador=input("Preparado para a batalha?\n Escolha sua arma: Pedra, papel, tesoura, lagarto ou spock\n" )
    escolha_computador= choice (eu)
    print ("Minha escolha é:",escolha_computador)
    if escolha_jogador == "papel":
        if escolha_computador == "pedra"or escolha_computador== "spock":
            print("Sortudo... ganhou dessa vez!")
        placar_jogador +=1
        placar_computador +=0
        if escolha_computador =="lagarto" or escolha_computador == "tesoura":
            print ("Esse papel é inofencivo! hahaha")
        placar_jogador +=0
        placar_computador +=1
    if escolha_jogador == "pedra":
        if escolha_computador == "tesoura"or escolha_computador =="lagarto":
            print ("Humph... perdi!")
        placar_jogador += 1
        if escolha_computador == "spock"or escolha_computador == "papel":
            print ("O que você tentou fazer com essa pedrinha? Tente de novo")
        placar_jogador +=0
        placar_computador +=1
    if escolha_jogador =="tesoura":
        if escolha_computador == "lagarto"or escolha_computador == "papel":
            print ("Você ganhou dessa vez!")
        placar_jogador +=1
        placar_computador +=0
        if escolha_computador == "spock" or escolha_computador == "pedra":
            print ("Melhor você afiar essa tesourinha")
        placar_jogador +=0
        placar_computador +=1
    if escolha_jogador == "lagarto":
        if escolha_computador == "papel"or escolha_computador =="spock":
            print ("Você ganhou desta vez!")
        placar_jogador +=1
        placar_computador +=0
        if escolha_computador == "pedra"or escolha_computador == "tesoura":
            print ("Tá achando que é jacaré, mané?!!")
        placar_computador += 1
        placar_jogador +=0
    if escolha_jogador == "spock":
        if escolha_computador == "pedra"or escolha_computador=="tesoura":
            print ("Está com muita sorte hoje.. Ganhou essa rodada!")
        placar_jogador +=1
        if escolha_computador == "papel"or escolha_computador == "lagarto":
            print ("Seu spock é muito fraco pra mim...")
        placar_jogador +=0
        placar_computador +=1