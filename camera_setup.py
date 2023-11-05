import bpy
import math



# Definir una clase para el operador de configuración de cámaras
class SetupCamerasOperator(bpy.types.Operator):
    bl_idname = "addon.setup_cameras"
    bl_label = "Configurar Cámaras"

    def execute(self, context):
        # Obtener las propiedades configuradas desde la GUI
        num_cameras = context.scene.num_cameras
        radius = context.scene.radius
        empty_position = context.scene.empty_position

        # Nombre único para el objeto empty
        empty_name = '360_Empty'

        # Verificar si el objeto empty ya existe en la escena
        if empty_name not in bpy.data.objects:
            # Crear el objeto empty si no existe
            bpy.ops.object.empty_add(location=empty_position)
            bpy.context.object.name = empty_name

        # Obtener el objeto empty como objetivo
        target_empty = bpy.data.objects.get(empty_name)

        if target_empty is not None:
            # Eliminar cámaras anteriores en la escena que empiezan con "360_"
            for obj in bpy.data.objects:
                if obj.type == 'CAMERA' and obj.name.startswith('360_'):
                    bpy.data.objects.remove(obj, do_unlink=True)

            # Crear las cámaras nuevamente sin eliminar las existentes
            for i in range(num_cameras):
                # Calcular la posición de la cámara
                angle = (2 * math.pi / num_cameras) * i
                x = radius * math.cos(angle) + target_empty.location.x
                y = radius * math.sin(angle) + target_empty.location.y
                z = target_empty.location.z

                # Crear una nueva cámara
                bpy.ops.object.camera_add(location=(x, y, z))
                camera = bpy.context.object

                # Calcular la dirección hacia el empty
                direction = target_empty.location - camera.location
                rot_quat = direction.to_track_quat('Z', 'Y')
                camera.rotation_euler = rot_quat.to_euler()

                # Girar la cámara 180 grados para que mire hacia el empty
                camera.rotation_euler[2] += math.pi

                # Establecer el nombre de la cámara
                camera.name = f'360_Camera_{i + 1}'
        else:
            self.report({'ERROR'}, f"El objeto '{empty_name}' no se encontró en la escena.")

        return {'FINISHED'}

# Definir una clase para el operador de reseteo
class ResetCamerasOperator(bpy.types.Operator):
    bl_idname = "addon.reset_cameras"
    bl_label = "Resetear Cámaras"

    def execute(self, context):
        # Eliminar cámaras existentes en la escena que empiezan con "360_"
        for obj in bpy.data.objects:
            if obj.type == 'CAMERA' and obj.name.startswith('360_'):
                bpy.data.objects.remove(obj, do_unlink=True)

        # Eliminar cámaras del archivo de Blender 
        for data_camera in bpy.data.cameras:
            bpy.data.cameras.remove(data_camera)

        return {'FINISHED'}
