# news-recommender
个性化新闻推荐系统

> 人工智能技术应用专业实践项目 | 小试牛刀

## 🚀 项目目标
构建一个完整的新闻推荐系统，包含：
- 实时新闻爬虫
- MySQL数据库存储
- 基于内容的推荐算法
- Flask RESTful API
- Vue.js前端展示
- 用户行为反馈系统

## 技术栈
| 模块 | 技术 |
|------|------|
| 爬虫 | Python, BeautifulSoup, Requests |
| 数据库 | MySQL, SQLAlchemy |
| 后端 | Flask, RESTful API |
| 前端 | Vue.js, Axios |
| 推荐算法 | TF-IDF, 余弦相似度 |

## 📂 项目结构
```bash
├── backend/         # 后端代码
├── frontend/        # 前端代码
├── data/            # 数据集和SQL脚本
└── docs/            # 项目文档
```

## 快速开始
```bash
# 克隆仓库
git clone https://github.com/Robot-2024/news-recommender.git

# 安装后端依赖
cd backend
pip install -r requirements.txt

# 运行Flask服务
python app.py
```

## 下一步计划
- [ ] 完成新华网爬虫模块
- [ ] 设计数据库表结构
- [ ] 实现基础推荐算法