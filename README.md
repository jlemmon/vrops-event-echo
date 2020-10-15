# vrops-event-echo
A simple webhook shim for echoing vR Ops alerts, which can be used to later send to other systems such as Splunk via HEC

This is completely based on https://github.com/prydin/vrops-splunk.git.  Thanks @prydin! 

## Installing
Ensure you have pip or pip3 available on your system.  For Ubuntu 20.04, that looks like:

```
apt-get update && apt-get install 
```

Once that's complete:
```
git clone https://github.com/jlemmon/vrops-event-echo.git
cd vrops-event-echo
pip install -r requirements.txt
```

Note: On Mac, you may have to replace ```pip``` with ```pip3```

## Usage
Start the server using the following commands:

```
flask run
```

By default, all attributes of the alert are printed as key-value pairs. If you want to change the format, you may
set the ```HEC_FORMAT``` environment variable. It accepts a Python format string that maps to the attributes
of the alert. For example:

```
export HEC_FORMAT="Alert: {alertName}, Criticality: {criticality}, Resource: {resourceName}"
```

If you want a different date format than the default one, you may set the ```HEC_DATE_FORMAT``` environment variable
to a valid Python date formatting string.
