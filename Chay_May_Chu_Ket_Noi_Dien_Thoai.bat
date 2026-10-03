@echo off
chcp 65001 >nul
title MAY CHU LOCAL - BAO CAO CONG VIEC BP QTTS
cd /d "%~dp0"
python server.py
pause
