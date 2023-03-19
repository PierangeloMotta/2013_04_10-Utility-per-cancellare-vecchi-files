@rem forfiles -p "C:\temp" -s -m *.* -d 45 -c "cmd /c del @path"
forfiles /p "C:\temp" /s /m *.* /d -30 /c "cmd /c echo @path && echo @path cancellato >> C:\temp\log.txt"