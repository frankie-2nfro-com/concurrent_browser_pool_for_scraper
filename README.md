# Making a Browser Pool for Your Scraper
This repository is a sample setup for creating a browser pool in Docker for your scraper to access multiple browsers concurrently to improve the overall scraping performance. 

## Step 1: clone this repository:
```
> mkdir <working directory>
> cd <working directory>
> git clone https://github.com/frankie-2nfro-com/concurrent_browser_pool_for_scraper.git
```

## Step 2: Run the browser pool
```
> docker compose up -d
```
The pool will be ready for scraper now. To make sure it is up and running, just access: http://localhost:4444 to check the console page

## Step 3: Access the browser pool 
```
> python scraper.py
```
(if the result is normal, you can start to modify you own scraper code)

## Step 4: Change browser type and number of browser
To optimize the browser pool, you can change parameter in the docker-compose.yaml
