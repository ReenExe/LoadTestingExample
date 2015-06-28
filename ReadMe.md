```bash
vagrant up
```

in vargant
```bash
cd /var/www/lte
```

start server:
```bash
sudo php -S 0.0.0.0:80
```

start locust
```bash
locust -f LocustStressTesting.py --host=http://lte.try
```

for see - go to http://lte.try:8089/