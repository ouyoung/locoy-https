#执行后在当前目录dist生成可执行文件
 # 先执行chcp 65001 这句可以解决打包后的文件在win7闪退的问题，报错示例：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb6 in position 5650: invalid start byte
chcp 65001
pyinstaller -i favicon.ico -F locoy-https.py