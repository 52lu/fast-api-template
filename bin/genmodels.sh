#!/bin/bash
# 判断参数是否为空
if [ -z "$1" ]; then
    echo -e " 使用说明: $0 connect db_type
[connect示例]:
 mysql: mysql+pymysql://用户名:密码@127.0.0.1:3306/数据库名
 postgresql: postgresql://username:password@localhost:5432/database_name
 mongodb: mongodb://username:password@localhost:27017/database_name
[db_type示例]:
  mysql、postgresql、mongodb
    "
    exit 1
fi



# 提取数据库类型
db_type=$(echo "$2" | awk -F: '{print $1}')
# 模型文件目录
model_path="app/dao/models/"

echo "db_type: $db_type"
# 生成模型文件名
output_file="$2"
case "$db_type" in
    mysql)
        output_file="${output_file}.gen.py"
        ;;
    postgresql)
        output_file="${output_file}.gen.py"
        ;;
    mongodb)
        output_file="${output_file}.gen.py"
        ;;
    *)
        echo "数据库类型只能是[mysql/postgresql/mongodb] database type: $db_type"
        exit 1
        ;;
esac

# 使用 sqlacodegen 生成模型文件
sqlacodegen "$1" > "${model_path}$output_file"
echo "Generated models file: $output_file"




