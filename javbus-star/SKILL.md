---
name: javbus-star
description: JavBus 演员作品搜索。当用户需要搜索演员作品（如"安野由美"）并获取磁力链接时使用。
---

# JavBus 演员搜索

## 工作流程

### 1. 搜索演员

用户提供演员名字后，使用 `javbus-scraper` skill 访问搜索页面：

```
搜索 URL 格式：https://www.javbus.com/searchstar/[URL编码的演员名]
```

例如：
- 演员 "安野由美" → `https://www.javbus.com/searchstar/%E5%AE%89%E9%87%8E%E7%94%B1%E7%BE%8E`

### 2. 进入演员页面

从搜索结果中点击演员名字，进入演员专属页面。

### 3. 获取作品列表和磁力链接

在演员页面中，获取第一个作品的磁力链接，表示成功了。

## 使用示例

**用户输入：** 搜索安野由美的作品

**执行步骤：**
1. 使用 javbus-scraper 访问 `https://www.javbus.com/searchstar/%E5%AE%89%E9%87%8E%E7%94%B1%E7%BE%8E`
2. 通过年龄验证（javbus-scraper 自动处理）
3. 点击演员名字进入演员页面（访问javbus-scraper 不覆盖的网页，使用 agent-browser 工具）
4. 获取第一个作品的磁力链接，表示成功了（访问javbus-scraper 不覆盖的网页，使用 agent-browser 工具）

## 依赖

依赖 `javbus-scraper` skill 进行网页访问和年龄验证处理。
