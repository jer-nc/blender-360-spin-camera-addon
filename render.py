import bpy
import os
from bpy_extras.io_utils import ExportHelper

# Definir una clase para el operador de renderizado
class Render360CamerasOperator(bpy.types.Operator, ExportHelper):
    bl_idname = "addon.render_360_cameras"
    bl_label = "Renderizar Cámaras 360"

    # Definir la extensión predeterminada del archivo
    # filename_ext = ".png"

    def execute(self, context):
        # Verificar si se ha configurado una ruta de salida
        if not context.scene.render_output_path:
            self.report({'ERROR'}, "Ruta de salida no configurada. Seleccione una carpeta válida para guardar los renders.")
            return {'CANCELLED'}

        # Recorrer todas las cámaras que comienzan con "360_"
        for obj in bpy.data.objects:
            if obj.type == 'CAMERA' and obj.name.startswith('360_'):
                # Activa la cámara actual
                bpy.context.scene.camera = obj

                # Configura la ruta de salida del render
                context.scene.render.filepath = os.path.join(context.scene.render_output_path, obj.name)

                # Renderiza la imagen
                bpy.ops.render.render(write_still=True)

        self.report({'INFO'}, "Renderización completada.")
        return {'FINISHED'}

# Definir una clase para el operador de renderizado de todas las cámaras
class RenderAll360CamerasOperator(bpy.types.Operator):
    bl_idname = "addon.render_all_360_cameras"
    bl_label = "Renderizar Todas las Cámaras 360"

    # Definir la extensión predeterminada del archivo
    filename_ext = ".png"

    def execute(self, context):
        # Verificar si se ha configurado una ruta de salida
        if not context.scene.render_output_path:
            self.report({'ERROR'}, "Ruta de salida no configurada. Seleccione una carpeta válida para guardar los renders.")
            return {'CANCELLED'}

        # Recorrer todas las cámaras que comienzan con "360_"
        for obj in bpy.data.objects:
            if obj.type == 'CAMERA' and obj.name.startswith('360_'):
                # Activa la cámara actual
                bpy.context.scene.camera = obj

                # Configura la ruta de salida del render
                context.scene.render.filepath = os.path.join(context.scene.render_output_path, obj.name)

                # Renderiza la imagen
                bpy.ops.render.render(write_still=True)

        self.report({'INFO'}, "Renderización de todas las cámaras completada.")
        return {'FINISHED'}
