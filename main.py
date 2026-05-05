# -*- coding: utf-8 -*-
from scripts.download_list_api import get_downloads_path
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="本地下载目录查看接口")

@app.get("/downloads", summary="获取下载目录下的文件/文件夹列表")
async def list_downloads():
    """
    返回下载目录下的所有文件和文件夹名称列表，
    每个条目包含名称和类型（file/dir）
    """
    downloads_dir = get_downloads_path()

    if not downloads_dir.exists():
        raise HTTPException(status_code=404, detail="下载目录不存在")
    if not downloads_dir.is_dir():
        raise HTTPException(status_code=500, detail="下载路径不是目录")

    try:
        items = []
        for item in downloads_dir.iterdir():
            items.append({
                "name": item.name,
                "type": "directory" if item.is_dir() else "file"
            })
        # 可选：按名称排序
        items.sort(key=lambda x: x["name"].lower())
        return {"path": str(downloads_dir), "items": items}
    except PermissionError:
        raise HTTPException(status_code=403, detail="无权限访问下载目录")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"读取目录失败: {str(e)}")



# 如果直接运行本脚本，启动 uvicorn 服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)