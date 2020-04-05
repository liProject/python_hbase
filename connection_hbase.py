import happybase
from happybase import table

if __name__ == '__main__':
    #创建
    connection = happybase.Connection('192.168.43.22')
    # 获取连接实例
    # host：主机名
    # port：端口
    # timeout：超时时间
    # autoconnect：连接是否直接打开
    # table_prefix：用于构造表名的前缀
    # table_prefix_separator：用于table_prefix的分隔符
    # compat：兼容模式
    # transport：运输模式
    # protocol：协议


    # 开启
    connection.open()

    table = happybase.Table('dw_ad',connection)

    # families = {
    #     'cf1': dict(max_versions=10),
    #     'cf2': dict(max_versions=1, block_cache_enabled=False),
    #     'cf3': dict(),
    # }
    #
    # connection.create_table('map',families)

    print(table.name)

    # 关闭
    connection.close()