from requests_toolbelt import MultipartEncoder
import requests
url="http://bxjg.circ.gov.cn/tabid/5254/Default.aspx"

m = MultipartEncoder(fields={'__EVENTTARGET': 'ess$ctr16713$OrganizationList$lbnToPage',
                             '__VIEWSTATE': "/wEPDwUJNjcwNjk2ODMxD2QWBmYPFgIeBFRleHQFeTwhRE9DVFlQRSBodG1sIFBVQkxJQyAiLS8vVzNDLy9EVEQgWEhUTUwgMS4wIFRyYW5zaXRpb25hbC8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9UUi94aHRtbDEvRFREL3hodG1sMS10cmFuc2l0aW9uYWwuZHRkIj5kAgEPZBYQAgUPFgIeB1Zpc2libGVoZAIGDxYCHgdjb250ZW50BRLkv53pmanmnLrmnoTmn6Xor6JkAgcPFgIfAgUu5Lit5Zu95L+d6Zmp55uR552j566h55CG5aeU5ZGY5LyaLEVhc3lTaXRlLEVTU2QCCA8WAh8CBTlDb3B5cmlnaHQgMjAxMSBieSBIdWlsYW4gSW5mb3JtYXRpb24gVGVjaG5vbG9neSBDby4sIEx0ZC5kAgkPFgIfAgUJRWFzeVNpdGUgZAIKDxYCHwIFIeS4reWbveS/nemZqeebkeedo+euoeeQhuWnlOWRmOS8mmQCDQ8WAh8CBQ1JTkRFWCwgRk9MTE9XZAIRDxYCHglpbm5lcmh0bWwFvg8uZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1iY3RyIHtib3JkZXItYm90dG9tOiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJvcmRlci1sZWZ0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJvcmRlci10b3A6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7ICBiYWNrZ3JvdW5kLWNvbG9yOiBUcmFuc3BhcmVudDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1iYXIge2N1cnNvcjogcG9pbnRlcjsgY3Vyc29yOiBoYW5kOyBoZWlnaHQ6MDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1pdG0ge2N1cnNvcjogcG9pbnRlcjsgY3Vyc29yOiBoYW5kOyBjb2xvcjogVHJhbnNwYXJlbnQ7IGZvbnQtc2l6ZTogMTJwdDsgZm9udC13ZWlnaHQ6IG5vcm1hbDsgZm9udC1zdHlsZTogbm9ybWFsOyBib3JkZXItbGVmdDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyBib3JkZXItYm90dG9tOiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJvcmRlci10b3A6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7fQ0KLmVzc19lc3NtZW51X2N0bGVzc21lbnVfc3BtaWNuIHtjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgYmFja2dyb3VuZC1jb2xvcjogVHJhbnNwYXJlbnQ7IGJvcmRlci1sZWZ0OiBUcmFuc3BhcmVudCAxcHggc29saWQ7IGJvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDFweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMXB4IHNvbGlkOyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiA1O2hlaWdodDogMDtkaXNwbGF5Om5vbmU7fQ0KLmVzc19lc3NtZW51X2N0bGVzc21lbnVfc3Btc3ViIHt6LWluZGV4OiAxMDAwOyBjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgYmFja2dyb3VuZC1jb2xvcjogVHJhbnNwYXJlbnQ7IGZpbHRlcjpwcm9naWQ6RFhJbWFnZVRyYW5zZm9ybS5NaWNyb3NvZnQuU2hhZG93KGNvbG9yPSdEaW1HcmF5JywgRGlyZWN0aW9uPTEzNSwgU3RyZW5ndGg9MykgO2JvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLWxlZnQ6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyBib3JkZXItcmlnaHQ6IFRyYW5zcGFyZW50IDBweCBzb2xpZDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1icmsge2JvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLWxlZnQ6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyAgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJhY2tncm91bmQtY29sb3I6IFdoaXRlOyBoZWlnaHQ6IDBweDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1pdG1zZWwge2JhY2tncm91bmQtY29sb3I6IFRyYW5zcGFyZW50OyBjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgY29sb3I6IFRyYW5zcGFyZW50OyBmb250LXNpemU6IDEycHQ7IGZvbnQtd2VpZ2h0OiBub3JtYWw7IGZvbnQtc3R5bGU6IG5vcm1hbDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1hcncge2ZvbnQtZmFtaWx5OiB3ZWJkaW5nczsgZm9udC1zaXplOiAxMHB0OyBjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAxcHggc29saWQ7IGJvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDFweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyBkaXNwbGF5Om5vbmU7fQ0KLmVzc19lc3NtZW51X2N0bGVzc21lbnVfc3BtcmFydyB7Zm9udC1mYW1pbHk6IHdlYmRpbmdzOyBmb250LXNpemU6IDEwcHQ7IGN1cnNvcjogcG9pbnRlcjsgY3Vyc29yOiBoYW5kO30NCi5lc3NfZXNzbWVudV9jdGxlc3NtZW51X3NwbWl0bXNjciB7d2lkdGg6IDEwMCU7IGZvbnQtc2l6ZTogNnB0O30NCmQCAg9kFgICAQ9kFgZmD2QWAmYPFgIfAWgWBAIBD2QWBAIDDxBkZBYAZAIFDw8WAh8BaGRkAgMPZBYEZg8UKwACFCsAAg8WBh4NU2VsZWN0ZWRJbmRleGYeBFNraW4FB0RlZmF1bHQeE0VuYWJsZUVtYmVkZGVkU2tpbnNoZBAWBmYCAQICAgMCBAIFFgYUKwACZGQUKwACZGQUKwACDxYCHwFoZGQUKwACDxYCHwFoZGQUKwACZGQUKwACZGQPFgZmZmZmZmYWAQVuVGVsZXJpay5XZWIuVUkuUmFkVGFiLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDExLjEuNTE5LjM1LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTEyMWZhZTc4MTY1YmEzZDRkFgQCAg8PFgIfAWhkZAIDDw8WAh8BaGRkAgEPFCsAAg8WAh8EZmQVBghQYWdlSG9tZQtQYWdlQ3VycmVudAxQYWdlRmF2b3JpdGUKUGFnZU1hbmFnZQhQYWdlU2l0ZQ5QYWdlSG9zdFN5c3RlbRYEAgIPDxYCHwFoZGQCAw8PFgIfAWhkZAIKD2QWAmYPZBYIZg9kFgICAg9kFgQCAQ8PFgIfAWhkZAIDD2QWAgIBDw9kFgIeBWNsYXNzBQlNb2RDSW5mb0NkAgIPZBYCAgIPZBYEAgEPDxYCHwFoZGQCAw9kFgICAQ8PZBYCHwcFEE1vZFRvd0xldmVsTWVudUNkAgQPZBYOAgIPZBYEAgEPDxYCHwFoZGQCAw9kFgICAQ8PZBYCHwcFH01vZEVTU0NvcnBDSVJDRVNTNkluc3VyYW5jZU9yZ0MWAgIBDw8WBh4HUGFn",
                             "__VIEWSTATEGENERATOR":"CA0B0334",
                             "__EVENTARGUMENT":'',
                             "ScrollTop":'',
                             "__essVariable":'',
                             "ess$ctr16712$OrganizationList$lblAtPageNum":'',
                             "ess$ctr16713$OrganizationList$lblAtPageNum":'3',
                             "ess$ctr16714$OrganizationList$lblAtPageNum":'',
                             "ess$ctr16715$OrganizationList$lblAtPageNum":'',
                             "ess$ctr16716$OrganizationList$lblAtPageNum":'',
                             "ess$ctr16720$OrganizationList$lblAtPageNum":'',
                             "ess$ctr26624$OrganizationList$lblAtPageNum":'',
                             })




header={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
                "Host": "bxjg.circ.gov.cn",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Referer" : "http://bxjg.circ.gov.cn/tabid/5254/Default.aspx",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "zip, deflate",
                "Cookie":".ASPXANONYMOUS=TIrGFSeW1AEkAAAAOWVlMjY4ZjMtMWJkNy00NzdlLWEzOTQtYmJhMTM3NjA3MWZi0; language_0=en-US; COOKIE_USERID=LTE`; ASP.NET_SessionId=hdwyodygd0ro4355nxgy0355",
                "Content-Type": "multipart/form-data; boundary=---------------------------5661172516428",
        }
#注意\r\n与\n的区别
Data =	"-----------------------------5661172516428" +\
		"content-disposition: form-data; name='__EVENTTARGET'\r\n"+\
		"\r\n" + \
		"ess$ctr16713$OrganizationList$lbnToPage"+\
        "-----------------------------5661172516428\r\n" +\
        "content-disposition: form-data; name=\"__VIEWSTATEGENERATOR\"\r\n" +\
        "\r\n" + \
        "CA0B0334"+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"__EVENTARGUMENbT\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"__VIEWSTATEGENERATOR\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"__ScrollTop\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"__essVarialble\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"__VIEWSTATE\"\r\n" +\
        "\r\n" + \
        "/wEPDwUJNjcwNjk2ODMxD2QWBmYPFgIeBFRleHQFeTwhRE9DVFlQRSBodG1sIFBVQkxJQyAiLS8vVzNDLy9EVEQgWEhUTUwgMS4wIFRyYW5zaXRpb25hbC8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9UUi94aHRtbDEvRFREL3hodG1sMS10cmFuc2l0aW9uYWwuZHRkIj5kAgEPZBYQAgUPFgIeB1Zpc2libGVoZAIGDxYCHgdjb250ZW50BRLkv53pmanmnLrmnoTmn6Xor6JkAgcPFgIfAgUu5Lit5Zu95L+d6Zmp55uR552j566h55CG5aeU5ZGY5LyaLEVhc3lTaXRlLEVTU2QCCA8WAh8CBTlDb3B5cmlnaHQgMjAxMSBieSBIdWlsYW4gSW5mb3JtYXRpb24gVGVjaG5vbG9neSBDby4sIEx0ZC5kAgkPFgIfAgUJRWFzeVNpdGUgZAIKDxYCHwIFIeS4reWbveS/nemZqeebkeedo+euoeeQhuWnlOWRmOS8mmQCDQ8WAh8CBQ1JTkRFWCwgRk9MTE9XZAIRDxYCHglpbm5lcmh0bWwFvg8uZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1iY3RyIHtib3JkZXItYm90dG9tOiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJvcmRlci1sZWZ0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJvcmRlci10b3A6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7ICBiYWNrZ3JvdW5kLWNvbG9yOiBUcmFuc3BhcmVudDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1iYXIge2N1cnNvcjogcG9pbnRlcjsgY3Vyc29yOiBoYW5kOyBoZWlnaHQ6MDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1pdG0ge2N1cnNvcjogcG9pbnRlcjsgY3Vyc29yOiBoYW5kOyBjb2xvcjogVHJhbnNwYXJlbnQ7IGZvbnQtc2l6ZTogMTJwdDsgZm9udC13ZWlnaHQ6IG5vcm1hbDsgZm9udC1zdHlsZTogbm9ybWFsOyBib3JkZXItbGVmdDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyBib3JkZXItYm90dG9tOiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJvcmRlci10b3A6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7fQ0KLmVzc19lc3NtZW51X2N0bGVzc21lbnVfc3BtaWNuIHtjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgYmFja2dyb3VuZC1jb2xvcjogVHJhbnNwYXJlbnQ7IGJvcmRlci1sZWZ0OiBUcmFuc3BhcmVudCAxcHggc29saWQ7IGJvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDFweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMXB4IHNvbGlkOyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiA1O2hlaWdodDogMDtkaXNwbGF5Om5vbmU7fQ0KLmVzc19lc3NtZW51X2N0bGVzc21lbnVfc3Btc3ViIHt6LWluZGV4OiAxMDAwOyBjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgYmFja2dyb3VuZC1jb2xvcjogVHJhbnNwYXJlbnQ7IGZpbHRlcjpwcm9naWQ6RFhJbWFnZVRyYW5zZm9ybS5NaWNyb3NvZnQuU2hhZG93KGNvbG9yPSdEaW1HcmF5JywgRGlyZWN0aW9uPTEzNSwgU3RyZW5ndGg9MykgO2JvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLWxlZnQ6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyBib3JkZXItcmlnaHQ6IFRyYW5zcGFyZW50IDBweCBzb2xpZDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1icmsge2JvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLWxlZnQ6IFRyYW5zcGFyZW50IDBweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyAgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAwcHggc29saWQ7IGJhY2tncm91bmQtY29sb3I6IFdoaXRlOyBoZWlnaHQ6IDBweDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1pdG1zZWwge2JhY2tncm91bmQtY29sb3I6IFRyYW5zcGFyZW50OyBjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgY29sb3I6IFRyYW5zcGFyZW50OyBmb250LXNpemU6IDEycHQ7IGZvbnQtd2VpZ2h0OiBub3JtYWw7IGZvbnQtc3R5bGU6IG5vcm1hbDt9DQouZXNzX2Vzc21lbnVfY3RsZXNzbWVudV9zcG1hcncge2ZvbnQtZmFtaWx5OiB3ZWJkaW5nczsgZm9udC1zaXplOiAxMHB0OyBjdXJzb3I6IHBvaW50ZXI7IGN1cnNvcjogaGFuZDsgYm9yZGVyLXJpZ2h0OiBUcmFuc3BhcmVudCAxcHggc29saWQ7IGJvcmRlci1ib3R0b206IFRyYW5zcGFyZW50IDFweCBzb2xpZDsgYm9yZGVyLXRvcDogVHJhbnNwYXJlbnQgMHB4IHNvbGlkOyBkaXNwbGF5Om5vbmU7fQ0KLmVzc19lc3NtZW51X2N0bGVzc21lbnVfc3BtcmFydyB7Zm9udC1mYW1pbHk6IHdlYmRpbmdzOyBmb250LXNpemU6IDEwcHQ7IGN1cnNvcjogcG9pbnRlcjsgY3Vyc29yOiBoYW5kO30NCi5lc3NfZXNzbWVudV9jdGxlc3NtZW51X3NwbWl0bXNjciB7d2lkdGg6IDEwMCU7IGZvbnQtc2l6ZTogNnB0O30NCmQCAg9kFgICAQ9kFgZmD2QWAmYPFgIfAWgWBAIBD2QWBAIDDxBkZBYAZAIFDw8WAh8BaGRkAgMPZBYEZg8UKwACFCsAAg8WBh4NU2VsZWN0ZWRJbmRleGYeBFNraW4FB0RlZmF1bHQeE0VuYWJsZUVtYmVkZGVkU2tpbnNoZBAWBmYCAQICAgMCBAIFFgYUKwACZGQUKwACZGQUKwACDxYCHwFoZGQUKwACDxYCHwFoZGQUKwACZGQUKwACZGQPFgZmZmZmZmYWAQVuVGVsZXJpay5XZWIuVUkuUmFkVGFiLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDExLjEuNTE5LjM1LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTEyMWZhZTc4MTY1YmEzZDRkFgQCAg8PFgIfAWhkZAIDDw8WAh8BaGRkAgEPFCsAAg8WAh8EZmQVBghQYWdlSG9tZQtQYWdlQ3VycmVudAxQYWdlRmF2b3JpdGUKUGFnZU1hbmFnZQhQYWdlU2l0ZQ5QYWdlSG9zdFN5c3RlbRYEAgIPDxYCHwFoZGQCAw8PFgIfAWhkZAIKD2QWAmYPZBYIZg9kFgICAg9kFgQCAQ8PFgIfAWhkZAIDD2QWAgIBDw9kFgIeBWNsYXNzBQlNb2RDSW5mb0NkAgIPZBYCAgIPZBYEAgEPDxYCHwFoZGQCAw9kFgICAQ8PZBYCHwcFEE1vZFRvd0xldmVsTWVudUNkAgQPZBYOAgIPZBYEAgEPDxYCHwFoZGQCAw9kFgICAQ8PZBYCHwcFH01vZEVTU0NvcnBDSVJDRVNTNkluc3VyYW5jZU9yZ0MWAgIBDw8WBh4HUGFn"+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"ess$ctr16712$OrganizationList$lblAtPageNum\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"ess$ctr16713$OrganizationList$lblAtPageNum\"\r\n" +\
        "\r\n" + \
        '3'+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"ess$ctr16714$OrganizationList$lblAtPageNum\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"ess$ctr16715$OrganizationList$lblAtPageNum\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"ess$ctr16716$OrganizationList$lblAtPageNum\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"ess$ctr16720$OrganizationList$lblAtPageNum\"\r\n" +\
        "\r\n" + \
        ''+\
        "-----------------------------5661172516428" +\
        "content-disposition: form-data; name=\"ess$ctr26624$OrganizationList$lblAtPageNum\"\r\n" +\
        "\r\n" + \
        '3'+\
        "-----------------------------5661172516428--"


if __name__=='__main__':
    s = requests.session()
    r=s.post(url,data=Data,headers=header)
    with open('zhihu_explore_new.html', 'w', encoding='utf-8') as f:
        f.write(r.text)

