# InventoryTracker
A simple inventory tracking web application for a logistics company. 

## Installation
Clone:
```
$ git clone https://github.com/ChrisPappin/InventoryTracker.git
$ cd InventoryTracker
```

Create the virtual environment and install the depencies:
```
$ python -m venv myenv  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env\Scripts\activate #myenv/bin/activate for non-Windows
$ pip install -r requirements.txt
```

Generate fake data and run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```