import os
import re

def convert_sql_file(file_path):
    """转换单个SQL文件为SQLite格式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换 value 为 VALUES
    content = re.sub(r'\bvalue\b', 'VALUES', content, flags=re.IGNORECASE)
    
    # 分割SQL语句
    statements = [s.strip() for s in content.split(';') if s.strip()]
    
    # 转换每个语句
    new_statements = []
    for stmt in statements:
        # 提取表名和字段
        match = re.match(r'insert\s+into\s+(\w+)\s*\((.*?)\)', stmt, re.IGNORECASE)
        if match:
            table_name = match.group(1)
            fields = match.group(2)
            
            # 添加时间戳字段
            if 'created_at' not in fields and 'updated_at' not in fields:
                fields = fields.strip()
                new_fields = f"{fields}, created_at, updated_at"
                
                # 提取VALUES部分
                values_match = re.search(r'VALUES\s*\((.*?)\)', stmt, re.IGNORECASE)
                if values_match:
                    values = values_match.group(1)
                    new_values = f"{values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP"
                    
                    # 构建新的SQL语句
                    new_stmt = f"INSERT INTO {table_name} ({new_fields}) VALUES ({new_values})"
                    new_statements.append(new_stmt)
                    continue
        
        new_statements.append(stmt)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        for stmt in new_statements:
            f.write(stmt + ';\n')

def main():
    """转换所有SQL文件"""
    sql_files = [
        'category_data.sql',
        'goods_data.sql',
        'express_data.sql',
        'order_data.sql'
    ]
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    for sql_file in sql_files:
        file_path = os.path.join(current_dir, sql_file)
        if os.path.exists(file_path):
            print(f"正在转换 {sql_file}...")
            convert_sql_file(file_path)
            print(f"完成转换 {sql_file}")
        else:
            print(f"找不到文件 {sql_file}")

if __name__ == '__main__':
    main() 