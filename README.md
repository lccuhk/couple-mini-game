# 🎮 双人小游戏合集 - Couple Mini Games

> 专为情侣和朋友设计的 10 款双人本地对战小游戏，纯 HTML/CSS/JavaScript 实现，无需安装，打开即玩！

![GitHub](https://img.shields.io/badge/GitHub-lccuhk%2Fcouple--mini--game-blue)
![Games](https://img.shields.io/badge/游戏数量-10款-green)
![Tech](https://img.shields.io/badge/技术栈-HTML%2FCSS%2FJS-orange)

---

## 🎯 游戏列表

### 🎮 经典对战

| 序号 | 游戏 | 图标 | 描述 |
|------|------|------|------|
| 01 | [乒乓球对战](games/01_pong.html) | 🏓 | 经典乒乓球游戏，支持音效、倒计时、获胜动画 |
| 02 | [井字棋](games/02_tic_tac_toe.html) | ❌⭕ | 三连棋对战，支持比分记录 |
| 07 | [四子棋](games/07_connect_four.html) | 🔴🔵 | 策略对战，四子连线获胜 |

### 🐍 动作竞技

| 序号 | 游戏 | 图标 | 描述 |
|------|------|------|------|
| 04 | [贪吃蛇对战](games/04_snake_battle.html) | 🐍 | 双人版贪吃蛇，吃食物长大，撞墙或对方即输 |
| 05 | [射击对战](games/05_shooter_battle.html) | 🎯 | 双人射击对战，击中对方得分 |
| 08 | [打地鼠对战](games/08_whack_a_mole.html) | 🐹 | 30秒限时比赛，看谁打得多 |

### 🧠 益智反应

| 序号 | 游戏 | 图标 | 描述 |
|------|------|------|------|
| 03 | [石头剪刀布](games/03_rock_paper_scissors.html) | 🪨📄✂️ | 经典猜拳游戏，多回合对战 |
| 06 | [记忆翻牌](games/06_memory_match.html) | 🃏 | 考验记忆力，配对成功得分 |
| 09 | [反应力测试](games/09_reaction_test.html) | ⚡ | 测试反应速度，抢跑会扣分 |
| 10 | [数字炸弹](games/10_number_bomb.html) | 💣 | 猜数字，猜中炸弹就输了 |

---

## 🚀 快速开始

### 方法一：直接打开（最简单）
```bash
# 克隆仓库
git clone https://github.com/lccuhk/couple-mini-game.git

# 进入目录
cd couple-mini-game

# 直接用浏览器打开 index.html
open index.html  # macOS
# 或双击 index.html 文件
```

### 方法二：本地服务器（推荐）
```bash
# Python 3
python3 -m http.server 8000

# 或 Node.js
npx serve .
```
然后访问：http://localhost:8000

### 方法三：GitHub Pages
1. 开启仓库的 GitHub Pages 功能
2. 访问：`https://lccuhk.github.io/couple-mini-game/`

---

## 🎮 操作说明

### 通用控制
- 每个游戏页面左上角有「← 返回」按钮可回到主页
- 大部分游戏支持键盘快捷键操作

### 各游戏控制

#### 🏓 乒乓球对战
| 玩家 | 向上 | 向下 |
|------|------|------|
| 玩家1 | `W` | `S` |
| 玩家2 | `↑` | `↓` |
| 全局 | `空格` 开始/暂停 | `R` 重新开始 |

#### 🐍 贪吃蛇对战
| 玩家 | 向上 | 向下 | 向左 | 向右 |
|------|------|------|------|------|
| 玩家1 | `W` | `S` | `A` | `D` |
| 玩家2 | `↑` | `↓` | `←` | `→` |

#### 🎯 射击对战
| 玩家 | 向上 | 向下 | 向左 | 向右 | 射击 |
|------|------|------|------|------|------|
| 玩家1 | `W` | `S` | `A` | `D` | `F` |
| 玩家2 | `↑` | `↓` | `←` | `→` | `/` |

#### 🐹 打地鼠对战
| 洞号 | 玩家1 | 玩家2 |
|------|-------|-------|
| 1 | `Q` | `7` |
| 2 | `W` | `8` |
| 3 | `E` | `9` |
| 4 | `A` | `4` |
| 5 | `S` | `5` |
| 6 | `D` | `6` |
| 7 | `Z` | `1` |
| 8 | `X` | `2` |
| 9 | `C` | `3` |

#### ⚡ 反应力测试
| 玩家 | 按键 |
|------|------|
| 玩家1 | `Q` |
| 玩家2 | `P` |

其他游戏请参考游戏内的操作说明。

---

## ✨ 特色功能

- 🎨 **精美界面**：每个游戏都有独特的渐变背景和霓虹风格
- 🎵 **音效系统**：乒乓球游戏支持 Web Audio API 实时音效
- 📱 **响应式设计**：适配不同屏幕尺寸
- 💾 **比分记录**：支持多回合对战和比分保存
- 🎉 **动画效果**：获胜庆祝、粒子特效、倒计时等
- ⚙️ **可配置设置**：乒乓球游戏支持调整获胜分数和音效开关

---

## 🛠️ 技术栈

- **HTML5** - 页面结构
- **CSS3** - 样式、动画、响应式设计
- **JavaScript (ES6+)** - 游戏逻辑
- **Canvas API** - 乒乓球、贪吃蛇、射击等游戏的渲染
- **Web Audio API** - 音效生成

---

## 📁 项目结构

```
couple-mini-game/
├── index.html              # 主页导航
├── README.md               # 项目说明
├── .gitignore             # Git 忽略配置
└── games/                  # 游戏目录
    ├── 01_pong.html             # 🏓 乒乓球对战
    ├── 02_tic_tac_toe.html      # ❌⭕ 井字棋
    ├── 03_rock_paper_scissors.html  # 🪨📄✂️ 石头剪刀布
    ├── 04_snake_battle.html     # 🐍 贪吃蛇对战
    ├── 05_shooter_battle.html   # 🎯 射击对战
    ├── 06_memory_match.html     # 🃏 记忆翻牌
    ├── 07_connect_four.html     # 🔴🔵 四子棋
    ├── 08_whack_a_mole.html     # 🐹 打地鼠对战
    ├── 09_reaction_test.html    # ⚡ 反应力测试
    └── 10_number_bomb.html      # 💣 数字炸弹
```

---

## 🌐 浏览器兼容性

| 浏览器 | 最低版本 | 推荐版本 |
|--------|----------|----------|
| Chrome | 60+ | 最新版 |
| Firefox | 55+ | 最新版 |
| Safari | 12+ | 最新版 |
| Edge | 79+ | 最新版 |

> 所有游戏均为纯前端实现，无需后端支持。

---

## 🔧 常见问题

### Q: 按键没有反应？
A: 请先点击游戏区域获得键盘焦点，然后再操作。

### Q: 音效没有声音？
A: 部分浏览器需要用户先交互才能播放音频，请点击游戏区域后再开始游戏。

### Q: 可以在手机上玩吗？
A: 所有游戏都支持触屏浏览，但部分需要键盘操作的游戏建议在电脑上游玩。

### Q: 如何添加新游戏？
A: 在 `games/` 目录下创建新的 HTML 文件，然后在 `index.html` 中添加游戏卡片即可。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 如何贡献新游戏
1. 在 `games/` 目录创建新的 HTML 文件（命名格式：`序号_游戏名.html`）
2. 在 `index.html` 中添加游戏卡片
3. 确保游戏支持双人对战
4. 提交 PR

---

## 📄 License

MIT License

---

## 💝 致谢

感谢所有为这个项目做出贡献的人！

如果这个项目对你有帮助，欢迎给个 ⭐ Star！

---

**Made with ❤️ for couples and friends**
