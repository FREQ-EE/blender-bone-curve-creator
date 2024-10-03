import bpy
import mathutils

# Ensure the active object is an armature
armature = bpy.context.active_object
if armature.type != 'ARMATURE':
    print("Error: The active object is not an armature.")
    exit()

# Collect the world-space head positions of all bones in the armature
bone_heads = []
for bone in armature.pose.bones:
    # Convert bone head position to world space
    head_pos = armature.matrix_world @ bone.head
    bone_heads.append(head_pos)

# Create a new Bézier curve data block
curve_data = bpy.data.curves.new(name=f"{armature.name}_curve", type='CURVE')
curve_data.dimensions = '3D'  # Enable 3D coordinates for the curve

# Create a new curve object with the curve data
curve_object = bpy.data.objects.new(name=f"{armature.name}_curve", object_data=curve_data)
bpy.context.collection.objects.link(curve_object)  # Link the object to the current collection

# Add a new spline to the curve
spline = curve_data.splines.new(type='BEZIER')
spline.bezier_points.add(len(bone_heads) - 1)  # Add necessary number of control points

# Position each control point at the corresponding bone head
for i, point in enumerate(spline.bezier_points):
    point.co = bone_heads[i]
    point.handle_left_type = 'AUTO'  # Set handle types for smooth curves
    point.handle_right_type = 'AUTO'

print(f"Bézier curve '{curve_object.name}' created with control points at bone head positions.")