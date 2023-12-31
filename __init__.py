bl_info = {
    "name": "360_CAMERA_ADDON",
    "blender": (3, 6, 1),
    "category": "User Interface",
    "author": "Brender Labs",
    "version": (0, 0, 1),
    "description": "Add-on for 360 camera setup and rendering"
}

import bpy
from .gui import CameraSetupPanel
from .camera_setup import SetupCamerasOperator, ResetCamerasOperator
from .render import  RenderAll360CamerasOperator

# Register and unregister the classes
def register():
    bpy.utils.register_class(CameraSetupPanel)
    bpy.utils.register_class(SetupCamerasOperator)
    bpy.utils.register_class(ResetCamerasOperator)
    bpy.utils.register_class(RenderAll360CamerasOperator)

    
def unregister():
    bpy.utils.unregister_class(CameraSetupPanel)
    bpy.utils.unregister_class(SetupCamerasOperator)
    bpy.utils.unregister_class(ResetCamerasOperator)
    bpy.utils.unregister_class(RenderAll360CamerasOperator)


if __name__ == "__main__":
    register()