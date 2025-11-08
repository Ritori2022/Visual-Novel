@echo off
REM Ren'Py Web 自动打包并部署到GitHub Pages
REM 作者：Luna
REM 用途：自动化构建并部署《漩涡与萤火》到网页版本

setlocal enabledelayedexpansion

echo ==========================================
echo 《漩涡与萤火》Web版本自动部署脚本
echo ==========================================
echo.

REM 配置变量
set PROJECT_NAME=vortex_and_firefly
set GITHUB_REPO=https://github.com/Ritori2022/Visual-Novel.git
set VERSION=1.0

REM 检测Ren'Py SDK
echo 步骤 1/5: 检测Ren'Py SDK...

REM 尝试多个可能的Ren'Py位置
set RENPY_FOUND=0

if exist "renpy-8.2.1-sdk\renpy.exe" (
    set RENPY_EXE=renpy-8.2.1-sdk\renpy.exe
    set RENPY_FOUND=1
    goto :renpy_found
)

if exist "..\renpy-8.2.1-sdk\renpy.exe" (
    set RENPY_EXE=..\renpy-8.2.1-sdk\renpy.exe
    set RENPY_FOUND=1
    goto :renpy_found
)

if exist "renpy.exe" (
    set RENPY_EXE=renpy.exe
    set RENPY_FOUND=1
    goto :renpy_found
)

if exist "C:\renpy\renpy.exe" (
    set RENPY_EXE=C:\renpy\renpy.exe
    set RENPY_FOUND=1
    goto :renpy_found
)

:renpy_not_found
echo [错误] 未找到Ren'Py SDK
echo.
echo 请确保Ren'Py SDK在以下位置之一:
echo   1. 当前目录下的 renpy-8.2.1-sdk\
echo   2. 上级目录的 renpy-8.2.1-sdk\
echo   3. C:\renpy\
echo.
echo 下载Ren'Py SDK: https://www.renpy.org/latest.html
pause
exit /b 1

:renpy_found
echo [成功] 找到Ren'Py SDK: %RENPY_EXE%

REM 检查项目是否存在
echo.
echo 步骤 2/5: 检查项目文件...

if not exist "%PROJECT_NAME%" (
    echo [错误] 找不到项目目录 '%PROJECT_NAME%'
    echo 请确保此脚本在 Visual-Novel 仓库根目录运行
    pause
    exit /b 1
)

echo [成功] 项目目录存在

REM 构建Web版本
echo.
echo 步骤 3/5: 构建Web版本...
echo 这可能需要5-15分钟，请耐心等待...

REM 使用Ren'Py命令行构建web版本
"%RENPY_EXE%" launcher distribute "%PROJECT_NAME%" --package web

REM 检查构建是否成功
set WEB_BUILD=%PROJECT_NAME%-%VERSION%-web.zip
if not exist "%WEB_BUILD%" (
    echo [错误] 构建失败: 找不到 %WEB_BUILD%
    pause
    exit /b 1
)

echo [成功] Web版本构建成功!

REM 解压Web版本
echo.
echo 步骤 4/5: 解压Web版本...

REM 清理旧的部署目录
if exist web_deploy rmdir /s /q web_deploy
mkdir web_deploy

REM 解压（使用PowerShell）
powershell -command "Expand-Archive -Path '%WEB_BUILD%' -DestinationPath 'web_deploy' -Force"

REM 找到解压后的目录
for /d %%D in (web_deploy\%PROJECT_NAME%*) do set WEB_DIR=%%D

if not defined WEB_DIR (
    echo [错误] 找不到解压后的目录
    pause
    exit /b 1
)

echo [成功] 解压成功: %WEB_DIR%

REM 部署到GitHub Pages
echo.
echo 步骤 5/5: 部署到GitHub Pages...

cd /d "%WEB_DIR%"

REM 初始化git仓库
git init
git checkout -b gh-pages

REM 添加所有文件
git add .

REM 提交
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)
set COMMIT_MSG=Deploy web build %mydate% %mytime%
git commit -m "%COMMIT_MSG%"

REM 推送到GitHub Pages
echo.
echo 正在推送到GitHub Pages...

REM 添加远程仓库（如果已存在会失败，但不影响）
git remote add origin "%GITHUB_REPO%" 2>nul

REM 强制推送到gh-pages分支
git push -f origin gh-pages

cd ..\..

echo.
echo ==========================================
echo [成功] 部署完成!
echo ==========================================
echo.
echo 你的游戏将在5-10分钟后可访问:
echo https://ritori2022.github.io/Visual-Novel/
echo.
echo 提示:
echo   - 如果无法访问，请到GitHub仓库设置中启用GitHub Pages
echo   - Settings -^> Pages -^> Source: gh-pages 分支
echo.

REM 清理临时文件（可选）
set /p cleanup="是否删除临时文件? (Y/N): "
if /i "%cleanup%"=="Y" (
    rmdir /s /q web_deploy
    del /q "%WEB_BUILD%"
    echo [成功] 临时文件已清理
)

echo.
echo 脚本执行完毕！
pause
