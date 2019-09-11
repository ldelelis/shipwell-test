
def noaa_response_mock(_):
    return {"today": {
        "high": {
            "fahrenheit": "68",
            "celsius": "20"
            },
        "low": {
            "fahrenheit": "50",
            "celsius": "10"
            },
        "current": {
            "fahrenheit": "55",
            "celsius": "12"
            }
        }
    }

def accuweather_response_mock(_):
    return {"simpleforecast": {
        "forecastday": [{
            "period": 1,
            "high": {
                "fahrenheit": "68",
                "celsius": "20"
                },
            "low": {
                "fahrenheit": "50",
                "celsius": "10"
                },
            "current": {
                "fahrenheit": "55",
                "celsius": "12"
                },
            "conditions": "Partly Cloudy",
            "icon": "partlycloudy",
            "icon_url": "http://icons-ak.wxug.com/i/c/k/partlycloudy.gif",
            "skyicon": "mostlysunny",
            "pop": 0,
            "qpf_allday": {
                "in": 0.00,
                "mm": 0.0
                }
            }]
        }
    }

def weatherdotcom_response_mock(_):
    return {
            "query": {
                "count": 1,
                "created": "2017-09-21T17:00:22Z",
                "lang": "en-US",
                "results": {
                    "channel": {
                        "units": {
                            "temperature": "F"
                            },
                        "description": "Current Weather",
                        "language": "en-us",
                        "lastBuildDate": "Thu, 21 Sep 2017 09:00 AM AKDT",
                        "ttl": "60",
                        "condition": {
                            "code": "33",
                            "date": "Thu, 21 Sep 2017 08:00 AM AKDT",
                            "temp": "37",
                            "text":
                            "Mostly Clear"
                        },
                        "atmosphere": {
                            "humidity": "80",
                            "pressure":
                            "1014.0",
                            "rising": "0",
                            "visibility":
                            "16.1"
                            },
                        "astronomy": {
                            "sunrise": "8:42 am",
                            "sunset": "9:16 pm"
                        },
                        "item": {
                            "title":
                            "Conditions for Nome, AK, US at 08:00 AM AKDT",
                            "lat":
                            "64.499474",
                            "long":
                            "-165.405792",
                            "pubDate":
                            "Thu, 21 Sep 2017 08:00 AM AKDT",
                            "guid":
                            {
                                "isPermaLink": "false"
                                }
                            }
                        }
                        }}}
