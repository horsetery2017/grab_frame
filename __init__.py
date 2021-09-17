'''
MIT License

Copyright (c) 2021 Chen Guojun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
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
