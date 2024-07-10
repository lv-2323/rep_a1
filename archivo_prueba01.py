print('hola mundo')
import random as rd

class Dado:
  def __init__(self,color):
    self.color=color
    self.valor=0
  def tirar(self):
    rdm=rd.randint(1,6)
    self.set_dado(rdm)
  def set_dado(self,nuValor):
    self.valor=nuValor:
  def get_dado(self):
    return self.valor
  def ver_resul(self):
    print(self.get_dado())