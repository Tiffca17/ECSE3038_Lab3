from fastapi import FastAPI, Request, HTTPException, status
import uuid

app = FastAPI()

tanks =[]

@app.get("/tank")
def get_tanks():
    return tanks

@app.get("/tank/{id}")
async def get_tank_id(id:str):
    for i in tanks:
        if i["id"]==id:
            return i
        raise HTTPException(status_code=404, detail="Tank not found")
    
@app.post("/tank", status_code=status.HTTP_201_CREATED)
async def add_tank(request:Request):
    new_tank = await request.json()
    new_uuid = uuid.uuid4() 

    new_tank = {"id":str(new_uuid), **new_tank}
    tanks.append(new_tank)
    return(new_tank)

@app.patch("/tank/{id}", status_code=status.HTTP_200_OK)
async def alter_tanks(id:str, request: Request):
    alter_tank = await request.json()

    for i, tank in enumerate(tanks):
        if tank["id"] == id:
            alter_tank.pop("id",None)
            tanks[i] = {**tank, **alter_tank}
            return tanks[i]
        raise HTTPException(status_code=404, detail="Tank not found")

@app.delete("/tank/{id}", status_code=status.HTTP_200_OK)
def delete_tank(id:str):
    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
           del tanks[i]
           return()
    raise HTTPException(status_code=404, detail="Tank not found")
           
    
            
        

    
        