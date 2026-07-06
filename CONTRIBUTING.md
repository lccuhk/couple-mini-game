# 贡献指南

感谢您对 **Couple Mini Games** 项目的关注！我们欢迎任何形式的贡献，无论是提交 Bug 报告、提出功能建议，还是直接贡献代码。

## 📋 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
  - [提交 Issue](#提交-issue)
  - [提交 Pull Request](#提交-pull-request)
  - [贡献新游戏](#贡献新游戏)
- [代码规范](#代码规范)
- [开发环境](#开发环境)

## 行为准则

本项目遵循 [Contributor Covenant](.github/CODE_OF_CONDUCT.md) 行为准则。参与项目即表示您同意遵守其条款。

## 如何贡献

### 提交 Issue

如果您发现了 Bug 或有新功能建议，请通过 Issue 告诉我们：

1. **Bug 报告**：请包含以下信息
   - 问题描述（清晰简洁）
   - 复现步骤
   - 预期行为
   - 实际行为
   - 浏览器和操作系统信息
   - 截图（如适用）

2. **功能建议**：请包含以下信息
   - 功能描述
   - 为什么需要这个功能
   - 实现思路（可选）

### 提交 Pull Request

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

**PR 规范：**
- 标题清晰描述改动内容
- 详细说明改动的原因和内容
- 关联相关的 Issue（如 `Fixes #123`）
- 确保代码通过所有检查

### 贡献新游戏

我们非常欢迎新游戏贡献！请遵循以下步骤：

1. **游戏文件**：在 `games/` 目录下创建新的 HTML 文件，命名格式为 `序号_游戏名.html`（例如 `42_new_game.html`）
2. **游戏卡片**：在 `index.html` 中添加游戏卡片，包含游戏名称、图标和描述
3. **游戏要求**：
   - 必须支持双人本地对战
   - 使用纯 HTML/CSS/JavaScript 实现（无需额外依赖）
   - 包含清晰的游戏规则说明
   - 支持键盘操作（推荐使用 `WASD` 和方向键）
   - 代码风格与现有游戏保持一致
4. **测试**：确保游戏在主流浏览器（Chrome、Firefox、Safari）中正常运行

## 代码规范

### JavaScript

- 使用 2 空格缩进
- 使用双引号
- 语句末尾加分号
- 变量和函数使用驼峰命名法
- 注释清晰，说明复杂逻辑

### HTML/CSS

- 使用 2 空格缩进
- 类名使用 kebab-case
- CSS 属性按字母顺序排列
- 语义化 HTML 标签

### 格式化

项目使用 Prettier 进行代码格式化，请确保提交前运行：

```bash
npx prettier --write .
```

## 开发环境

本项目是纯前端项目，无需复杂的开发环境：

1. 克隆仓库：`git clone https://github.com/lccuhk/couple-mini-game.git`
2. 进入目录：`cd couple-mini-game`
3. 启动本地服务器（可选）：
   ```bash
   # 使用 Python
   python3 -m http.server 8000
   
   # 或使用 Node.js
   npx serve .
   ```
4. 在浏览器中访问 `http://localhost:8000`

## 问题？

如果您在贡献过程中遇到任何问题，欢迎通过以下方式联系我们：

- 提交 [Issue](https://github.com/lccuhk/couple-mini-game/issues)
- 查看 [README.md](README.md) 了解更多项目信息

再次感谢您的贡献！🎉
