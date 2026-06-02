#!/usr/bin/env python3
"""
双人小游戏测试脚本
测试21-40号新游戏能否正常启动
"""

import os
import sys
import time
import random
import webbrowser
import urllib.request
from datetime import datetime

# 游戏列表（21-40号）
GAMES = [
    ("21_doudizhu_battle.html", "斗地主对战"),
    ("22_tetris_battle.html", "俄罗斯方块对战"),
    ("23_tank_battle.html", "坦克大战"),
    ("24_linkup_battle.html", "连连看对战"),
    ("25_basketball_battle.html", "篮球对战"),
    ("26_soccer_battle.html", "足球对战"),
    ("27_bubble_shooter_battle.html", "泡泡龙对战"),
    ("28_match3_battle.html", "消消乐对战"),
    ("29_sokoban_battle.html", "推箱子对战"),
    ("30_breakout_battle.html", "打砖块对战"),
    ("31_racing_battle.html", "赛车对战"),
    ("32_space_shooter_battle.html", "飞行射击对战"),
    ("33_bomberman_battle.html", "炸弹人对战"),
    ("34_hop_battle.html", "跳一跳对战"),
    ("35_runner_battle.html", "跑酷对战"),
    ("36_tower_defense_battle.html", "塔防对战"),
    ("37_gomoku_battle.html", "五子棋对战"),
    ("38_chinese_chess_battle.html", "中国象棋对战"),
    ("39_go_battle.html", "围棋对战"),
    ("40_fishing_battle.html", "捕鱼达人对战"),
]

BASE_URL = "http://localhost:8000/games/"
RESULTS = []


def print_banner(text):
    """打印横幅"""
    print("=" * 60)
    print(f"  {text}")
    print("=" * 60)


def test_game_exists(filename):
    """测试游戏文件是否存在"""
    filepath = os.path.join("games", filename)
    exists = os.path.exists(filepath)
    filesize = os.path.getsize(filepath) if exists else 0
    return exists, filesize


def test_game_loads(filename, open_in_browser=False):
    """测试游戏能否正常加载"""
    try:
        url = BASE_URL + filename
        if open_in_browser:
            print(f"  🔗 打开游戏: {url}")
            webbrowser.open(url)
            return True, "手动检查模式"
        else:
            # 尝试访问URL
            with urllib.request.urlopen(url, timeout=10) as response:
                content = response.read()
                return True, f"响应码: {response.status}, 大小: {len(content)} bytes"
    except Exception as e:
        return False, str(e)


def run_tests(mode="check", num_games=None):
    """运行测试"""
    print_banner("🎮 双人小游戏测试脚本")
    print(f"⏰ 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 准备测试列表
    test_games = GAMES.copy()
    if mode == "random" and num_games:
        random.shuffle(test_games)
        test_games = test_games[:num_games]
    elif mode == "random":
        random.shuffle(test_games)

    # 开始测试
    print(f"📋 测试模式: {mode}")
    print(f"🎯 测试数量: {len(test_games)} 款游戏")
    print()

    for i, (filename, name) in enumerate(test_games, 1):
        print(f"[{i}/{len(test_games)}] 测试: {name}")
        print(f"  文件: {filename}")

        # 检查文件是否存在
        exists, filesize = test_game_exists(filename)
        if not exists:
            print(f"  ❌ 文件不存在")
            RESULTS.append((name, filename, "文件不存在"))
            print()
            continue

        print(f"  ✅ 文件存在 ({filesize} bytes)")

        # 测试加载
        if mode in ["check", "random"]:
            success, msg = test_game_loads(filename, open_in_browser=False)
        else:  # manual
            success, msg = test_game_loads(filename, open_in_browser=True)
            input("  按回车键继续测试下一个...")

        if success:
            print(f"  ✅ {msg}")
            RESULTS.append((name, filename, "通过"))
        else:
            print(f"  ❌ {msg}")
            RESULTS.append((name, filename, msg))

        print()
        if mode == "manual" and i < len(test_games):
            time.sleep(1)

    # 打印结果
    print_banner("📊 测试结果")
    passed = sum(1 for r in RESULTS if r[2] == "通过")
    total = len(RESULTS)

    print(f"\n📈 统计: {passed}/{total} 游戏通过测试\n")

    for name, filename, status in RESULTS:
        icon = "✅" if status == "通过" else "❌"
        print(f"{icon} {name:20} - {status}")

    print()
    print(f"⏰ 结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 保存结果到文件
    save_results()


def save_results():
    """保存测试结果"""
    filename = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  双人小游戏测试结果\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for name, filename, status in RESULTS:
            f.write(f"{name:20} - {status}\n")
        passed = sum(1 for r in RESULTS if r[2] == "通过")
        f.write(f"\n总计: {passed}/{len(RESULTS)} 通过\n")

    print(f"📄 测试结果已保存到: {filename}")


def main():
    """主函数"""
    print("\n🎮 双人小游戏测试脚本")
    print("-" * 40)
    print("\n请选择测试模式:")
    print("1. 🔍 检查模式 - 检查所有游戏文件存在性和可访问性")
    print("2. 🎲 随机模式 - 随机选择10款游戏进行测试")
    print("3. 👆 手动模式 - 逐个打开游戏在浏览器中手动测试")
    print("4. 📋 列出所有游戏")
    print("0. ❌ 退出")

    choice = input("\n请输入选择 (0-4): ").strip()

    if choice == "1":
        run_tests("check")
    elif choice == "2":
        run_tests("random", num_games=10)
    elif choice == "3":
        run_tests("manual")
    elif choice == "4":
        print_banner("📋 游戏列表")
        for i, (file, name) in enumerate(GAMES, 21):
            print(f"{i:2d}. {name}")
        print()
    elif choice == "0":
        print("👋 再见！")
        sys.exit(0)
    else:
        print("❌ 无效选择")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 测试中断，再见！")
        sys.exit(0)
