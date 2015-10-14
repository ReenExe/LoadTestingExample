#!/usr/bin/env bash
echo 'http://lte.try:8089/'
locust -f LocustStressTesting.py --host=http://lte.try