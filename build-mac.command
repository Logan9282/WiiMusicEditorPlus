#!/bin/bash

cd "`dirname "$0"`"
pyinstaller --noconfirm -n Program --icon=Icon/icon.ico WiiMusicEditorPlus.py
mv dist/Program/Program dist/Program/WiiMusicEditorPlus
mkdir dist/WiiMusicEditorPlus
echo "creating app"
/usr/local/bin/platypus -y -R -i 'Icon/icon.icns'  -a 'WiiMusicEditorPlus'  -o 'None'  -p '/bin/sh'  -f dist/Program  'macscript.sh' dist/WiiMusicEditorPlus/WiiMusicEditorPlus.app
echo "copying helper"
cp -r crossplatformhelpers/Mac/Helper dist/WiiMusicEditorPlus/Helper
cp crossplatformhelpers/Version.txt dist/WiiMusicEditorPlus/Helper/Update
echo "creating .zip"
rm dist/WiiMusicEditorPlus-Mac.zip
tar -a -C dist -cf dist/WiiMusicEditorPlus-Mac.zip WiiMusicEditorPlus/WiiMusicEditorPlus.app WiiMusicEditorPlus/Helper
echo "done"