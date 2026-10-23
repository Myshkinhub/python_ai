def read_file(filename):

    try:
        with open(filename, 'r', encoding= 'utf-8') as f:
            content = f.read()
            return content
    except Exception as e:
        print(f'文件读取异常： {e}')
        return None


