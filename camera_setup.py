import bpy
import math



# Define a class for the camera setup operator
class SetupCamerasOperator(bpy.types.Operator):
    bl_idname = "addon.setup_cameras"
    bl_label = "Setup Cameras"

    def execute(self, context):
        # Get the user-configured properties from the GUI
        num_cameras = context.scene.num_cameras
        radius = context.scene.radius
        empty_position = context.scene.empty_position

        # Unique name for the empty object
        empty_name = '360_Empty'

        # Check if the empty object already exists in the scene
        if empty_name not in bpy.data.objects:
            # Create the empty object if it doesn't exist
            bpy.ops.object.empty_add(location=empty_position)
            bpy.context.object.name = empty_name

        # Get the empty object as the target
        target_empty = bpy.data.objects.get(empty_name)

        if target_empty is not None:
            # Remove previous cameras in the scene starting with "360_"
            for obj in bpy.data.objects:
                if obj.type == 'CAMERA' and obj.name.startswith('360_'):
                    bpy.data.objects.remove(obj, do_unlink=True)

            # Create cameras again without removing existing ones
            for i in range(num_cameras):
                # Calculate the camera position
                angle = (2 * math.pi / num_cameras) * i
                x = radius * math.cos(angle) + target_empty.location.x
                y = radius * math.sin(angle) + target_empty.location.y
                z = target_empty.location.z

                # Create a new camera
                bpy.ops.object.camera_add(location=(x, y, z))
                camera = bpy.context.object

                # Calculate the direction towards the empty
                direction = target_empty.location - camera.location
                rot_quat = direction.to_track_quat('Z', 'Y')
                camera.rotation_euler = rot_quat.to_euler()

                # Rotate the camera 180 degrees to point at the empty
                camera.rotation_euler[2] += math.pi

                # Set the camera name
                camera.name = f'360_Camera_{i + 1}'
        else:
            self.report({'ERROR'}, f"The object '{empty_name}' was not found in the scene.")

        return {'FINISHED'}

# Define a class for the reset operator
class ResetCamerasOperator(bpy.types.Operator):
    bl_idname = "addon.reset_cameras"
    bl_label = "Reset Cameras"

    def execute(self, context):
        # Remove existing cameras in the scene starting with "360_"
        for obj in bpy.data.objects:
            if obj.type == 'CAMERA' and obj.name.startswith('360_'):
                bpy.data.objects.remove(obj, do_unlink=True)

        # Remove cameras from the Blender file 
        for data_camera in bpy.data.cameras:
            bpy.data.cameras.remove(data_camera)

        return {'FINISHED'}
