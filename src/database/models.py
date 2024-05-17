from sqlalchemy import Column, Integer, String
from database.database import db

class Pedidos(db):
  __tablename__ = 'pedidos'

  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)
  usermail = Column(String(50), nullable=False)
  request_pedido = Column(String(300), nullable=False)

  def __repr__(self):
    return f'<Pedidos:[id:{self.id}, username:{self.username}, usermail:{self.usermail}, request_pedido:{self.request_pedido}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "username": self.username,
      "usermail": self.usermail,
      "request_pedido": self.request_pedido
      }