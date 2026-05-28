from sqlalchemy.orm import Session
import models
import schemas


def criar_tarefa(db: Session, tarefa: schemas.TarefaCreate):
    nova_tarefa = models.Tarefa(**tarefa.dict())

    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return nova_tarefa


def listar_tarefas(db: Session):
    return db.query(models.Tarefa).all()


def buscar_tarefa(db: Session, tarefa_id: int):
    return db.query(models.Tarefa).filter(
        models.Tarefa.id == tarefa_id
    ).first()


def atualizar_tarefa(db: Session, tarefa_id: int, dados: schemas.TarefaCreate):
    tarefa = buscar_tarefa(db, tarefa_id)

    if not tarefa:
        return None

    tarefa.titulo = dados.titulo
    tarefa.descricao = dados.descricao
    tarefa.concluida = dados.concluida

    db.commit()
    db.refresh(tarefa)

    return tarefa


def deletar_tarefa(db: Session, tarefa_id: int):
    tarefa = buscar_tarefa(db, tarefa_id)

    if not tarefa:
        return None

    db.delete(tarefa)
    db.commit()

    return {
        "id": tarefa_id,
        "status": "deletado"
    }