# dovetail_calculator

This project is a flask webapp, designed to receive input from user and calculate the size of a dovetail for dovetail-joined boards.

![Webapp form](form.JPG?raw=true "Form")

## Running Locally

To run this app locally, create a new Python 3.8.3 virtual environment
(such as with `pyenv`). Then, use the following command to update `pip`
and `setuptools`:

```
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
```

And install the required libraries:

```
python3 -m pip install -r requirements.txt
```

The main source code is contained in `app.py`. To run the app, execute

```
python3 app.py
```

To access the app, navigate to `http://127.0.0.1:5000/form` on your browser.

On clickling `Calculate`, you'll be redirected to `http://127.0.0.1:5000/data`, where the results are displayed.

![Webapp data](data.JPG?raw=true "Data")
