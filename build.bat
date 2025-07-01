pyinstaller ^
    --noupx^
    -F --noconsole --clean ^
    -n TextureForge-v0.1.0^
    --upx-dir=..\resources\upx-4.2.4-win64^
    --icon=.\textureforge\resources\icon.ico^
    --add-data textureforge\resources\icon.ico:resources^
    --add-data textureforge\bin\texconv.exe:bin^
    --add-data textureforge\bin\texdiag.exe:bin^
    .\main.py