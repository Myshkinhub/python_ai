from datatools import processor,reader,writer


def main():
    write_lens = writer.write_to_file('data.txt',"测试一下包管理是否成功")

    if not write_lens:
        return

    print(f"写入成功，写入{write_lens}")

    contents = reader.read_file('data.txt')
    if not contents:
        return

    print(f'读取成功，读取内容:\n{contents}')


if __name__ == "__main__":
    main()