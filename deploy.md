cd /etc/systemd/system/
touch test_drive.service            # Создание

```
[Unit]
Description=test_drive
After=syslog.target
After=network.target

[Service]
Type=simple
User=lilyxer-pc
WorkingDirectory=/home/lilyxer-pc/my_bot
ExecStart=/home/lilyxer-pc/my_bot/venv_my_bot/bin/python3 /home/lilyxer-pc/my_bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```
sudo systemctl daemon-reload        # Перезагрузка демона
sudo systemctl enable test_drive    # Активация
sudo systemctl start test_drive     # Старт
sudo systemctl status test_drive    # Статус юнита
sudo systemctl stop test_drive      # Остановка
sudo systemctl disable test_drive   # Отключение
sudo systemctl restart test_drive   # Перезапуск после обновления