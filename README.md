# SiteSnap - takes screenshots of websites

Usage:
1. `pip install -r requirements.txt`
2. `python site_snap.py` - look at `utils/arguments.py` for tailored usage

Tech:
1. Selenium to launch the browser of choice. Look at `maps/` to understand the various OS's and browsers supported (TLDR: most of them)

Working on the below to make this a fully fledged website scraper:
1. Clearing pop-up messages (for sites where the cookies have not been loaded)
2. Adding EasyOCR to extract the text from the screenshots - this essentially makes this a web scraper
3. Use an LLM to parse the information and output the info in any custom format
