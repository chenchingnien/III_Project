

# 啟動Window CMD執行Selenium伺服器
system("cmd.exe", ignore.stdout = T, ignore.stderr = T, input = paste("cd /r_work"), show.output.on.console = F ,minimized = F, invisible = T)
system("cmd.exe", ignore.stdout = T, ignore.stderr = T, input = paste("java -Dwebdriver.chrome.driver=C:/r_work/chromedriver.exe -Dwebdriver.gecko.driver=C:/r_work/geckodriver.exe -jar selenium-server-standalone-3.141.59.jar"), show.output.on.console = F,minimized = F, invisible = T)
