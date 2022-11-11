
import pygame
import os
from pygame import font
from random import randint
import random
pygame.init()

TELA_LARGURA = 1380
TELA_ALTURA = 640

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Fome Zero')

relogio = pygame.time.Clock()
FPS = 60

#Colocando a música de fundo do jogo

pygame.mixer.init()
pygame.mixer.music.load('musicafundo.mp3')
pygame.mixer.music.play()

movimento_esquerda = False
movimento_direita = False
movimento_Cima = False
movimento_Baixo = False

tela_fundo = (0, 0, 0)

def desenho_tela():
    fundo=(pygame.image.load('0.jpg'))
    tela.blit(fundo,(0,0))


class Lula(pygame.sprite.Sprite):
    def __init__(self, jogador_tipo, x, y, scale, velocidade):
    
        pygame.sprite.Sprite.__init__(self)
        self.vivo = True
        self.jogador_tipo = jogador_tipo
        self.velocidade = velocidade
        self.vel_y = 0
        self.direcao = 1
        self.virar = False
        self.animacao_lista = []
        self.frame_index = 0
        self.acao = 0
        self.atualizar_tempo = pygame.time.get_ticks()
        self.p=0
        h=0
        animacao_tipo = ['Parado', 'Correr' ]
        scale=1
        for animacao in animacao_tipo:
            temp_list = []
            numero_de_frames = len(os.listdir(f'img/{self.jogador_tipo}/{animacao}'))
            for i in range(numero_de_frames):
                img = pygame.image.load(f'img/{self.jogador_tipo}/{animacao}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animacao_lista.append(temp_list)

        self.image = self.animacao_lista[self.acao][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def comida(self):
        self.rect.x =randint(10,500)
        self.rect.y=randint(10,500)
    
    def mov(self,movimento_direita):
            dx=0
            if self.rect.x>randint(1500,100000):
                self.rect.x=-50
            dx = self.velocidade
            self.virar = False
            self.direcao = 1
            self.rect.x += dx
            

    def movimento(self, movimento_esquerda, movimento_direita, movimento_Cima, movimento_Baixo):


        dx = 0
        dy=0
        
        if movimento_esquerda and self.rect.x > 0:
            
            dx = -self.velocidade
            self.virar = True
            self.direcao = -1
            
        if movimento_direita and self.rect.x < 1300:

            dx = self.velocidade
            self.virar = False
            self.direcao = 1
        
        if movimento_Baixo and self.rect.y < 560:

            dy = self.velocidade
            self.virar = False
            self.direcao = 1
            
        if movimento_Cima and self.rect.y > 0:

            dy = -self.velocidade
            self.virar = False
            self.direcao = -1
            
        if movimento_esquerda and movimento_Baixo:
            self.virar = True
        
        if movimento_esquerda and movimento_Cima:
            self.virar = True
        
        self.rect.x += dx
        self.rect.y += dy
    def mov1(self, movimento_esquerda, movimento_direita, movimento_Cima, movimento_Baixo):


        dx = 0
        dy=0
        
        if movimento_esquerda:
            
            dx = -self.velocidade
            self.virar = True
            self.direcao = -1
            
        if movimento_direita:

            dx = self.velocidade
            self.virar = False
            self.direcao = 1
        
        if movimento_Baixo:

            dy = self.velocidade
            self.virar = False
            self.direcao = 1
            
        if movimento_Cima:

            dy = -self.velocidade
            self.virar = False
            self.direcao = -1
            
        if movimento_esquerda and movimento_Baixo:
            self.virar = True
        
        if movimento_esquerda and movimento_Cima:
            self.virar = True
        
        self.rect.x += dx
        self.rect.y += dy
       
        
    def atualizar_animacao(self):
            ANIMACAO_FRESH = 150

            self.image = self.animacao_lista[self.acao][self.frame_index]

            if pygame.time.get_ticks() - self.atualizar_tempo > ANIMACAO_FRESH:
                self.atualizar_tempo = pygame.time.get_ticks()
                self.frame_index += 1

            if self.frame_index >= len(self.animacao_lista[self.acao]):
                self.frame_index = 0

    def atualizar_acao(self, new_action):
        if new_action != self.acao:
                self.acao = new_action

                self.frame_index = 0
                self.atualizar_tempo = pygame.time.get_ticks()

    def desenho(self):
            tela.blit(pygame.transform.flip(self.image, self.virar, False), self.rect)

#personagens e seu local de imagens, local no mapa e velocidade
caminhao = Lula ('Caminhao',1280,0,2,2)
jogador = Lula('Lula', 50, 50, 2, 10)
inimigo = Lula('Bolsonaro', 500, 500, 2, 25)
jacare =  Lula('inimigo',50,200,2,5)
jacare1 = Lula('inimigo',-50,400,2,7)
jacare2 = Lula('inimigo',10,350,2,8)
jacare3 = Lula('inimigo',20,300,2,10)
jacare4 = Lula('inimigo',-30,250,2,9)
jacare5 = Lula('inimigo',50,250,2,8)
jacare6 = Lula('inimigo',-50,250,2,4)
jacare7 = Lula('inimigo',10,250,2,5)
jacare8 = Lula('inimigo',20,250,2,10)
jacare9 = Lula('inimigo',-30,250,2,11)
bife = Lula('Bife',100,100,5,0)
cerveja = Lula('Cerveja',150,50,5,0)
Fase = Lula('fase',100,520,2,0)
pegadinha = Lula ('pegadinha',1280, 480,2,0)

p=0
pontuacao=0
aleatorio=1
run = True
fase = 0
while run:
    
    txt= str(pontuacao)
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 60)
    txttela = fontesys.render(txt, 1, (0,0,0)) 
    tela.blit(txttela,(1300,0)) 
    pygame.display.update() 
    relogio.tick(FPS)
    
    desenho_tela()

    jogador.atualizar_animacao()
    jogador.desenho()
    '''if fase == -1:'''
    caminhao.desenho()
    if fase == 2:
        inimigo.desenho()
    if fase == 0 or fase == 2:
        jacare.desenho()
        jacare1.desenho()
        jacare2.desenho()
        jacare3.desenho()
        jacare4.desenho()
        jacare5.desenho()
        jacare6.desenho()
        jacare7.desenho()
        jacare8.desenho()
        jacare9.desenho()
    if fase ==1:
        Fase.desenho()
        pegadinha.desenho()
    if fase == 0 or fase == 2: 
     if aleatorio==0:
        bife.desenho()
     else:
        cerveja.desenho()
    if jogador.vivo:
            if movimento_esquerda or movimento_direita or movimento_Cima or movimento_Baixo:
                jogador.atualizar_acao(1)
            
                
            else:
             if fase == 2:
                #faz o bolsonaro se movimntar aleatoriamente atras do lula
               
                if inimigo.rect.x > jogador.rect.x:
                    inimigo.rect.x -= inimigo.velocidade
                if inimigo.rect.x < jogador.rect.x:
                    inimigo.rect.x += inimigo.velocidade
                if inimigo.rect.y > jogador.rect.y:
                    inimigo.rect.y -= inimigo.velocidade
                if inimigo.rect.y < jogador.rect.y:
                    inimigo.rect.y += inimigo.velocidade
                jogador.atualizar_acao(0)
                inimigo.atualizar_acao(0)
            '''if fase == -1:'''
            caminhao.mov1(True,False,False,True)
            jogador.movimento(movimento_esquerda, movimento_direita, movimento_Cima, movimento_Baixo)
            inimigo.movimento(movimento_direita, movimento_esquerda,movimento_Baixo ,movimento_Cima )
            jacare.mov(True)
            jacare1.mov(True)
            jacare2.mov(True)
            jacare3.mov(True)
            jacare4.mov(True)
            jacare5.mov(True)
            jacare6.mov(True)
            jacare7.mov(True)
            jacare8.mov(True)
            jacare9.mov(True)



   
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    run = False

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                            movimento_esquerda = True
                    if event.key == pygame.K_d:
                            movimento_direita = True
                    if event.key == pygame.K_w:
                            movimento_Cima = True
                    if event.key == pygame.K_s:
                            movimento_Baixo = True
                    
                    if event.key == pygame.K_ESCAPE:
                            run = False

            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                            movimento_esquerda = False
                    if event.key == pygame.K_d:
                            movimento_direita = False
                    if event.key == pygame.K_w:
                            movimento_Cima = False
                    if event.key == pygame.K_s:
                            movimento_Baixo = False
                            
            #se lula encontar com bolsonaro depois de 10 segudos que o jogo começou, o jogo acaba
            encontro = pygame.image.load('lulabolso.jpg')
            #aumenta o tamanho da imagem
            encontro = pygame.transform.scale(encontro, (1400, 700))
            
            if fase ==0 or fase ==2:
              if jogador.rect.colliderect(jacare.rect) or  jogador.rect.colliderect(jacare1.rect ) or  jogador.rect.colliderect(jacare2.rect ) or  jogador.rect.colliderect(jacare3.rect ) or  jogador.rect.colliderect(jacare4.rect ) or  jogador.rect.colliderect(jacare5.rect ) or  jogador.rect.colliderect(jacare6.rect ) or  jogador.rect.colliderect(jacare7.rect ) or  jogador.rect.colliderect(jacare8.rect ) or  jogador.rect.colliderect(jacare9.rect ):
                tela.blit(encontro, (0, 0))
                pygame.display.update()
                run = False
                print ('Você perdeu virou jacaré')
                
                #escreve na tela que o jogador perdeu
                pygame.font.init()
                fonte=pygame.font.get_default_font()
                fontesys=pygame.font.SysFont(fonte, 60)
                txttela = fontesys.render('VOCÊ PERDEU VIROU JACARE', 1, (255,0,0))
                tela.blit(txttela,(400,400))
                pygame.display.update()
               
                #muda o audio para o audio de derrota
                pygame.mixer.music.load('derrota.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.9)
                pygame.display.update()
                pygame.time.delay(5000)
                run = False
                pygame.quit()
            if jogador.rect.colliderect(inimigo.rect ) :
              if fase == 2:
                tela.blit(encontro, (0, 0))
                pygame.display.update()
                run = False
                print ('Você perdeu virou jacaré')
                
                #escreve na tela que o jogador perdeu
                pygame.font.init()
                fonte=pygame.font.get_default_font()
                fontesys=pygame.font.SysFont(fonte, 60)
                txttela = fontesys.render('VOCÊ PERDEU VIROU JACARE', 1, (255,0,0))
                tela.blit(txttela,(400,400))
                pygame.display.update()
               
                #muda o audio para o audio de derrota
                pygame.mixer.music.load('derrota.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.9)
                pygame.display.update()
                pygame.time.delay(5000)
                run = False
                pygame.quit()
            if fase == 0 or fase == 2: 
             if aleatorio==1:    
                if jogador.rect.colliderect(cerveja.rect):
                    pygame.display.update()
                    cerveja.comida()
                    pontuacao+=15
                    aleatorio=0 
             else:
                if jogador.rect.colliderect(bife.rect):
                    pygame.display.update()
                    bife.comida()
                    pontuacao+=15
                    aleatorio=1
    # se a pontuação for maior que 100, o jogo acaba
    if pontuacao>=14:
        fase = 1
        #Escreve na tela ache o portal para passar de fase
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 40)
        txttela = fontesys.render('Escolha um Lado', 1, (255,0,0))
        tela.blit(txttela,(500,400))
        run = True
        # coloca a imagem do portal para aparecer na tela no inicio do jogo
     
        if jogador.rect.colliderect(Fase.rect) :
            print ("fsi")
            fase=2
            pontuacao=0
        if jogador.rect.colliderect(pegadinha.rect) :
            print ("perdeu")
            fase=2
            pontuacao=0
    pygame.display.update()

pygame.quit()
