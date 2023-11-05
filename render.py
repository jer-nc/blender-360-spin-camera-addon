import bpy
import os

# Define a class for the render operator 
class RenderAll360CamerasOperator(bpy.types.Operator):
    bl_idname = "addon.render_all_360_cameras"
    bl_label = "Render All 360 Cameras"

    def execute(self, context):
        # Verify that the output path is set
        if not context.scene.render_output_path:
            self.report({'ERROR'}, "Output path not configured. Please select a valid folder to save the renders.")
            return {'CANCELLED'}

        # Get all cameras in the scene starting with "360_" 
        camera_objs = [obj for obj in bpy.data.objects if obj.type == 'CAMERA' and obj.name.startswith('360_')]

        # Order the cameras by name (360_camera_00, 360_camera_01, 360_camera_02, ...)
        camera_objs.sort(key=lambda x: x.name)

        # Get the output path from the scene
        output_path = context.scene.render_output_path

        # Render all cameras in the scene starting with "360_" 
        for index, camera in enumerate(camera_objs):
            # Set the active camera
            context.scene.camera = camera

            # Rename the camera with the index (360_camera_00, 360_camera_01, 360_camera_02, ...)
            camera.name = f'360_camera_{str(index).zfill(2)}'

            # Set the output path for the camera (output_path/360_camera_00) 
            context.scene.render.filepath = os.path.join(output_path, camera.name)

            # Render the image
            bpy.ops.render.render(write_still=True)

        self.report({'INFO'}, "Render Completed")
        return {'FINISHED'}