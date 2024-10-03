# Blender Bone Curve Creator

## Overview
This script creates a Bézier curve in Blender, with control points at the world-space head positions of bones from an active armature.

## Requirements
- Blender with an active armature object.

## Usage
1. Ensure the active object is an armature in Blender.
2. Run the script in the Blender scripting editor.
3. A new Bézier curve will be created and linked to the current collection, with control points positioned at each bone head.

## Notes
- Control points are set to have `AUTO` handle types for smooth curve interpolation.
