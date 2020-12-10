# Client Script Injection Kit (CSIK)

This simple Flask server app is meant to back cross-site scripting (XSS) proof-of-concept examples. Its main function is providing facilities for capturing and logging data from various events. It also contains some crude example scripts for actually submitting data to the server.

**Note** Future development, if any, will be done in the https://github.com/mgillam/csik repo.

## Disclaimers
Although this project does *not* contain any exploit code, we would like to remind you to always be certain you have explicit, written permission before testing an application.

Pull requests are welcome, however maintaining this project is not a priority for the original author. YMMV

Currently TLS isn't used in any sort of built-in form. A stop-gap measure is to run it behind a reverse proxy e.g. nginx

## Prereqs
Python 3.x - this version was developed on 3.6.

## Setting up
 1. Clone the repo and `cd` into the directory.
 2. Run `pip install -r requirements`
 3. `python csik.py`
 
 ## URLs
  - `/hello` test path to verify all is good
  - `/id` return an ID that can be used to uniquely tag subsequent traffic
  - `/x` socket.io data exfiltration endpoint
  - `/s/` alias for the scripts subdirectory. Files retrieved from here are processed with a simple replacement of *$$HOST$$* with the host header of the request.
  - `/<anything else>` XHR/fetch data exfiltration endpoint, where the path becomes the name for the log file.
 
 
 ## Project Structure
  - **csik.py** - the app logic
  - **/scripts** - a place to get payloads from
  - **/logs** - a place where the data gets logged to
  
 
 
