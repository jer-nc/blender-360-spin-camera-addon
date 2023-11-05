import bpy
import os

# Define a class for the rendering operator for all cameras
class RenderAll360CamerasOperator(bpy.types.Operator):
    bl_idname = "addon.render_all_360_cameras"
    bl_label = "Render All 360 Cameras"

    def execute(self, context):
        # Check if an output path has been configured
        if not context.scene.render_output_path:
            self.report({'ERROR'}, "Output path not configured. Please select a valid folder to save the renders.")
            return {'CANCELLED'}

        # Iterate through all cameras starting with "360_"
        for obj in bpy.data.objects:
            if obj.type == 'CAMERA' and obj.name.startswith('360_'):
                # Activate the current camera
                bpy.context.scene.camera = obj

                # Set the render output path
                context.scene.render.filepath = os.path.join(context.scene.render_output_path, obj.name)

                # Render the image
                bpy.ops.render.render(write_still=True)

        self.report({'INFO'}, "Rendering of all cameras completed.")
        return {'FINISHED'}
