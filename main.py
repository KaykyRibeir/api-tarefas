from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Tarefas",
    description="API com SQLite e FastAPI",
)

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota inicial
@app.get("/")
def home():
    return {
        "mensagem": "API de Tarefas rodando 🚀",
        "docs": "/docs"
    }

# Criar tarefa
@app.post("/tarefas", response_model=schemas.TarefaResponse)
def criar_tarefa(
    tarefa: schemas.TarefaCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_tarefa(db, tarefa)

# Listar tarefas
@app.get("/tarefas", response_model=list[schemas.TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return crud.listar_tarefas(db)

# 🔵 TAREFAS CONCLUÍDAS
@app.get("/tarefas/concluidas", response_model=list[schemas.TarefaResponse])
def tarefas_concluidas(db: Session = Depends(get_db)):
    return db.query(models.Tarefa).filter(models.Tarefa.concluida == True).all()

# 🟡 TAREFAS PENDENTES
@app.get("/tarefas/pendentes", response_model=list[schemas.TarefaResponse])
def tarefas_pendentes(db: Session = Depends(get_db)):
    return db.query(models.Tarefa).filter(models.Tarefa.concluida == False).all()

# Buscar tarefa por ID
@app.get("/tarefas/{tarefa_id}", response_model=schemas.TarefaResponse)
def buscar_tarefa(
    tarefa_id: int,
    db: Session = Depends(get_db)
):
    tarefa = crud.buscar_tarefa(db, tarefa_id)

    if not tarefa:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return tarefa

# Atualizar tarefa
@app.put("/tarefas/{tarefa_id}", response_model=schemas.TarefaResponse)
def atualizar_tarefa(
    tarefa_id: int,
    dados: schemas.TarefaCreate,
    db: Session = Depends(get_db)
):
    tarefa = crud.atualizar_tarefa(db, tarefa_id, dados)

    if not tarefa:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return tarefa

# 🔴 DELETAR (melhorado)
@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(
    tarefa_id: int,
    db: Session = Depends(get_db)
):
    tarefa = crud.deletar_tarefa(db, tarefa_id)

    if not tarefa:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return {
        "status": "sucesso",
        "mensagem": "Tarefa deletada com sucesso",
        "id": tarefa_id
    }