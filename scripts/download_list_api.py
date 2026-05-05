# -*- coding: utf-8 -*-
# download_list_api.py
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse



def get_downloads_path() -> Path:
    """获取当前用户的下载目录路径（Windows/跨平台兼容）"""
    home = Path.home()
    # Windows 标准下载目录：C:\Users\<用户名>\Downloads
    downloads_path = home / "Downloads"
    return downloads_path



