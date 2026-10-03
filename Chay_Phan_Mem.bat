@echo off
chcp 65001 >nul
title BÁO CÁO NGÀY CBNV BP QTTS

echo ========================================================
echo   KHỞI ĐỘNG PHẦN MỀM BÁO CÁO NGÀY CBNV BP QTTS
echo ========================================================
echo.
echo Đang mở giao diện phần mềm...
echo.

set "HTML_PATH=%~dp0index.html"

:: Thử mở với Microsoft Edge ở chế độ App (Giao diện như phần mềm Desktop)
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" (
    start "" "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" --app="file:///%HTML_PATH%"
    exit
)

if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" (
    start "" "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" --app="file:///%HTML_PATH%"
    exit
)

:: Thử mở với Google Chrome ở chế độ App
if exist "%ProgramFiles%\Google\Chrome\Application\chrome.exe" (
    start "" "%ProgramFiles%\Google\Chrome\Application\chrome.exe" --app="file:///%HTML_PATH%"
    exit
)

if exist "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" (
    start "" "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" --app="file:///%HTML_PATH%"
    exit
)

:: Nếu không có Edge/Chrome app mode thì mở bằng trình duyệt mặc định
start "" "%HTML_PATH%"
exit
