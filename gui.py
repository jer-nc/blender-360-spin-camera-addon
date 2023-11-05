import bpy


# Definir una función de actualización para la propiedad empty_position
def update_empty_position(self, context):
    empty = bpy.data.objects.get('360_Empty')
    if empty:
        empty.location = self.empty_position

# Definir una clase para la GUI del addon
class CameraSetupPanel(bpy.types.Panel):
    bl_label = "360 Cameras"
    bl_idname = "PT_CameraSetup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "360 Cameras"

    # Definir las propiedades personalizadas
    bpy.types.Scene.num_cameras = bpy.props.IntProperty(
        name="Número de Cámaras",
        default=24,
        min=1
    )
    bpy.types.Scene.radius = bpy.props.FloatProperty(
        name="Radio",
        default=10.0,
        min=0.1
    )
    bpy.types.Scene.empty_position = bpy.props.FloatVectorProperty(
        name="Posición del Empty",
        default=(0, 0, 0),
        update=update_empty_position
    )

    bpy.types.Scene.render_output_path = bpy.props.StringProperty(
        name="Ruta de salida del render",
        default="",
        subtype='DIR_PATH',
    )

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Configuración de Cámaras:")
        layout.prop(scene, "num_cameras")
        layout.prop(scene, "radius")
        layout.separator()
        layout.label(text="Posición del Empty:")

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
        layout.operator("addon.setup_cameras")
        layout.operator("addon.reset_cameras")
        layout.label(text="Ruta de salida del render:")
        layout.prop(context.scene, "render_output_path")
        layout.operator("addon.render_all_360_cameras")
