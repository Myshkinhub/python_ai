def write_to_file(filename, data):
    try:
        with open(filename, 'a', encoding= 'utf-8') as f:
            return f.write(data)

    except Exception as e:
        print(f'文件写入异常： {e}')
        return None

