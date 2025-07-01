pyinstaller ^
    --noupx^
    -F --noconsole --clean ^
    -n TextureForge-v0.0.1^
    --upx-dir=..\resources\upx-4.2.4-win64^
    --icon=.\textureforge\resources\icon.ico^
    --add-data textureforge\resources\icon.ico:resources^
    .\main.py