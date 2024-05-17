from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from database.models import Pedidos
from database.database import SessionLocal
from fastapi.templating import Jinja2Templates
import uvicorn
from database.models import Pedidos
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from pydantic import BaseModel

class Pedido(BaseModel):
    username: str
    usermail: str
    request_pedido: str

templates = Jinja2Templates(directory="templates")

app = FastAPI()

async def get_async_db():
    db = SessionLocal()
    async with db as session:
        yield session


# Add dependencies to CRUD user endpoints to get current pedido
@app.get("/pedidos")
async def get_pedidos(db: Session = Depends(get_async_db)):
    async with db as session:

        pedidos = select(Pedidos)
        result = await session.execute(pedidos)
        pedidos = result.scalars().all()
    return pedidos

@app.get("/pedidos/{id}")
async def get_pedido(id: int, db: Session = Depends(get_async_db)):
    async with db as session:
        stmt = select(Pedidos).filter(Pedidos.id == id)
        try:
            result = await session.execute(stmt)
            pedido = result.scalars().one()
            return pedido
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Pedido not found")

@app.post("/pedidos")
async def create_pedido(pedido_data: Pedido, db: Session = Depends(get_async_db)):
    async with db as session:
        db_pedido = Pedidos(username=pedido_data.username, usermail=pedido_data.usermail, request_pedido=pedido_data.request_pedido)
        session.add(db_pedido)
        await session.commit()
        await session.refresh(db_pedido)
    return {"status": f"Pedido by user [{pedido_data.username}] created with id [{db_pedido.id}]"}
        
@app.put("/pedidos/{id}")
async def update_pedido(id: int, pedido_data: Pedido, db: Session = Depends(get_async_db)):
    async with db as session:
        db_pedido = await session.get(Pedidos, id)
        if not db_pedido:
            raise HTTPException(status_code=404, detail="Pedido not found")
        db_pedido.username = pedido_data.username
        db_pedido.usermail = pedido_data.usermail
        db_pedido.request_pedido = pedido_data.request_pedido
        await session.commit()
        return {"status": f"Pedido requested by user [{pedido_data.username}] with id [{id}] updated"}

@app.delete("/pedidos/{id}")
async def delete_pedido(id: int, db: Session = Depends(get_async_db)):
    async with db as session:
        db_pedido = await session.get(Pedidos, id)
        if not db_pedido:
            raise HTTPException(status_code=404, detail="Pedido not found")
        await session.delete(db_pedido)
        await session.commit()
        return {"status": f"Pedido with id [{id}] deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
