"""
argparse-解析命令行参数
"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='backup',
        description='backup mysql database',
        epilog='Copyright(r), 2024'
    )
    parser.add_argument('outfile')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('-p', '--port', default=3306, type=int)
    parser.add_argument('-u', '--user', default='root')
    parser.add_argument('-P', '--password', required=True)
    parser.add_argument('-d', '--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    # 解析参数:
    args = parser.parse_args()

    # 打印参数:
    print('parsed args:')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')
    print(f'outfile = {args.outfile}')


if __name__ == '__main__':
    main()
# python .\argparse_demo.py test -udb_root -p110 -P123456 --database testdb -gz
