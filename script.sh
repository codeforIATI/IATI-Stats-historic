#!/bin/bash

mkdir dashboard-blacklist
cd dashboard-blacklist
wget "http://dashboard.iatistandard.org/stats-blacklist/gitaggregate-dated.tar.gz" -O gitaggregate-dated.tar.gz
wget "http://dashboard.iatistandard.org/stats-blacklist/gitaggregate-publisher-dated.tar.gz" -O gitaggregate-publisher-dated.tar.gz
tar -xf gitaggregate-dated.tar.gz
tar -xf gitaggregate-publisher-dated.tar.gz
rm -rf *.tar.gz
cd ..

mkdir dashboard
cd dashboard
wget "http://dashboard.iatistandard.org/stats/gitaggregate-dated.tar.gz" -O gitaggregate-dated.tar.gz
wget "http://dashboard.iatistandard.org/stats/gitaggregate-publisher-dated.tar.gz" -O gitaggregate-publisher-dated.tar.gz
tar -xf gitaggregate-dated.tar.gz
tar -xf gitaggregate-publisher-dated.tar.gz
rm -rf *.tar.gz
cd ..

mkdir publishingstats-blacklist
cd publishingstats-blacklist
wget "http://publishingstats.iatistandard.org/stats-blacklist/gitaggregate-dated.tar.gz" -O gitaggregate-dated.tar.gz
wget "http://publishingstats.iatistandard.org/stats-blacklist/gitaggregate-publisher-dated.tar.gz" -O gitaggregate-publisher-dated.tar.gz
tar -xf gitaggregate-dated.tar.gz
tar -xf gitaggregate-publisher-dated.tar.gz
rm -rf *.tar.gz
cd ..

mkdir publishingstats
cd publishingstats
wget "http://publishingstats.iatistandard.org/stats/gitaggregate-dated.tar.gz" -O gitaggregate-dated.tar.gz
wget "http://publishingstats.iatistandard.org/stats/gitaggregate-publisher-dated.tar.gz" -O gitaggregate-publisher-dated.tar.gz
tar -xf gitaggregate-dated.tar.gz
tar -xf gitaggregate-publisher-dated.tar.gz
rm -rf *.tar.gz
cd ..

python script.py
