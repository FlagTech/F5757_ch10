# TaskMaster - 個人任務管理系統

一個簡單的任務管理應用程式，展示 Claude Code 自定義指令的實際應用。

> **Ch09 專案成果**
> 本專案示範了如何使用 Claude Code 自定義指令進行專案重構，透過 `/auto-fix` 將混亂的程式碼重構為模組化架構。

---

## 🎯 定位下一步

### 目前狀態 (Ch09)
- ✅ 建立本地 Claude Code 自定義指令
- ✅ 實作自動化 Git 工作流程
- ✅ 使用 `/auto-fix` 完成專案重構
- ✅ 中文化提交訊息規範

### 下一步 (Ch10)
- 🔜 將 Claude Code 與 GitHub 協作整合
- 🔜 自定義指令移植到 GitHub 環境
- 🔜 在 GitHub 上應用本地開發的工作流程
- 🔜 實現跨平台的自動化協作

**最後結果請見 custom_tk 分支**

---

## 📋 功能特色

- 桌面 GUI 介面 (Tkinter)
- Web API 服務 (Flask)
- SQLite 資料庫
- 任務管理 (新增、檢視、刪除)

---

## 🚀 快速開始

```bash
# 安裝套件
uv sync

# 啟動 GUI
uv run python main.py gui

# 啟動 API (http://127.0.0.1:5000)
uv run python main.py api
# 或
uv run python main.py web

# 🔍 檢查資料庫狀態
uv run python main.py check

# ❓ 顯示完整說明
uv run python main.py help

```

---

## 🤖 Claude Code 自定義指令

本專案的核心特色是整合了 Claude Code 自定義指令：

### 可用指令

- `/auto-fix` - 自動規劃、實作、提交的完整工作流程
- `/pack-zh` - 中文互動式 Git 提交流程
- `/commit-rules` - Git 提交訊息規範

### 指令檔案位置

```
.claude/
└── commands/
    ├── auto-fix.md       # 自動修復流程
    ├── pack-zh.md        # 中文提交指令
    ├── pack-basic.md     # 基礎提交流程
    ├── pack-direct.md    # 強制執行提交
    └── commit-rules.md   # 提交訊息規範
```

**這些指令也將在 Ch10 中移植到 GitHub 環境使用，只是互動式的指令需要其他處理才能在 GitHub 中順利使用**

---

## 🏗️ 專案架構

```
F5757_ch09/
├── main.py          # 程式入口點
├── database.py      # 資料庫管理
├── task_gui.py      # GUI 介面
├── api_server.py    # API 服務
└── .claude/         # Claude Code 自定義指令（Ch10 將整合至 GitHub）
```

---

## 💻 技術棧

- Python 3.11+
- Tkinter (GUI)
- Flask (API)
- SQLite (資料庫)
- Claude Code 自定義指令

---

## 📝 授權

本專案僅供學習與練習使用。
