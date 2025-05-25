import bpy

# Configuration de la scène
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 16500  # 11 minutes à 25 fps
fps = 25

# Fonction pour créer une animation d'assemblage et de désassemblage avec annotations
def create_animation_with_annotations(obj, start_frame, mid_frame, end_frame, material_info):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)

    # Assemblage
    obj.location = (0, 0, -5)  # Commence en dessous
    obj.keyframe_insert(data_path="location", frame=start_frame)
    obj.location = (0, 0, 0)  # Se déplace vers la position d'origine
    obj.keyframe_insert(data_path="location", frame=mid_frame)

    # Ajout d'annotations
    bpy.ops.object.text_add(location=(0, 0, 5))
    annotation = bpy.context.object
    annotation.data.body = f"{obj.name}: {material_info}"
    annotation.data.size = 0.5
    annotation.data.align_x = 'CENTER'
    annotation.keyframe_insert(data_path="location", frame=mid_frame)
    annotation.keyframe_insert(data_path="location", frame=mid_frame + 50)  # Affichage de l'annotation
    annotation.location.z -= 10
    annotation.keyframe_insert(data_path="location", frame=end_frame - 50)
    annotation.location.z -= 20
    annotation.keyframe_insert(data_path="location", frame=end_frame)

    # Désassemblage
    obj.location = (0, 0, 0)  # Commence à la position d'origine
    obj.keyframe_insert(data_path="location", frame=end_frame - 50)
    obj.location = (0, 0, -5)  # Se déplace en dessous
    obj.keyframe_insert(data_path="location", frame=end_frame)

# Assigner les objets pour l'animation
objects = bpy.data.objects  # Vous pouvez ajuster cette ligne pour sélectionner des objets spécifiques

# Temps pour chaque séquence
time_per_section = (bpy.context.scene.frame_end - bpy.context.scene.frame_start) // len(objects)

# Liste d'informations sur les matériaux
material_info_list = [
    "Zirconium Carbide (ZrC): High temperature resistance",
    "Tungsten Carbide (WC): Excellent electrical conductivity",
    "Silicon Carbide (SiC): Superior insulation properties",
    "Niobium Carbide (NbC): High-performance interconnections",
    "Boron Carbide (B4C): Effective heat dissipation",
    # Ajoutez plus d'informations pour chaque objet ici
]

# Animation d'assemblage et de désassemblage avec annotations pour chaque objet
for i, obj in enumerate(objects):
    if obj.type == 'MESH':  # Seulement pour les objets mesh
        start_frame = i * time_per_section + 1
        mid_frame = start_frame + time_per_section // 2
        end_frame = (i + 1) * time_per_section

        # Vérifier si une information de matériau est disponible pour l'objet
        if i < len(material_info_list):
            material_info = material_info_list[i]
        else:
            material_info = "No specific material information available."

        # Animation avec annotations
        create_animation_with_annotations(obj, start_frame, mid_frame, end_frame, material_info)

# Configuration de la caméra dynamique
camera = bpy.data.objects['Camera']
camera.location = (7, -7, 7)
camera.rotation_euler = (1.1, 0, 0.8)
camera.keyframe_insert(data_path="location", frame=1)
camera.keyframe_insert(data_path="rotation_euler", frame=1)

# Mouvement de la caméra pour donner différentes perspectives
for i in range(len(objects)):
    frame = (i + 1) * time_per_section
    camera.location = (7 + i, -7 + i, 7 - i * 0.5)
    camera.rotation_euler = (1.1 + i * 0.1, 0, 0.8 + i * 0.05)
    camera.keyframe_insert(data_path="location", frame=frame)
    camera.keyframe_insert(data_path="rotation_euler", frame=frame)

# Configuration du rendu
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'BEST'
bpy.context.scene.render.filepath = "//animation_output.mp4"
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.film_transparent = False

# Lancer le rendu de l'animation
bpy.ops.render.render(animation=True)
