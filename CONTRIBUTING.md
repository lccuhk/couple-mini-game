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

## 代码风格指南

### Git 提交规范

我们遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**提交类型（type）：**
- `feat` - 新功能、新游戏
- `fix` - Bug 修复
- `docs` - 文档更新
- `style` - 代码格式（不影响代码运行）
- `refactor` - 重构（既不是新增功能，也不是修改 bug）
- `perf` - 性能优化
- `test` - 增加测试
- `chore` - 构建过程或辅助工具的变动
- `ci` - CI/CD 配置变更
- `revert` - 回退提交

**示例：**
```
feat(game): add neon saber battle game

- Add 41st game: neon saber battle
- Implement two-player sword fighting mechanics
- Add neon visual effects and sound effects
- Add game rules and control instructions
- Update index.html with new game card

Closes #456
```

**提交规范：**
- 标题不超过 72 个字符
- 使用中文或英文均可，但要保持一致
- 标题使用祈使句（"添加" 而不是 "添加了"）
- 正文详细说明改动的原因和内容
- 关联相关 Issue（如 `Closes #123`、`Fixes #456`）

### 命名约定

#### JavaScript
```javascript
// 变量/函数 - camelCase
let player1Score = 0
let gameState = 'playing'

function startGame() {
  // ...
}

function checkCollision(obj1, obj2) {
  // ...
}

// 常量 - UPPER_SNAKE_CASE
const CANVAS_WIDTH = 800
const CANVAS_HEIGHT = 600
const PLAYER_SPEED = 5
const GAME_FPS = 60

// 构造函数/类 - PascalCase
class Player {
  constructor(x, y) {
    this.x = x
    this.y = y
  }
}

class Game {
  constructor() {
    this.canvas = null
  }
}

// 私有变量/方法 - 下划线前缀
class Game {
  constructor() {
    this._animationId = null
    this._isRunning = false
  }

  _update() {
    // 内部更新方法
  }
}
```

#### HTML/CSS
```html
<!-- 类名 - kebab-case，语义化命名 -->
<div class="game-container">
  <div class="player player-1">
    <div class="player-score"></div>
  </div>
  <div class="game-canvas-wrapper">
    <canvas id="gameCanvas"></canvas>
  </div>
  <div class="game-controls">
    <button class="btn btn-start">开始游戏</button>
  </div>
</div>
```

```css
/* BEM 命名规范 */
.game-container { }              /* Block */
.game-container__canvas { }      /* Element */
.game-container--paused { }      /* Modifier */

/* 状态类 */
.is-active { }
.is-playing { }
.is-paused { }
.has-winner { }

/* 工具类 */
.text-center { }
.hidden { }
.visible { }
```

#### 文件命名
```
# 游戏文件 - 序号_游戏名（蛇形）
41_neon_saber_battle.html
42_new_game.html

# 样式文件 - kebab-case
game-styles.css
neon-theme.css

# 脚本文件 - camelCase（如果独立）
gameEngine.js
collisionDetection.js

# 图片资源 - kebab-case
player-sprite.png
background.svg
icon-sword.png
```

### 注释规范

#### JavaScript 注释
```javascript
/**
 * 初始化游戏
 * @param {HTMLCanvasElement} canvas - 画布元素
 * @param {Object} options - 游戏配置选项
 * @returns {Game} 游戏实例
 * @example
 * const game = initGame(canvas, { width: 800, height: 600 })
 * game.start()
 */
function initGame(canvas, options) {
  // ...
}

// ✅ 好的注释 - 解释为什么这样做
// 使用 requestAnimationFrame 而不是 setInterval，确保流畅的 60fps
function gameLoop() {
  update()
  render()
  requestAnimationFrame(gameLoop)
}

// ✅ 好的注释 - 解释游戏逻辑
// 玩家 1 用 WASD 控制，玩家 2 用方向键控制
// 这样两人可以在同一键盘上对战
function handleKeyDown(e) {
  // ...
}

// ❌ 不好的注释 - 重复代码内容
// 增加分数
score++
```

#### HTML 注释
```html
<!-- ✅ 好的注释 - 说明区块用途 -->
<!-- 游戏主界面 -->
<div class="game-container">
  <!-- 玩家 1 区域（左侧） -->
  <div class="player player-1">...</div>
  
  <!-- 游戏画布 -->
  <canvas id="gameCanvas"></canvas>
  
  <!-- 玩家 2 区域（右侧） -->
  <div class="player player-2">...</div>
</div>
```

### 游戏代码结构规范

每个游戏文件应遵循以下结构：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>游戏名称</title>
  <style>
    /* 1. 全局样式重置 */
    /* 2. 游戏容器样式 */
    /* 3. 玩家/元素样式 */
    /* 4. UI 样式 */
    /* 5. 动画效果 */
  </style>
</head>
<body>
  <!-- 游戏 UI 结构 -->
  
  <script>
    // 1. 常量定义
    // 2. 游戏状态变量
    // 3. DOM 元素引用
    // 4. 工具函数
    // 5. 游戏类/对象
    // 6. 事件处理
    // 7. 游戏主循环
    // 8. 初始化
  </script>
</body>
</html>
```

### 性能优化规范

```javascript
// ✅ 使用 requestAnimationFrame 进行游戏循环
function gameLoop() {
  update()
  render()
  animationId = requestAnimationFrame(gameLoop)
}

// ✅ 缓存 DOM 查询
const canvas = document.getElementById('gameCanvas')
const ctx = canvas.getContext('2d')

// ✅ 使用对象池减少 GC
class BulletPool {
  constructor() {
    this.pool = []
    this.active = []
  }
  
  get() {
    return this.pool.pop() || new Bullet()
  }
  
  release(bullet) {
    this.pool.push(bullet)
  }
}

// ✅ 避免在游戏循环中创建新对象
function update() {
  // ❌ 不好：每帧创建新对象
  const newPos = { x: player.x + vx, y: player.y + vy }
  
  // ✅ 好：复用现有对象
  player.x += vx
  player.y += vy
}
```

### 错误处理规范

```javascript
// ✅ 游戏初始化错误处理
function initGame() {
  try {
    canvas = document.getElementById('gameCanvas')
    if (!canvas) {
      throw new Error('Canvas element not found')
    }
    ctx = canvas.getContext('2d')
    if (!ctx) {
      throw new Error('Canvas 2D context not supported')
    }
  } catch (error) {
    console.error('游戏初始化失败:', error)
    showErrorMessage('游戏加载失败，请刷新页面重试')
  }
}

// ✅ 游戏循环中的错误捕获
function gameLoop() {
  try {
    update()
    render()
  } catch (error) {
    console.error('游戏运行错误:', error)
    gameState = 'error'
    showErrorMessage('游戏出错，请刷新页面')
    return // 停止游戏循环
  }
  
  if (gameState === 'playing') {
    requestAnimationFrame(gameLoop)
  }
}
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
