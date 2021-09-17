import bpy

class grab_property(bpy.types.PropertyGroup):
    count:bpy.props.IntProperty(default=4)
    
class grab_forward(bpy.types.Operator):
    bl_idname = "wm.grab_forward"
    bl_label = "grab_forward"
    def execute(self,context):
        try:
            bpy.context.scene.frame_current += bpy.context.scene.grab_count.count
            # print(bpy.context.scene.grab_count.count)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}
        
class grab_back(bpy.types.Operator):
    bl_idname = "wm.grab_back"
    bl_label = "grab_back"
    def execute(self,context):
        try:
            bpy.context.scene.frame_current -= bpy.context.scene.grab_count.count
            # print(bpy.context.scene.grab_count.count)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}    

addon_keymaps=[]
class grab_frame_panel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_grab_frame"
    bl_label = "grab_frame"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self,context):
        props = bpy.context.scene.grab_count
        row = self.layout.row()
        row.label(text = "count:")
        row.prop(props,"count")
        row.operator("wm.grab_back",text="<")        
        row.operator("wm.grab_forward",text=">")
        
def register():
    #bpy.types.Scene.grab_count  = bpy.props.IntProperty(name="grab_frame_count",default=4)
    bpy.utils.register_class(grab_forward)
    bpy.utils.register_class(grab_back)
    bpy.utils.register_class(grab_property)
    bpy.utils.register_class(grab_frame_panel)
    bpy.types.Scene.grab_count = bpy.props.PointerProperty(type=grab_property)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc :
#        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY',region_type='WINDOW')
        #km=kc.keymaps.new(name = "Window",space_type='EMPTY', region_type='WINDOW')
        # km = wm.keyconfigs.addon.keymaps.new(name='Draw', space_type='EMPTY')
        kmi_left = km.keymap_items.new(grab_back.bl_idname, 'LEFT_ARROW', 'PRESS', ctrl=True, shift=False)
        kmi_right = km.keymap_items.new(grab_forward.bl_idname, 'RIGHT_ARROW', 'PRESS', ctrl=True, shift=False)
        kmi_left.active =True
        kmi_right.active =True
        addon_keymaps.append((km, kmi_left))        
        addon_keymaps.append((km, kmi_right))        
    
def unregister():
    bpy.utils.unregister_class(grab_forward)
    bpy.utils.unregister_class(grab_back)
    bpy.utils.unregister_class(grab_property)    
    bpy.utils.unregister_class(grab_frame_panel)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def addon_register():
    register()

if __name__ == "__main__":
    register()
