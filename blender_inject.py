import bpy
import sys
import os
import random

argv = sys.argv
argv = argv[argv.index("--") + 1:]

avatar_path = argv[0]
output_path = argv[1]

animations_dir = "/app/animations"
animations = [f for f in os.listdir(animations_dir) if f.endswith(".fbx")]
chosen = random.choice(animations)
chosen_path = os.path.join(animations_dir, chosen)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

bpy.ops.import_scene.gltf(filepath=avatar_path)
bpy.ops.import_scene.fbx(filepath=chosen_path)

armature = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'][0]
action = bpy.data.actions[-1]

armature.animation_data_create()
armature.animation_data.action = action

bpy.ops.export_scene.gltf(filepath=output_path, export_format='GLB')
