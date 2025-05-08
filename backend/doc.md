flask_shop/
├── app/                      # 应用主目录
│   ├── __init__.py          # 应用初始化
│   ├── models/              # 模型目录
│   │   ├── __init__.py
│   │   ├── user.py         # 用户相关模型
│   │   ├── goods.py        # 商品相关模型
│   │   ├── order.py        # 订单相关模型
│   │   └── base.py         # 基础模型类
│   ├── api/                 # API蓝图目录
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── goods.py
│   │   └── order.py
│   ├── services/            # 业务逻辑层
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── order_service.py
│   ├── schemas/            # 序列化模式
│   │   ├── __init__.py
│   │   └── base.py
│   └── utils/              # 工具函数
│       ├── __init__.py
│       └── common.py
├── config/                 # 配置文件目录
│   ├── __init__.py
│   ├── development.py
│   ├── production.py
│   └── testing.py
├── migrations/            # 数据库迁移文件
├── scripts/              # 脚本文件目录
│   ├── __init__.py
│   └── db/              # 数据库相关脚本
│       ├── migrations/  # 数据库迁移脚本
│       └── seeds/       # 数据库种子数据
│           ├── initial_data.sql
│           ├── category_data.sql
│           ├── goods_data.sql
│           └── order_data.sql
├── tests/               # 测试目录
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models/
│   └── test_api/
├── instance/           # 实例配置（不进入版本控制）
│   └── config.py
├── logs/              # 日志目录
├── .env.example       # 环境变量示例
├── .gitignore
├── requirements.txt
└── manage.py         # 应用管理脚本