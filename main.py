
"""
TaskMaster 主程式入口點
提供統一的命令行介面來啟動不同的應用模式
"""

import sys
import os
from database import DatabaseManager
from task_gui import TaskGUI
from api_server import run_web_server


def run_gui():
    """啟動桌面GUI介面"""
    try:
        
        gui = TaskGUI()
        gui.run()
    except ImportError as e:
        print(f"❌ 無法啟動GUI介面: {e}")
        print("請確認 task_gui.py 模組存在且正確")
        sys.exit(1)
    except Exception as e:
        print(f"❌ GUI啟動失敗: {e}")
        sys.exit(1)


def run_web():
    """啟動Web介面"""
    try:
        
        run_web_server()
    except ImportError as e:
        print(f"❌ 無法啟動Web服務: {e}")
        print("請確認 api_server.py 模組存在且正確")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Web服務啟動失敗: {e}")
        sys.exit(1)


def run_backup():
    """執行資料庫備份"""
    try:
        backup_database()
    except ImportError:
        # 如果 backup_main 不存在，使用簡單的備份方式
        import shutil
        try:
            shutil.copy('tasks.db', 'backup_tasks.db')
            print("✅ 資料庫備份完成: backup_tasks.db")
        except Exception as e:
            print(f"❌ 備份失敗: {e}")
    except Exception as e:
        print(f"❌ 備份失敗: {e}")


def run_database_check():
    """執行資料庫檢查"""
    try:
        # 延遲匯入避免 check_db 模組的 sys.stdout 設定影響其他模式
        from check_db import main as check_db_main
        check_db_main()
    except ImportError as e:
        print(f"❌ 無法執行資料庫檢查: {e}")
        print("請確認 check_db.py 模組存在且正確")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 資料庫檢查失敗: {e}")
        sys.exit(1)


def show_help():
    """顯示使用說明"""
    print("""
TaskMaster - 任務管理系統

用法: python main.py <模式>

可用模式:
  gui       啟動桌面GUI介面
  api/web   啟動Web API服務 (瀏覽器訪問 http://127.0.0.1:5000)
  backup    執行資料庫備份
  check     執行資料庫檢查
  help      顯示此說明

範例:
  python main.py gui      # 啟動桌面應用
  python main.py api      # 啟動Web API服務
  python main.py backup   # 備份資料庫
  python main.py check    # 檢查資料庫狀態

系統需求:
  - Python 3.11+
  - Flask (Web模式)
  - tkinter (GUI模式，通常內建)

更多資訊請查看 README.md
    """)


def initialize_database():
    """初始化資料庫（如果需要）"""
    try:
        
        db_manager = DatabaseManager()
        db_manager.initialize()
    except ImportError:
        # 如果 database 模組不存在，使用簡單的初始化
        import sqlite3
        try:
            conn = sqlite3.connect('tasks.db')
            conn.execute('''CREATE TABLE IF NOT EXISTS tasks
                           (id INTEGER PRIMARY KEY, title TEXT, description TEXT,
                            priority TEXT, status TEXT, created_at TEXT)''')
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"⚠️  資料庫初始化警告: {e}")
    except Exception as e:
        print(f"⚠️  資料庫初始化警告: {e}")


def main():
    """主程式入口"""
    # 初始化資料庫
    initialize_database()

    # 解析命令行參數
    if len(sys.argv) < 2:
        print("❌ 請指定執行模式")
        show_help()
        sys.exit(1)

    mode = sys.argv[1].lower()

    # 路由到對應的功能
    if mode == "gui":
        print("🖥️  啟動桌面GUI介面...")
        run_gui()
    elif mode in ["web", "api"]:
        print("🌐 啟動Web API服務...")
        run_web()
    elif mode == "backup":
        print("💾 執行資料庫備份...")
        run_backup()
    elif mode == "check":
        print("🔍 執行資料庫檢查...")
        run_database_check()
    elif mode in ["help", "-h", "--help"]:
        show_help()
    else:
        print(f"❌ 未知的模式: {mode}")
        show_help()
        sys.exit(1)


if __name__ == "__main__":
    main()