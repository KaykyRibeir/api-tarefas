from pydantic import BaseModel

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False

class TarefaCreate(TarefaBase):
    pass

class TarefaResponse(TarefaBase):
    id: int

    class Config:
        orm_mode = True