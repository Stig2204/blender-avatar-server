from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess
import uuid
import shutil

app = FastAPI()

class InjectRequest(BaseModel):
    avatar_url: str

@app.post("/inject")
async def inject_avatar(data: InjectRequest):
    avatar_id = str(uuid.uuid4())
    input_path = f"/tmp/{avatar_id}.glb"
    output_path = f"/tmp/{avatar_id}_animated.glb"

    # Télécharger le fichier .glb
    subprocess.run(["curl", "-o", input_path, data.avatar_url])

    # Lancer Blender en CLI pour injecter l'animation
    subprocess.run([
        "blender", "--background", "--python", "blender_inject.py", "--",
        input_path, output_path
    ])

    # Retourner le fichier animé
    return {
        "success": True,
        "result": f"/static/{avatar_id}_animated.glb"
    }
