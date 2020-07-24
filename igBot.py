from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Parte da blibioteta que vai simular teclas do teclado
import time # biblioteca pra esperar tempo
import random #Possibilida gerar valores aleatorios

class InstagramBot:
    def __init__(self, username, password):
        self.username = username 
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        
        time.sleep(10)
        
        campo_user = driver.find_element_by_xpath('//input[@name="username"]')
        campo_user.click()
        campo_user.clear()
        time.sleep(1)
        campo_user.send_keys(self.username)
        time.sleep(2)

        campo_senha = driver.find_element_by_xpath('//input[@name="password"]')
        campo_senha.click()
        campo_senha.clear()
        time.sleep(1)
        campo_senha.send_keys(self.password)
        time.sleep(2)

        campo_senha.send_keys(Keys.RETURN)

    def login_face(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        
        time.sleep(8)

        campo_face = driver.find_element_by_xpath('//span[contains(text(), "Entrar com o Facebook")]')
        campo_face.click()
        time.sleep(5)

        campo_user = driver.find_element_by_xpath('//input[@placeholder="Email ou telefone"]')
        campo_user.click()
        campo_user.clear()
        time.sleep(1)
        campo_user.send_keys(self.username)
        time.sleep(2)

        campo_senha = driver.find_element_by_xpath('//input[@placeholder="Senha"]')
        campo_senha.click()
        campo_senha.clear()
        time.sleep(1)
        campo_senha.send_keys(self.password)
        time.sleep(1)

        campo_senha.send_keys(Keys.RETURN)

        time.sleep(2)
        self.comentar()

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep((random.randint(1,2))/2) 


    def comentar(self):
        driver = self.driver
        try:
            #driver.get("https://www.instagram.com/p/B_1BX_OF8cp/?utm_source=ig_web_copy_link") #link
            driver.get("https://www.instagram.com/p/CC-IjbAhuEy/?utm_source=ig_web_copy_link") #link
            time.sleep(2)
            print("entrou na publicação!")    
        except Exception as err:
            print("Erro ao entrar na publicação: ", err)
        
        time.sleep(3)

        try:
            element = driver.find_element_by_xpath('//div[@class="RxpZH"]/span/a[1]')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            print("Entrou com facebook")
        except Exception as err:
            print("Erro ao entrar com facebook: ", err)
        
        time.sleep(3)
        
        try:
            driver.find_element_by_xpath('//div[contains(text(), "Continuar como ramonalves1357")]').click()
            time.sleep(3)
            print("Deu certo ao Confirmar")
        except Exception as err:
            print("Erro ao confirmar. Erro: ", err)
        
        time.sleep(3)

        # try:
        #     comentarios = ["Eu quero", "Já ganhei", "É meu", "Quero ganhar", "Azul", "Ramon", "Gabriel", "Rafael", "Davi", "Bruna", "Valentina", "São Paulo", "Zebra", "Cachorro", "Gato", "Leão", "Papagaio", "Amazonas", "Paraiba", "Vaca", "Cajá", "Melão", "Melancia", "Abacate", "Coco" , "Banana", "Manga", "Mateus", "Uva"]

        #     j = int(len(comentarios))
        #     print("j: ", j)

        #     for a in range(1, 100000):
        #         print ("Comentario: ", a)
                
        #         i = random.randint(0, int(len(comentarios)))
        #         print("Comentario escolhido: ", comentarios[i])
        #         print("Posição: ", i)

        #         driver.find_element_by_xpath('//textarea[@placeholder="Adicione um comentário..."]').click()
        #         campo_comentario = driver.find_element_by_xpath('//textarea[@placeholder="Adicione um comentário..."]')
        #         time.sleep((random.randint(1, 3))/2)
                
        #         self.digite_como_uma_pessoa(comentarios[i], campo_comentario)
        #         time.sleep(random.randint(8,13))

        #         driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
        #         time.sleep(3)
        
        # except Exception as err:
        #     print("Ouve um erro: ", err)

        
        comentarios = ["Eu quero", "Já ganhei", "É meu", "Quero ganhar", "Azul", "Ramon", "Guilherme", "Lidiane", "Gabriel", "Alice", "Miguel", "Sophia", "Arthur", "Helena", "Bernardo", "Valentina", "Heitor", "Laura", "Davi", "Isabella", "Lorenzo", "Manuela", "Théo", "Júlia", "Pedro", "Heloísa", "Gabriel", "Luiza", "Enzo", "Maria Luiza","Lorena", "Lucas", "Lívia", "Benjamin", "Giovanna", "Nicolas", "Guilherme", "Beatriz", "Joaquim", "Davi", "Bruna", "Valentina", "São Paulo", "Zebra", "Cachorro", "Gato", "Leão", "Papagaio", "Amazonas", "Paraiba", "Vaca", "Cajá", "Melão", "Melancia", "Abacate", "Coco" , "Banana", "Manga", "Mateus", "Uva"]

        j = int(len(comentarios))
        print("j: ", j)

        for a in range(1, 100000):
              try:
                print ("Comentario: ", a)
            
                i = random.randint(0, int(len(comentarios)))
                
                print("Comentario escolhido: ", comentarios[i])
                print("Posição: ", i, "\n")

                driver.find_element_by_xpath('//textarea[@placeholder="Adicione um comentário..."]').click()
                campo_comentario = driver.find_element_by_xpath('//textarea[@placeholder="Adicione um comentário..."]')
                time.sleep((random.randint(1, 3))/2)
                
                self.digite_como_uma_pessoa(comentarios[i], campo_comentario)
                time.sleep(6)


                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(random.randint(20,22))
              except Exception as err:
                print("Erro: ", err)
                driver.refresh()
                time.sleep(6)
                print("Refresh \n")

StartBot = InstagramBot("ramon81062213@hotmail.com", "81326776")
StartBot.login_face()

"""
Traceback (most recent call last):
  File "c:/Users/ramon/Desktop/BootInstagram/igBot.py", line 158, in <module>  
    StartBot.login_face()
  File "c:/Users/ramon/Desktop/BootInstagram/igBot.py", line 61, in login_face 
    self.comentar()
  File "c:/Users/ramon/Desktop/BootInstagram/igBot.py", line 143, in comentar  
    driver.find_element_by_xpath('//textarea[@placeholder="Adicione um comentário..."]').click()
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\webdriver.py", 
line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementClickInterceptedException: Message: Element <textarea class="Ypffh focus-visible"> is not clickable at point (948,440) because another element <form class="X7cDz"> obscures it
"""
