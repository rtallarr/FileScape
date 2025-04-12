@echo off
setlocal enabledelayedexpansion

:: Search and delete build folders recursively
for /d %%d in (dist,build,FileScape.egg-info) do (
    if exist "%%d" (
        echo Deleting: "%%d"
        rmdir /s /q "%%d"
    )
)

echo Cleanup complete!