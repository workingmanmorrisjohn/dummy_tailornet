from pathlib import Path
import shutil
from typing import Dict

from src.config import TAILORNET_OBJ_DIR

async def generate_clothes(avatar_id: str, pkl_filepath: Path, avatar_gender: str) -> Dict[str, Path]:
    avatar_path = TAILORNET_OBJ_DIR / f"{avatar_id}_{avatar_gender}_avatar.obj"
    pants_path = TAILORNET_OBJ_DIR / f"{avatar_id}_{avatar_gender}_pants.obj"
    shirt_path = TAILORNET_OBJ_DIR / f"{avatar_id}_{avatar_gender}_shirt.obj"
    sleeves_path = TAILORNET_OBJ_DIR / f"{avatar_id}_{avatar_gender}_sleeves.obj"
    
    shutil.copy(pkl_filepath, avatar_path)
    shutil.copy(pkl_filepath, pants_path)
    shutil.copy(pkl_filepath, shirt_path)
    shutil.copy(pkl_filepath, sleeves_path)
    
    return {
        "avatar" : avatar_path,
        "pants" : pants_path,
        "shirt" : shirt_path,
        "sleeves" : sleeves_path
    }