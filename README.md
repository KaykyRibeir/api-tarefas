# 📌 API de Tarefas - FastAPI + SQLite

## 🚀 Descrição do Projeto

Este projeto é uma API REST desenvolvida com **FastAPI**, utilizando **SQLite** como banco de dados e **SQLAlchemy** como ORM.

A API permite o gerenciamento completo de tarefas, incluindo criação, listagem, atualização e remoção (CRUD).

---

## ⚙️ Tecnologias Utilizadas

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Pydantic
* Uvicorn

---

## 📁 Estrutura do Projeto

```
api-tarefas/
│
├── main.py          # Rotas da API
├── models.py        # Modelos do banco de dados
├── schemas.py       # Validação de dados (Pydantic)
├── crud.py          # Operações do banco (CRUD)
├── database.py      # Conexão com SQLite
├── tarefas.db       # Banco de dados local
├── requirements.txt # Dependências do projeto
```

---

## 📌 Funcionalidades

### ✔ Criar tarefa

### ✔ Listar tarefas

### ✔ Buscar tarefa por ID

### ✔ Atualizar tarefa

### ✔ Deletar tarefa

### ✔ Filtrar tarefas concluídas e pendentes

---

## 🔗 Endpoints da API

### 📍 Home

```
GET /
```

---

### 📍 Criar tarefa

```
POST /tarefas
```

```json
{
  "titulo": "Estudar FastAPI",
  "descricao": "Aprender CRUD com SQLite",
  "concluida": false
}
```

---

### 📍 Listar tarefas

```
GET /tarefas
```

---

### 📍 Buscar tarefa por ID

```
GET /tarefas/{id}
```

---

### 📍 Atualizar tarefa

```
PUT /tarefas/{id}
```

---

### 📍 Deletar tarefa

```
DELETE /tarefas/{id}
```

---

### 📍 Filtros

```
GET /tarefas/concluidas
GET /tarefas/pendentes
```

---

## ▶️ Como executar o projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Rodar a aplicação

```bash
uvicorn main:app --reload
```

### 3. Acessar no navegador

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Aprendizados

Este projeto foi desenvolvido para praticar:

* Criação de APIs com FastAPI
* Integração com banco de dados SQLite
* Uso de ORM (SQLAlchemy)
* Estruturação de projetos backend
* Boas práticas em APIs REST

---

## 👨‍💻 Autor

Desenvolvido por Kayky Ribeiro
