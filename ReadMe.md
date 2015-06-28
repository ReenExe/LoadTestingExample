
```bash
vagrant up --provision
vagrant ssh
```

directory
```bash
cd /var/www/lte
```

in vargant start server http://lte.try:
```bash
sudo php -S 0.0.0.0:80
```

in vargant start locust
```bash
locust -f LocustStressTesting.py --host=http://lte.try
```

for see - go to http://lte.try:8089/
