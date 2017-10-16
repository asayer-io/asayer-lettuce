[<img src="https://dashboard.asayer.io/assets/logo-507f1d735124eb7b629733a52415bd374776bf107c05352184bbb39d8e3f26f5.png" width="235"/>](https://asayer.io)
[<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/lettuce/logo.svg" width="96"/>](http://lettuce.it)

# Asayer - Lettuce (Python)
[Lettuce (Python)](http://lettuce.it) integration with [Asayer](https://asayer.io).

### Table of Contents:
* [Prerequisites](#prerequisites)
* [Set it up](#set-it-up)
* [Run it](#run-it)
* [Dashboard](#dashboard)
   - [Test List](#test-list)
   - [Test Overview](#test-overview)
   - [Session Recording](#session-recording)
   - [Timeline](#timeline)
   - [Screenshots](#screenshots)
   - [Server Logs](#server-logs)
   - [Console Logs](#console-logs)
   - [Assets](#assets)
   - [Tunnels](#tunnels)
* [Application Parameters](#application-parameters)
* [Capabilities](#capabilities)
   - [Supported Mobile Devices](#supported-mobile-devices)
   - [Fun with Flags](#fun-with-flags)
* [Integrating Asayer with your existing project](#integrating-asayer-with-your-existing-project)
* [Local Testing](#local-testing)
   - [Starting the Tunnel](#starting-the-tunnel)
   - [Setting up the tests for Local Testing](#setting-up-the-tests-for-local-testing)
   - [Limitations](#limitations)
* [Mark Session](#mark-session)
* [Dependencies](#dependencies)

## Prerequisites
* [Python](https://www.python.org) 2.7 or newer
* An IDE is optional
    
## Set it up
* Clone the repo `git clone https://github.com/asayer-io/asayer-lettuce.git` or [download it](https://github.com/asayer-io/asayer-lettuce/archive/master.zip)
* Install the required dependencies `pip install -r requirements.txt`
* Update the `asayer.config.json` file under the `config` folder with your Asayer [API key](https://dashboard.asayer.io/settings?f=3)

## Run it
To run the test, proceed as follows:
* In the terminal, execute `lettuce`
* Go to https://dashboard.asayer.io/automate/sessions and see what happened.


## Dashboard
Details about the test session can be found in the [Dashboard](https://dashboard.asayer.io/automate/sessions) under *Automate > Sessions*.

### Test List
This is where all your executed tests are listed. You can use the filter to navigate through *Passed* or *Failed* tests (see [Mark A Completed Test](#mark-a-completed-test) to learn how to mark a test).

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/lettuce/tests-list2.PNG"/>
</p>

### Test Overview
Encloses various details like *State*, *Duration*, *Execution Time*, *Platform*/*Browser* as well as the *User* who initiated the test.

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/lettuce/test+overview2.PNG"/>
</p>

### Session Recording
Each session gets fully recorded. The video can be played or downloaded (as part of the [Assets](#assets)).

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/specflow/video.PNG"/>
</p>

### Timeline
All commands gets displayed in the form of a comprehensive timeline, including details such as *Execution Time*, *Duration* and [*Screenshot*](#screenshots).

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/specflow/timeline2.PNG"/>
</p>

### Screenshots
A screenshot is taken automatically upon the execution of each and every command. Simply hover over the cam icon to see it.

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/specflow/screenshot3.png"/>
</p>

### Server Logs
Various actions (i.e. HTTP) taking place throughout the session, are logged.

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/specflow/log-request-response.PNG"/>
</p>

### Console Logs
Chrome and Opera console logs are captured and displayed back.

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/specflow/console+log.PNG"/>
</p>

### Assets
Clicking on the *Download Assets* button will download a zip file enclosing:
* All screenshots
* Session recording (.webm)
* Server logs
* Browser console logs (only Chrome and Opera)

<p align="center">
<kbd>
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/lettuce/download+assets.png"/>
</kbd>
</p>

### Tunnels
The list of your active tunnels is available in *Settings > Tunnels*. For more information, see [Local Testing](#local-testing).

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/specflow/tunnels+list+3.PNG"/>
</p>

## Application Parameters
You can change the app settings from the [`asayer.config.json`](https://github.com/asayer-io/asayer-lettuce/blob/master/config/asayer.config.json) file.
```
{
  "apikey": "ASAYER API KEY",
  "server": "https://hub.asayer.io/wd/hub",
  "name": "Testing Lettuce with Asayer",
  ...
}
```

Belows are the supported settings:

| Name        | Value           | Description  | Required  |
| :-------------: |:-------------| :-----|:-----:|
| `apikey`|  | Your Asayer [API key](https://dashboard.asayer.io/settings?f=3) | yes |
| `server`|`https://hub.asayer.io/wd/hub` |   Asayer's Selenium hub | yes |
| `name` | |    The name of the test to execute (will be visible in the [Dashboard](#test-overview)) | yes |
| `build` | |The build's ID (if any) | no |
| `tunnelId` | | The tunnel's ID for local tests | yes for ([local testing](#local-testing)) | 

## Capabilities
You can change the caps from the [`asayer.config.json`](https://github.com/asayer-io/asayer-lettuce/blob/master/config/asayer.config.json) file under `capabilities`.

```
{
  ...
  "capabilities": {
    "browserName": "chrome",
    "platform": "any",
    ...
  }
}
```

Below is the list of supported capabilities:

| Name        | Possible Values           | Default Value  |Description  | Required  |
| :-------------: |:-------------| :-----:|:-------------|:-----:|
| `platform`| `linux` `windows` `mac` `android` `ios` `any`| linux | The platform used for the test | yes |
| `browser`|`chrome` `firefox` `ie` `safari` `opera` `edge`| chrome | The browser used for the test | yes |
| `flags`|| - |A list of flags to be passed to the browser, see [Fun with Flags](#fun-with-flags) | no |
| `deviceName`| see the list of [supported mobile devices](#supported-mobile-devices) | - |The android device name to use for the test | yes if `platform` is set to `android` or `ios` |

The supported browser versions are:

| Name        | Version           |
| :-------------: |:-------------:| 
| edge | 15 |
| opera | 48 |
| firefox | 56 |
| chrome | 61 |
| ie | 11 |
| safari | 11.0 |

### Supported Mobile Devices

The list of available mobile simulators/emulators is as below:

| platform | deviceName|
| :-------------: |:-------------| 
| `android` | `Galaxy_S8`, `LG_G6`, `Pixel`, `Pixel_XL`, `Pixel_C`, `Nexus_5X`, `Nexus_6P` `Nexus_9` |
| `ios` | `iPhone 5`, `iPhone 5s`, `iPhone 6`, `iPhone 6 Plus`, `iPhone 6s`, `iPhone 6s Plus`, `iPhone 7`, `iPhone 7 Plus`, `iPhone SE`, `iPad Air`, `iPad Air 2`, `iPad Pro` |

Note: Only `Android 7.1.1` and `iOS 10.3` are supported.

### Fun with Flags

In addition to the above mentioned capabilities, you can attach a list of `flags` (to run the browser with) by simply adding `[FLAG NAME]:[value]` to the [`asayer.config.json`](https://github.com/asayer-io/asayer-lettuce/blob/master/config/asayer.config.json) file under `capabilities:flags`.

In the following example, we used some of the Chrome flags:

```
{
  ...
  "capabilities": {
    ...
    "flags": {
      "--incognito": true,
      "--start-fullscreen": true
      ...
    }
  }
}
```

These flags will be interpreted as `--incognito --start-fullscreen`.

* Kepp in mind that each browser has its **own and unique** list of flags:
    * [FireFox](https://developer.mozilla.org/fr/docs/Mozilla/Command_Line_Options)
    * [Chrome](https://peter.sh/experiments/chromium-command-line-switches/)
    * [IE](https://msdn.microsoft.com/en-us/library/hh826025(v=vs.85).aspx)
    * Safari (no flags)
    * [Opera](http://www.opera.com/docs/switches/)
    
## Integrating Asayer with your existing project
Follow the below steps to integrate Asayer with your existing project:
* Copy the [`AsayerWebDriver.py`](https://github.com/asayer-io/asayer-lettuce/blob/master/features/AsayerWebDriver.py) file to your project under the `features` folder
* Have the required [dependencies](#dependencies) installed
* Copy the [`asayer.config.json`](https://github.com/asayer-io/asayer-lettuce/blob/master/config/asayer.config.json) file to your project under the `config` folder
* Make sure that the `before.each_scenario` hook of the `AsayerWebDriver` file is the only hook initiating the `world.browser` `webDriver` instance
	

## Local Testing
Local testing allows you to test your internal servers, in addition to public URLs, using Asayer's infrastucture without having to update your firewalls or proxies.

### Starting the Tunnel
1. Download `asayer-tunnel` for *Windows* ([32bits](https://s3.eu-central-1.amazonaws.com/asayer-tunnel/asayer-tunnel_win32.exe)\|[64bits](https://s3.eu-central-1.amazonaws.com/asayer-tunnel/asayer-tunnel_win64.exe)), *Linux* ([32bits](https://s3.eu-central-1.amazonaws.com/asayer-tunnel/asayer-tunnel_linux32)\|[64bits](https://s3.eu-central-1.amazonaws.com/asayer-tunnel/asayer-tunnel_linux64)) or *Mac* ([32bits](https://s3.eu-central-1.amazonaws.com/asayer-tunnel/asayer-tunnel_mac32)\|[64bits](https://s3.eu-central-1.amazonaws.com/asayer-tunnel/asayer-tunnel_mac64))
2. Open a terminal and `cd` to the binary folder 
3. Execute the binary by running `asayer-tunnel_win64.exe -k API_KEY -i TUNNEL_NAME` 

The complete manual for the tunnel is the following:

```
$ asayer-tunnel_win64.exe -h
Usage:
  main [OPTIONS]

Application Options:
  -k, --key=            The user API_KEY
  -i, --id=             The id of the tunnel
  -p, --port=           The local proxy port (default: 9090)
  -w, --whitelist=      List of URLs to exclude from proxy, separated by ';' (eg: url1; url2)
      --proxy-url=      If you are behind a proxy set its URL here, the format is HOST:PORT.
                        If needed, auth info can be set in --proxy-user and --proxy-password
      --proxy-user=     Basic auth HTTP Proxy username
      --proxy-password= Basic auth HTTP Proxy password
  -v, --verbose         Show debug information

Help Options:
  -h, --help            Show this help message
```

Note that only `-k` and `-i` parameters are required.

### Setting up the tests for Local Testing
To set up your tests for local testing, you must add the `tunnelId` capability to the [`asayer.config.json`](https://github.com/asayer-io/asayer-lettuce/blob/master/config/asayer.config.json) file

```
{
  ...
  "tunnelId": "[TUNNEL_ID]",
  "capabilities": {
    ...
  }
}
```
Once done, run your tests as [usual](#run-it). HTTP traffic will then be redirected to the machine on which the `asayer-tunnel` binary is running through a secure connection.

Details about the local tests can be found in the [Dashboard](#dashboard). Local tests are marked with a *plug* icon.

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/lettuce/local1.PNG"/>
</p>

### Limitations
* Local Testing is available on `chrome`, `firefox` and `opera` browsers only
* Only 3 active tunnels are allowed per organization

## Mark Session
Once the session is completed, you can mark the test (either passed or failed) by calling the `mark_session(["Passed"|"Failed"])` method of the [`AsayerWebDriver.py`](https://github.com/asayer-io/asayer-lettuce/blob/master/features/AsayerWebDriver.py) file. 

You can also rely on our REST API to do so by submitting `sessionID` and `sessionStatus` parameters:

```
Endpoint: https://dashboard.asayer.io/mark_session
Method: POST
Json: {
        sessionID: world.session_id, // Required
        sessionStatus:"Passed"|"Failed", // Required
        apiKey:"YOUR ASAYER API KEY" | world.apikey, // Required
    }
```

The state will be visible in the Dashboard:

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/lettuce/test+state+2.PNG"/>
</p>

For reporting purposes, you can call the `mark_session_details(state, requirementID, testStatus)` method of the [`AsayerWebDriver.py`](https://github.com/asayer-io/asayer-lettuce/blob/master/features/AsayerWebDriver.py) file.

`mark_session_details`'s parameters are:

- `state`: the session's state
- `requirementID`: the session's requirement ID
- `testStatus`: a dictionary object of `"testId":"testStatus"`

See the example below:

```python
    mark_session_details("Passed", "requirementId1230", {"TEST ID 1":"Passed","TEST ID 2":"Failed"})
```

You can also rely on our REST API by calling:

```
Endpoint: https://dashboard.asayer.io/mark_session
Method: POST
Json: {
        sessionID:$this->sessionId, // Required
        sessionStatus:"Passed"|"Failed", // Required
        apiKey:"YOUR ASAYER API KEY ($this->apikey)", // Required
        reqID: "REQUIREMENT ID", // Required
	    testStatus: { // Required
    		"TEST ID 1":"Passed"|"Failed",
    		"TEST ID 2": "Passed"|"Failed"
		    ...
    	}
    }
```

Note that every step’s status is automatically reported to Asayer throughout the execution of the test. This may be seen in in the Reporting section, as shown below:

<p align="center">
<img src="https://s3.eu-central-1.amazonaws.com/asayer-samples-assets/lettuce/reporting.PNG"/>
</p>

## Dependencies
This project relies on the below dependencies:
- lettuce
- selenium 
- nose
- requests

To install the required dependencies, execute in the terminal `pip install -r requirements.txt`