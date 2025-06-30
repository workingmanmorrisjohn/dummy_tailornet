from decouple import config

TEMP_FILES_DIR = config('TEMP_FILES_DIR', default='nothing found')

RAW_OBJS_DIR = TEMP_FILES_DIR / "raw_objs"
CORRECT_ORIENTATION_DIR = TEMP_FILES_DIR / "correct_orientation"
REGISTERED_OBJ_DIR = TEMP_FILES_DIR / "registered"
TAILORNET_OBJ_DIR = TEMP_FILES_DIR / "tailornet_objs"
TAILORNET_GLTF_DIR = TEMP_FILES_DIR / "tailornet_gltf"