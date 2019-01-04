#!/usr/bin/env bash
openssl genrsa -out key.pem 2048
openssl req -new -key key.pem -out csr.pem -sha512
openssl req -nodes -newkey rsa:2048 -keyout key.pem -out csr.pem  -sha512
openssl req -new -x509  -days 365 -key key.pem  -out crt.pem -sha512

openssl x509 -noout -modulus -in crt.pem | openssl md5
openssl x509 -noout -modulus -in key.pem | openssl md5
openssl x509 -noout -modulus -in csr.pem | openssl md5
