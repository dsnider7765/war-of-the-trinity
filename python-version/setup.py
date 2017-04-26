# -*- coding: utf-8 -*-

# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ['pygame','pyscroll','pytmx','tkinter']}

base = None
"""if sys.platform == 'win32':
    base = 'Win32GUI'"""
#base = 'Win64GUI'
executables = [
    Executable('main.py', base=base)
]
""", includes=['pygame','pyscroll','pytmx',
                                               'combat','random',
                                               'create_character','elements',
                                               'encounter','map_objects',
                                               'player','save_game',
                                               'spritesheet','stats',
                                               'wott_base_lib','six']"""

setup(name='War Of The Trinity',
      version='0.1',
      description='Sample cx_Freeze Tkinter script',
      options={'build_exe':{'include_files':['BombExploding.png',
'cyborg assassin(scaled).png', 'hyptosis_sprites-and-tiles-for-you.png',
'hyptosis_til-art-batch-2.png', 'hyptosis_tile-art-batch-1.png',
'hyptosis_tile-art-batch-3.png', 'hyptosis_tile-art-batch-4.png',
'hyptosis_tile-art-batch-5.png', 'Magic.ogg', 'map.png', 'save_game.xml',
'theMap.tmx', 'types.xml', 'WhoToJoin.ogg', 'combat.py', 'create_character.py',
'elements.py', 'map_objects.py', 'player.py', 'save_game.py', 'spritesheet.py',
'stats.py', 'wott_base_lib.py','Army of the Republic.ogg',
'Institute of Science.ogg','main.py']}},
      executables=executables
      )
