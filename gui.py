import bpy
import math

# Define an update function for the empty_position property
def update_empty_position(self, context):
    empty = bpy.data.objects.get('360_Empty')
    if empty:
        # Update the empty position
        empty.location = self.empty_position


def update_camera_rotation_x(self, context):
    for obj in bpy.data.objects:
        if obj.type == 'CAMERA' and obj.name.startswith('360_'):
            obj.rotation_euler.x = self.camera_rotation_x


# Define a class for the addon GUI
class CameraSetupPanel(bpy.types.Panel):
    bl_label = "360 Cameras"
    bl_idname = "PT_CameraSetup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "360 Cameras"

    # Define custom properties
    bpy.types.Scene.num_cameras = bpy.props.IntProperty(
        name="Number of Cameras",
        default=24,
        min=1
    )
    bpy.types.Scene.radius = bpy.props.FloatProperty(
        name="Radius",
        default=10.0,
        min=0.1
    )
    bpy.types.Scene.empty_position = bpy.props.FloatVectorProperty(
        name="Empty Position",
        default=(0, 0, 0),
        update=update_empty_position
    )

    bpy.types.Scene.render_output_path = bpy.props.StringProperty(
        name="",
        default="",
        subtype='DIR_PATH',
    )

    bpy.types.Scene.camera_rotation_x = bpy.props.FloatProperty(
        name="Camera X Rotation",
        default=0.0,
        min=0.0,
        max=2 * math.pi,
        update=update_camera_rotation_x
    )

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Camera setup
        layout.label(text="Camera Setup:")
        layout.prop(scene, "num_cameras")
        # Camera radius
        layout.prop(scene, "radius")


        layout.label(text="Camera X Rotation:")
        layout.prop(scene, "camera_rotation_x")
        layout.separator()

        # Empty position
        layout.label(text="Empty Position:")

        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.label(text="X")
        row.prop(scene, "empty_position", index=0, text="")
        row = col.row(align=True)
        row.label(text="Y")
        row.prop(scene, "empty_position", index=1, text="")
        row = col.row(align=True)
        row.label(text="Z")
        row.prop(scene, "empty_position", index=2, text="")
        layout.separator()
        # Cameras setup Button
        layout.operator("addon.setup_cameras")
        # Reset Cameras Button
        layout.operator("addon.reset_cameras")
        layout.separator()
        # Render Output Path
        layout.label(text="Render Output Path:")
        layout.prop(context.scene, "render_output_path")
        layout.separator()
        # Render All Cameras Button
        layout.operator("addon.render_all_360_cameras")
