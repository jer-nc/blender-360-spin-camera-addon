bl_info = {
    "name": "360 CAMERA ADDON",
    "blender": (3, 6, 0),
    "category": "Object",
}

import bpy
from .gui import CameraSetupPanel
from .camera_setup import SetupCamerasOperator, ResetCamerasOperator
from .render import Render360CamerasOperator, RenderAll360CamerasOperator



# Registrar las clases
def register():
    bpy.utils.register_class(CameraSetupPanel)
    bpy.utils.register_class(SetupCamerasOperator)
    bpy.utils.register_class(ResetCamerasOperator)
    bpy.utils.register_class(Render360CamerasOperator)
    bpy.utils.register_class(RenderAll360CamerasOperator)

    
def unregister():
    bpy.utils.unregister_class(CameraSetupPanel)
    bpy.utils.unregister_class(SetupCamerasOperator)
    bpy.utils.unregister_class(ResetCamerasOperator)
    bpy.utils.unregister_class(Render360CamerasOperator)
    bpy.utils.unregister_class(RenderAll360CamerasOperator)


if __name__ == "__main__":
    register()