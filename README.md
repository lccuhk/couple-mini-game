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
1. 打开仓库 Settings → Pages
2. Source 选择 `Deploy from a branch`
3. Branch 选择 `main`，文件夹选择 `/ (root)`
4. 点击 Save，等待 1-5 分钟
5. 访问：`https://lccuhk.github.io/couple-mini-game/`

> **遇到 404？** 请参考文末的 [GitHub Pages 404 排查指南](#-github-pages-404-排查指南)

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

### 支持的浏览器

| 浏览器 | 最低版本 | 推荐版本 |
|--------|----------|----------|
| Chrome | 60+ | 最新版 |
| Firefox | 55+ | 最新版 |
| Safari | 12+ | 最新版 |
| Edge | 79+ | 最新版 |

> 所有游戏均为纯前端实现，无需后端支持。

### 🔧 浏览器兼容性问题解决

#### 1. 游戏画面不显示或黑屏
**可能原因**：浏览器不支持 Canvas API 或禁用了 JavaScript

**解决方法**：
- 确保浏览器已启用 JavaScript
  - Chrome: 设置 → 隐私和安全 → 网站设置 → JavaScript
  - Firefox: 设置 → 隐私与安全 → JavaScript
  - Safari: 设置 → 安全 → 启用 JavaScript
- 尝试按 `F5` 或 `Cmd/Ctrl + R` 刷新页面
- 尝试使用无痕/隐私模式打开
- 清除浏览器缓存后重新打开
  - Chrome: `Cmd/Ctrl + Shift + Delete`
  - Firefox: `Cmd/Ctrl + Shift + Delete`
  - Safari: 开发 → 清空缓存

#### 2. 按键没有响应
**可能原因**：页面没有获得焦点，或浏览器快捷键冲突

**解决方法**：
- 点击游戏区域确保获得焦点（建议点击画布区域）
- 检查是否有浏览器插件占用了快捷键（如 `W`/`S`/`↑`/`↓`/`空格`）
- 尝试关闭其他可能占用快捷键的程序（如输入法、截图工具等）
- 在 macOS 上，检查系统设置→键盘→快捷键是否有冲突
- 尝试禁用浏览器扩展，特别是广告拦截器和快捷键管理扩展

#### 3. 方向键控制时页面滚动
**可能原因**：浏览器默认行为没有被阻止

**解决方法**：
- 确保点击了游戏区域（画布）获得焦点
- 尝试刷新页面
- 如果问题持续，尝试使用其他浏览器
- 检查是否启用了"平滑滚动"等浏览器特性

#### 4. 游戏运行卡顿
**可能原因**：浏览器硬件加速未开启，或后台程序过多

**解决方法**：
- 关闭浏览器中其他不必要的标签页
- 开启浏览器硬件加速：
  - **Chrome**：设置 → 系统 → "使用硬件加速模式" → 重启浏览器
  - **Firefox**：设置 → 常规 → 性能 → "使用硬件加速" → 重启浏览器
  - **Safari**：设置 → 高级 → "在菜单栏中显示开发菜单" → 开发 → "停用硬件加速"（确保未勾选）
- 尝试降低浏览器缩放比例（`Cmd/Ctrl + 0` 重置为 100%）
- 更新浏览器到最新版本
- 关闭其他占用系统资源的程序

#### 5. 音效没有声音
**可能原因**：浏览器自动播放策略限制，或音频上下文未初始化

**解决方法**：
- 点击游戏区域后再开始游戏（浏览器需要用户交互才能播放音频）
- 检查浏览器标签页是否被静音（右键标签页 → 取消静音）
- 检查系统音量是否正常
- 在 Chrome 中检查：设置 → 隐私和安全 → 网站设置 → 声音
- 尝试刷新页面后先点击任意位置，再开始游戏
- 如果使用 Safari，检查：设置 → 网站 → 自动播放 → 允许所有自动播放

#### 6. 空格键无法开始游戏
**可能原因**：浏览器插件或扩展拦截了空格键

**解决方法**：
- 点击游戏区域后再按空格键
- 尝试禁用广告拦截插件或其他浏览器扩展
- 尝试使用 `R` 键先重置游戏，再按空格开始
- 检查是否有输入法占用了空格键（如中文输入法的选词功能）

#### 7. Canvas 游戏画面模糊
**可能原因**：高 DPI 屏幕适配问题，或浏览器缩放比例不对

**解决方法**：
- 按 `Cmd/Ctrl + 0` 重置浏览器缩放为 100%
- 在 Chrome 中访问 `chrome://flags/#high-dpi-support` 确保启用
- 尝试关闭浏览器的"页面缩放"功能
- 更新显卡驱动程序

#### 8. 动画不流畅或掉帧
**可能原因**：浏览器帧率限制，或 `requestAnimationFrame` 被抑制

**解决方法**：
- 确保浏览器窗口处于活动状态（后台标签页可能会降低帧率）
- 关闭浏览器的"节能模式"或"后台标签页限制"
- 在 Chrome 中访问 `chrome://flags/#disable-accelerated-2d-canvas` 禁用后重新启用
- 尝试关闭其他使用 GPU 的程序

#### 9. 移动端浏览器问题
**注意**：本合集的游戏主要为双人本地对战设计，**部分游戏需要物理键盘**

**解决方法**：
- 建议使用电脑浏览器游玩
- 连接外接键盘到移动设备（不保证完全兼容）
- 触屏游戏（如井字棋、石头剪刀布、四子棋）可以在移动端正常游玩
- 确保移动端浏览器未开启"请求桌面站点"或"桌面模式"

#### 10. 其他问题
如果以上方法都无法解决，请尝试：
1. 更新浏览器到最新版本
2. 尝试使用其他浏览器（Chrome/Firefox/Safari/Edge）
3. 检查电脑是否安装了必要的系统更新
4. 检查是否有杀毒软件或防火墙拦截了页面功能
5. 在 GitHub 提交 Issue 描述你的问题（请注明浏览器版本和操作系统）

### 检查浏览器兼容性

你可以访问以下网站检查你的浏览器是否支持所需功能：
- Canvas 支持：https://caniuse.com/canvas
- ES6 特性：https://caniuse.com/es6
- Web Audio API：https://caniuse.com/audio-api
- CSS 动画：https://caniuse.com/css-animation

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

## 🔍 GitHub Pages 404 排查指南

如果开启 GitHub Pages 后访问显示 404，请按照以下步骤排查：

### 1. ⏳ 等待足够时间
- **首次部署**：需要 1-5 分钟
- **更新后**：需要 30 秒 - 2 分钟
- 可以在仓库的 **Actions** 页面查看部署进度

### 2. ✅ 检查 Pages 设置
打开：https://github.com/lccuhk/couple-mini-game/settings/pages

确保：
- **Source** 选择了 `Deploy from a branch`
- **Branch** 选择了 `main`（或 `master`）
- **文件夹** 选择了 `/ (root)`
- 点击了 **Save** 按钮
- 页面显示 `Your site is live at https://...`

### 3. 📁 检查文件结构
确保仓库根目录有 `index.html`：
```
couple-mini-game/
├── index.html       ✅ 必须存在
├── README.md
└── games/
    └── ...
```

如果 `index.html` 在子目录中，需要调整 Pages 设置中的文件夹路径。

### 4. 🌐 检查访问的 URL
确保访问的是正确的 URL：
```
✅ 正确：https://lccuhk.github.io/couple-mini-game/
❌ 错误：https://lccuhk.github.io/couple-mini-game
❌ 错误：https://lccuhk.github.io/Couple-Mini-Game/  (大小写敏感)
```

> **注意**：GitHub Pages URL 是大小写敏感的！

### 5. 🧹 清除浏览器缓存
- 硬刷新页面：`Cmd/Ctrl + Shift + R`
- 或使用无痕/隐私模式访问
- 或清除浏览器缓存后重新访问

### 6. 🚫 检查 Jekyll 问题
GitHub Pages 默认使用 Jekyll 构建，如果你的项目中有以下划线开头的文件或目录，可能会被 Jekyll 忽略。

**解决方法**：在仓库根目录创建一个名为 `.nojekyll` 的空文件：
```bash
touch .nojekyll
git add .nojekyll
git commit -m "Add .nojekyll to bypass Jekyll"
git push
```

### 7. 📊 检查部署状态
1. 打开仓库的 **Actions** 页面：https://github.com/lccuhk/couple-mini-game/actions
2. 查看最近的 `pages build and deployment` 工作流
3. 确保工作流运行成功（显示绿色 ✓）
4. 如果失败，点击查看详细错误信息

### 8. 🔐 检查仓库权限
确保仓库是 **Public**（公开的）：
- 打开仓库 **Settings** → **General**
- 滚动到 **Danger Zone**
- 确保 **Change repository visibility** 显示为 `Public`

> 私有仓库也可以使用 GitHub Pages，但需要 GitHub Pro 账户。

### 9. 🔄 重新触发部署
如果部署卡住了，可以尝试：
1. 做一个空提交：
   ```bash
   git commit --allow-empty -m "Trigger rebuild"
   git push
   ```
2. 或者在 Pages 设置中切换分支再切回来：
   - 先选 `None`，保存
   - 再选 `main` / `root`，保存

### 10. 📝 检查自定义域名（如果使用）
如果你设置了自定义域名：
- 确保 DNS 解析正确
- 确保 CNAME 文件存在且内容正确
- 确保 SSL 证书已颁发

---

## 💡 快速检查清单

| 检查项 | 状态 |
|--------|------|
| 等待了至少 5 分钟 | ⬜ |
| Pages 设置正确（main + root） | ⬜ |
| index.html 在根目录 | ⬜ |
| URL 大小写正确 | ⬜ |
| 尝试了硬刷新/无痕模式 | ⬜ |
| Actions 部署成功 | ⬜ |
| 仓库是公开的 | ⬜ |

---

## 🆘 还是不行？

1. 访问：`https://github.com/lccuhk/couple-mini-game/deployments` 查看部署历史
2. 检查是否有 `pages build and deployment` 的错误信息
3. 参考官方文档：https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

---

## 📄 License

MIT License

---

## 💝 致谢

感谢所有为这个项目做出贡献的人！

如果这个项目对你有帮助，欢迎给个 ⭐ Star！

---

**Made with ❤️ for couples and friends**
