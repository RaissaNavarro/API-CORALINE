from fastapi import FastAPI, HTTPException, status, Response, Path, Header, Query, Depends
from model import Coraline
from typing import Optional, Any, List

app = FastAPI()

personagens = {
    1:{
        "id" : 1,
        "nome" : "Coraline",
        "Interpretador" : "Dakota Fanning",
        "Parentesco" : "A PRÓPRIA"
        
    },
    2:{
        "id" : 2,
        "nome" : "Wybie Lovat",
        "Interpretador" : "Bruno Pinasco",
        "Parentesco" : "Amigo da Coraline"
    },
    3:{
        "id" : 3,
        "nome" : "Mãe",
        "Interpretador" : "Teri Hatcher",
        "Parentesco" : "Mãe de Verdade"
    },
    4:{
        "id" : 4,
        "nome" : "Pai",
        "Interpretador" : "Jonh Hodgman",
        "Parentesco" : "Pai da Coraline"
    },
    5:{
        "id" : 5,
        "nome" : "Gato",
        "Interpretador" : "Keith David",
        "Parentesco" : "Gato parceiro da Coraline e do Wybie"
    },
    6:{
        "id" : 6,
        "nome" : "Sr. Bobinsky",
        "Interpretador" : "Ian McShane",
        "Parentesco" : "Vizinho dono do Circo de Camudongos"
    },
    7:{
        "id" : 7,
        "nome" : "Srta Spink",
        "Interpretador" : "Jennifer Saunders",
        "Parentesco" : "Vizinha que usa andador"
    },
    8:{
        "id" : 8,
        "nome" : "Srta Forcible",
        "Interpretador" : "Dawn French",
        "Parentesco" : "Vizinha que usa óculos"
    },
    9:{
        "id" : 9,
        "nome" : "Outra Mãe {BELA DAMA}",
        "Interpretador" : "Teri Hatcher",
        "Parentesco" : "Mãe de Mentira e Malvada"
    },
    10:{
        "id" : 10,
        "nome" : "Outro Pai",
        "Interpretador" : "Jonh Hodgman",
        "Parentesco" : "Pai de Mentira"
    },
    11:{
        "id" : 11,
        "nome" : "Garoto Fantasma",
        "Interpretador" : "George Selick",
        "Parentesco" : "Garoto amigo com a alma presa dentro do espelho da Bela Dama"
    },
    12:{
        "id" : 12,
        "nome" : "Garota Fantasma Alta",
        "Interpretador" : "Hannah Kaiser",
        "Parentesco" : "Garota amiga com a alma presa dentro do espelho da Bela Dama"
    },
    13:{
        "id" : 13,
        "nome" : "Garota Fantasma Meiga",
        "Interpretador" : "Aankha Neal",
        "Parentesco" : "Garota amiga com a alma presa dentro do espelho da Bela Dama"
    },
    14:{
        "id" : 14,
        "nome" : "Avó de Wybie",
        "Interpretador" : "Caroline Crawford",
        "Parentesco" : "Avó de Wybie amigo de Coraline"
    }
}


def fake_coraline():
    try:
        print("Entrando no Mundo Secreto de Coraline")
    
    finally:
        print("Saindo do Mundo Secreto de Coraline")

@app.get("/personagens", summary="retorna todos os personagens") #Pegar todos os personagens
async def get_personagens_coraline(db: Any = Depends(fake_coraline)):
    return personagens

@app.get("/personagens/{personagem_id}") # Pegar apenas um personagem
async def get_personagem_coraline(personagem_id: int = Path(..., title='ID do Personagem', description="O ID deve ser entre 1 e 14", gt=0, lt=15)):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="personagem não encontrado!")
    
@app.delete("/personagens/{personagem_id}") # Deletar um personagem
async def delete_personagem_coraline(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    
@app.delete("/personagens/{personagem_id}") # Deletar um personagem pelo id 
async def delete_personagem_coraline(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    
@app.post("/personagens", status_code=status.HTTP_201_CREATED) # Adicionar um personagem
async def post_personagem_coraline(personagem: Optional[Coraline] = None):
    try:
        next_id = len(personagens) + 1
        personagens[next_id] = personagem
        del personagem.id 
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Já existe um personagem com esse id")
    
@app.put("/personagens/{personagem_id}",status_code=status.HTTP_202_ACCEPTED)
async def put_personagem_coraline(personagem_id: int, personagem: Coraline):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem 
        personagem.id = personagem_id 
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, log_level="info", reload=True) #





