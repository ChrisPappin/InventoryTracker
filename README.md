# InventoryTracker
A simple inventory tracking web application for a logistics company. 

![image](https://user-images.githubusercontent.com/45044493/150242067-26b3c179-edb2-424d-a65f-866f8a2cdf0e.png)

## Installation
Clone the repo:
```
$ git clone https://github.com/ChrisPappin/InventoryTracker.git
$ cd InventoryTracker
```

Create the virtual environment and install the depencies:
```
$ python -m venv myenv  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ myenv\Scripts\activate #myenv/bin/activate for non-Windows
$ pip install -r requirements.txt
```

Create the database and run:
```
$ sqlite3 database.db < schema.sql
$ flask run
* Running on http://127.0.0.1:5000/
```
Note: If "sqlite3 database.db < schema.sql" returns "sqlite3 is not recoginzed as an internal or external command", it is likely due to the Python installation not having sqlite3. In order to fix this sqlite can be downloaded seperately [here](https://www.sqlite.org/download.html). [This](https://www.youtube.com/watch?v=9Mo8jjS-FMQ) is a quick 2 minute tutorial showing how to get it working correctly.
