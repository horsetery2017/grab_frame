"""
***** BEGIN GPL LICENSE BLOCK *****

Mixamo add-on for Blender provides a solution to create an IK control 
rig and bake animations in and out of a character control rig and skeleton.
Copyright (C) 2021 Adobe.
 
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

***** END GPL LICENSE BLOCK *****
"""

bl_info = {
    "name": "Grab Frame",
    "author": "GuoJun Chen (horsetery@gmail.com)",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "3D View >Tool> Grab Frame",
    "description": '''Use keyboard shortcuts to change the current frame by a specified number of frames.ctrl + left arrow : back frame,ctrl + right arrow : forward frame''',
    "category": "Animation"}
from . import grab_frame

def register():
    grab_frame.register()
def unregister():
    grab_frame.unregister()

if __name__ == "__main__":
    register()
