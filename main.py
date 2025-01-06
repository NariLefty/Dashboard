import flet as ft
import flet.canvas as cv
from flet_timer.flet_timer import Timer
import urllib.request as req
import json
import math
import calendar
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import locale
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

def main(page: ft.Page):
    page.title = ""
    page.window.title_bar_hidden = True # タイトルバーを非表示
    page.window.frameless = True # 枠を非表示
    page.window.width = 1280  # 幅
    page.window.height = 660  # 高さ
    page.window.top = 100  # 位置(TOP)
    page.window.left = 4000  # 位置(LEFT)
    # container size
    ct1_width, ct1_height = page.window.width*0.2, page.window.height*0.2
    ct2_width, ct2_height = page.window.width*0.8, page.window.height*0.2
    ct3_width, ct3_height = page.window.width*0.2, page.window.height*0.63
    ct4_width, ct4_height = page.window.width*0.8, page.window.height*0.63
    # AppBar
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.DASHBOARD),
        # toolbar_height=100,
        title=ft.Text("Dashboard"), # size
        bgcolor=ft.Colors.TRANSPARENT,
    )

    # ============================================================
    # Container 1 date
    ct1_date = ft.Container(
        # widthはrowのexpand
        # height=ct1_height*0.3,  # ページの高さの2割
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=5,
        border_radius=5,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
            controls=[
                ft.Text(" ", size=10, color=ft.Colors.WHITE),
                ft.Text(" . ", size=25, color=ft.Colors.WHITE),
                ft.Text("|", size=25, color=ft.Colors.WHITE12),
                ft.Text(" ", size=25, color=ft.Colors.WHITE)
            ],
        )
    )
    # Container 1 next date
    ct1_next_date = ft.Container(
        # widthはrowのexpand
        # height=ct1_height*0.3,  # ページの高さの2割
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=2,
        border_radius=5,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
            controls=[
                ft.Text("", size=12, color=ft.Colors.WHITE),
                ft.Text(" 月 日  曜日", size=12, color=ft.Colors.WHITE,),
                # ft.Text("大晦日", size=12, color=ft.Colors.WHITE),
            ],
        )
    )
    # Container 1 empty
    ct1_empty = ft.Container(
        # widthはrowのexpand
        # height=ct1_height*0.3,  # ページの高さの2割
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=3,
        border_radius=5,
        content=ft.Text(" ", color=ft.Colors.WHITE),
    )
    # Container 1 Top
    container1_top = ft.Container(
        # width=ct1_width,  # ページの幅の2割 # rowのexpand
        # heightはrowのexpand
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=3,
        border_radius=0,
        content=ft.Row(
            spacing=0,
            controls=[ct1_date, ct1_next_date, ct1_empty],
        )
    )
    # Container 1 Today Calendar
    font = "Menlo"
    font_size = 11
    ct1_calendar = ft.Container(
        # height=container1_bottom,
        # width = expand
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=20,
        border_radius=0,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=2,
            controls=[
                ft.Container(
                    # widthはrowのexpand
                    bgcolor="#232F32",
                    alignment=ft.alignment.center,
                    expand=3,
                    border_radius=2,
                    content=ft.Row(
                        spacing=5,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row([
                                ft.Text("|", size=15, color="#8EE2E9"),
                                ft.Text("予定1", size=15, color="#8EE2E9"),
                            ]),
                            ft.Text("10:00-11:00", size=font_size, color=ft.Colors.WHITE60, font_family=font),
                        ],
                        
                    )
                ),
                ft.Container(
                    # widthはrowのexpand
                    bgcolor="#232F32",
                    alignment=ft.alignment.center,
                    expand=3,
                    border_radius=2,
                    content=ft.Row(
                        spacing=5,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("|", size=15, color="#8EE2E9"),
                                    ft.Text("予定2", size=15, color="#8EE2E9"),
                                ]
                            ),
                            ft.Text("10:00-11:00", size=font_size, color=ft.Colors.WHITE60, font_family=font),
                        ],
                        
                    )
                ),
                ft.Container(
                    # widthはrowのexpand
                    bgcolor="#232F32",
                    alignment=ft.alignment.center,
                    expand=3,
                    border_radius=2,
                    content=ft.Row(
                        spacing=5,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row([
                                ft.Text("|", size=15, color="#8EE2E9"),
                                ft.Text("予定3", size=15, color="#8EE2E9"),
                            ]),
                            ft.Text("10:00-11:00", size=font_size, color=ft.Colors.WHITE60, font_family=font),
                        ],
                        
                    )
                ),
            ],
        )
    )
    # Container 1 NextDay Calendar
    ct1_nextday_calendar = ft.Container(
        # height=ct1_height*0.8,  # ページの高さの8割
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=20,
        border_radius=0,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=2,
            controls=[
                ft.Container(
                    # widthはrowのexpand
                    bgcolor="#232F32",
                    alignment=ft.alignment.center,
                    expand=3,
                    border_radius=2,
                    content=ft.Row(
                        spacing=5,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row([
                                ft.Text("|", size=15, color="#8EE2E9"),
                                ft.Text("予定4", size=15, color="#8EE2E9"),
                            ]),
                            ft.Text("10:00-11:00", size=font_size, color=ft.Colors.WHITE60, font_family=font),
                        ],
                        
                    )
                ),
                ft.Container(
                    # widthはrowのexpand
                    bgcolor="#232F32",
                    alignment=ft.alignment.center,
                    expand=3,
                    border_radius=2,
                    content=ft.Row(
                        spacing=5,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row([
                                ft.Text("|", size=15, color="#8EE2E9"),
                                ft.Text("予定5", size=15, color="#8EE2E9"),
                            ]),
                            ft.Text("10:00-11:00", size=font_size, color=ft.Colors.WHITE60, font_family=font),
                        ],
                        
                    )
                ),
                ft.Container(
                    # widthはrowのexpand
                    bgcolor="#232F32",
                    alignment=ft.alignment.center,
                    expand=3,
                    border_radius=2,
                    content=ft.Row(
                        spacing=5,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row([
                                ft.Text("|", size=15, color="#8EE2E9"),
                                ft.Text("予定6", size=15, color="#8EE2E9"),
                            ]),
                            ft.Text("10:00-11:00", size=font_size, color=ft.Colors.WHITE60, font_family=font),
                        ],
                        
                    )
                ),
            ],
        )
    )
    ct1_bottom_empty = ft.Container(
        # height=ct1_height*0.8,  # ページの高さの8割
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=1,
        border_radius=0,
    )
    # Container 1 Bottom
    container1_bottom = ft.Container(
        # width=ct1_width,  # ページの幅の2割 # rowのexpand
        # heightはrowのexpand
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=7,
        border_radius=0,
        content=ft.Row(
            spacing=0,
            controls=[
                ct1_bottom_empty, ct1_calendar,ct1_bottom_empty, ct1_nextday_calendar, ct1_bottom_empty
            ],
        )
    )
    # Container 1
    container1 = ft.Container(
        # rowのexpand
        height=ct1_height,  # ページの高さの2割
        bgcolor="#1E1E1E",
        alignment=ft.alignment.center,
        expand=4,
        border_radius=10,
        content=ft.Column(
            spacing=0,
            controls=[container1_top, container1_bottom],
        )
    )

    # Google Calendarの予定を表示する関数
    def update_google_calendar():
        """今日と次の予定がある日のGoogle Calendarの予定を表示する関数
        Ref : https://developers.google.com/calendar/api/quickstart/python?hl=ja

        今日の日付を表示する
        今日の予定を表示する
        次の予定がある日を表示する
        次の予定を表示する
        """
        # If modifying these scopes, delete the file token.json.
        SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("calendar", "v3", credentials=creds)
            
            # Call the Calendar API
            now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None).isoformat() + "Z"
            event_max_results = 10
            events_result = (
                service.events().list(
                    calendarId="primary", timeMin=now, maxResults=event_max_results,
                    singleEvents=True, orderBy="startTime").execute()
                )
            events = events_result.get("items", [])

            if not events: # 予定が全くない場合
                print("No upcoming events found.")
                # 次の予定がある日を空欄にする
                container1.content.controls[0].content.controls[1].content.controls[1].value = f" "
                

            # 今日の日付をupdate
            today = datetime.date.today()
            container1.content.controls[0].content.controls[0].content.controls[1].value = f"{today.month}.{today.day}"
            container1.content.controls[0].content.controls[0].content.controls[3].value = today.strftime('%A')[0]
            
            # 次の予定がある日
            next_date = None

            # 今日の予定のカウントと次の予定のカウント
            today_event_count = 0
            next_date_event_count = 0

            # Prints the start and name of the next 10 events
            for i, event in enumerate(events):
                # eventの日付を取得
                event_date = datetime.datetime.fromisoformat(event['start']['dateTime']).date()
                # print(i, event['summary'], event_date)
                
                # 次の予定の日付(next_date)がNoneの場合は設定
                if event_date != today and next_date is None:
                    next_date = datetime.datetime.fromisoformat(event['start']['dateTime']).date()
                    # 次の予定がある日をnext_date.month月next_date.day日 next_date.strftime('%A')に設定
                    # print(f"次の予定がある日を{next_date.month}月{next_date.day}日({next_date.strftime('%A')[0]})に設定")
                    container1.content.controls[0].content.controls[1].content.controls[1].value \
                        = f"{next_date.month}月{next_date.day}日 {next_date.strftime('%A')}"
                # 今日の予定か次の予定かを判定
                if event_date == today or event_date == next_date:
                    start_time = datetime.datetime.fromisoformat(event['start']['dateTime']).time()
                    end_time = datetime.datetime.fromisoformat(event['end']['dateTime']).time()
                    # event['summary']の長さが9文字より大きい場合，8文字まで表示して「...」を追加
                    summary = event['summary'] if len(event['summary']) < 9 else event['summary'][:8] + "..."
                    if event_date == today:
                        # print("今日の予定があります！")
                        # print(f"summary : {summary}, time : {start_time.hour:02d}:{start_time.minute:02d}-{end_time.hour:02d}:{end_time.minute:02d}")
                        container1.content.controls[1].content.controls[1].content.controls[today_event_count].content.controls[0].controls[1].value = summary
                        container1.content.controls[1].content.controls[1].content.controls[today_event_count].content.controls[1].value \
                            = f"{start_time.hour:02d}:{start_time.minute:02d}-{end_time.hour:02d}:{end_time.minute:02d}"
                        today_event_count += 1
                    elif event_date == next_date:
                        # print(f"次の予定が{next_date.month}月{next_date.day}日({next_date.strftime('%A')[0]})あります！")
                        # print(f"summary : {summary}, time : {start_time.hour:02d}:{start_time.minute:02d}-{end_time.hour:02d}:{end_time.minute:02d}")
                        container1.content.controls[1].content.controls[3].content.controls[next_date_event_count].content.controls[0].controls[1].value = summary
                        container1.content.controls[1].content.controls[3].content.controls[next_date_event_count].content.controls[1].value \
                            = f"{start_time.hour:02d}:{start_time.minute:02d}-{end_time.hour:02d}:{end_time.minute:02d}"
                        next_date_event_count += 1

                # 次の予定の日付が変わったらループを抜ける
                elif next_date != datetime.datetime.fromisoformat(event['start']['dateTime']).date():
                    # print("break")
                    break
        except HttpError as error:
            print(f"An error occurred: {error}")
        
        # 今日の予定と次の予定がある日の空欄の処理
        if today_event_count == 0: # 今日の予定がない場合
            # 今日の予定リストを空欄，背景を透過して「予定なし」と表示
            container1.content.controls[1].content.controls[1].content.controls[0].bgcolor = ft.Colors.TRANSPARENT
            container1.content.controls[1].content.controls[1].content.controls[0].content.controls[0].controls[0].value = ""
            container1.content.controls[1].content.controls[1].content.controls[0].content.controls[0].controls[1].value = ""
            container1.content.controls[1].content.controls[1].content.controls[0].content.controls[1].value = ""
            container1.content.controls[1].content.controls[1].content.controls[1].bgcolor = ft.Colors.TRANSPARENT
            container1.content.controls[1].content.controls[1].content.controls[1].content.controls[0].controls[0].value = ""
            container1.content.controls[1].content.controls[1].content.controls[1].content.controls[0].controls[1].color = ft.Colors.WHITE
            container1.content.controls[1].content.controls[1].content.controls[1].content.controls[0].controls[1].value = "予定なし"
            container1.content.controls[1].content.controls[1].content.controls[1].content.controls[1].value = ""
            container1.content.controls[1].content.controls[1].content.controls[2].bgcolor = ft.Colors.TRANSPARENT
            container1.content.controls[1].content.controls[1].content.controls[2].content.controls[0].controls[0].value = ""
            container1.content.controls[1].content.controls[1].content.controls[2].content.controls[0].controls[1].value = ""
            container1.content.controls[1].content.controls[1].content.controls[2].content.controls[1].value = ""
        elif today_event_count < 3: # 今日の予定が3つ未満の場合
            for i in range(today_event_count, 3):
                container1.content.controls[1].content.controls[1].content.controls[i].bgcolor = ft.Colors.TRANSPARENT
                container1.content.controls[1].content.controls[1].content.controls[i].content.controls[0].controls[0].value = ""
                container1.content.controls[1].content.controls[1].content.controls[i].content.controls[0].controls[1].value = ""
                container1.content.controls[1].content.controls[1].content.controls[i].content.controls[1].value = ""
        
        if next_date_event_count == 0: # 今日よりも先の予定がない場合 (滅多にない)
            # 次の予定リストを空欄，背景を透過して「予定なし」と表示
            container1.content.controls[1].content.controls[3].content.controls[0].bgcolor = ft.Colors.TRANSPARENT
            container1.content.controls[1].content.controls[3].content.controls[0].content.controls[0].controls[0].value = ""
            container1.content.controls[1].content.controls[3].content.controls[0].content.controls[0].controls[1].value = ""
            container1.content.controls[1].content.controls[3].content.controls[0].content.controls[1].value = ""
            container1.content.controls[1].content.controls[3].content.controls[1].bgcolor = ft.Colors.TRANSPARENT
            container1.content.controls[1].content.controls[3].content.controls[1].content.controls[0].controls[0].value = ""
            container1.content.controls[1].content.controls[3].content.controls[1].content.controls[0].controls[1].color = ft.Colors.WHITE
            container1.content.controls[1].content.controls[3].content.controls[1].content.controls[0].controls[1].value = "予定なし"
            container1.content.controls[1].content.controls[3].content.controls[1].content.controls[1].value = ""
            container1.content.controls[1].content.controls[3].content.controls[2].bgcolor = ft.Colors.TRANSPARENT
            container1.content.controls[1].content.controls[3].content.controls[2].content.controls[0].controls[0].value = ""
            container1.content.controls[1].content.controls[3].content.controls[2].content.controls[0].controls[1].value = ""
            container1.content.controls[1].content.controls[3].content.controls[2].content.controls[1].value = ""
        elif next_date_event_count < 3: # 今日よりも先の予定が3つ未満の場合
            for i in range(next_date_event_count, 3):
                container1.content.controls[1].content.controls[3].content.controls[i].bgcolor = ft.Colors.TRANSPARENT
                container1.content.controls[1].content.controls[3].content.controls[i].content.controls[0].controls[0].value = ""
                container1.content.controls[1].content.controls[3].content.controls[i].content.controls[0].controls[1].value = ""
                container1.content.controls[1].content.controls[3].content.controls[i].content.controls[1].value = ""
        
        container1.update()

    # ============================================================
    # Container 2 Location
    ct2_location = ft.Container(
        # heightはrowのexpand
        width = ct2_width,
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center_left,
        expand=3,
        border_radius=0,
        content=ft.Text(" TOKYO", size=25, color=ft.Colors.WHITE),
    )
    # Container 2 Empty
    ct2_bottom_empty = ft.Container(
        height=ct2_height*0.7,
        # widthはrowのexpand
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=1,
        border_radius=0,
    )
    ct2_bottom_weather = ft.Container(
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        expand=30,
        border_radius=5,
        content=ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                # Weather Icon
                ft.Image(src="./imgs/100.png", width=70, height=70),
                # max temperature
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("最高気温", size=12, color=ft.Colors.WHITE),
                        ft.Text(" °C", size=23, color=ft.Colors.RED), 
                    ],
                ),
                # min temperature
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("最低気温", size=12, color=ft.Colors.WHITE),
                        ft.Text(" °C", size=23, color=ft.Colors.BLUE),
                    ],
                ),
                # precipitation
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("降水確率", size=12, color=ft.Colors.WHITE),
                        ft.Text(" %", size=23, color=ft.Colors.WHITE),
                    ],
                ),
        ])
    )
    ct2_bottom_weather2 = ft.Container(
        bgcolor=ft.Colors.TRANSPARENT, #bgcolor="#232F32",
        alignment=ft.alignment.center,
        expand=30,
        border_radius=5,
        content=ft.Text("", size=10, color=ft.Colors.WHITE),
    )
    # Container 2 Weather
    ct2_weather = ft.Container(
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center_left,
        expand=7,
        border_radius=0,
        content=ft.Row(
            spacing=0,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ct2_bottom_empty,
                    ct2_bottom_weather,
                    ct2_bottom_empty,
                    ct2_bottom_weather2,
                    ct2_bottom_empty,
                ]
        )
    )
    # Container 2
    container2 = ft.Container(
        # rowのexpand
        height=ct2_height,  # ページの高さの2割
        bgcolor="#1E1E1E", 
        alignment=ft.alignment.center,
        expand=6,
        border_radius=10,
        content=ft.Column(
            spacing=0,
            controls=[
                ct2_location, ct2_weather
            ]
        ),
    )

    # 天気情報を更新する関数
    def update_weather():
        """気象庁から東京都の天気情報を更新する関数
        
        天気アイコンを更新する
        最高温度と最低温度を更新する
        降水確率を更新する
        天気概況を更新する
        """
        url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json'
        filename = 'forecast_130000.json'
        url2 = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json"
        filename2 = "overview_forecast_130000.json"

        # Download
        req.urlretrieve(url, filename)
        req.urlretrieve(url2, filename2)

        # Load json file
        json_open = open("./forecast_130000.json", "r")
        json_load = json.load(json_open)
        json_open2 = open("./overview_forecast_130000.json", "r")
        json_load2 = json.load(json_open2)

        # Get temp and precip from json file
        temp = json_load[1]["tempAverage"]["areas"][0]
        precip = json_load[0]['timeSeries'][1]['areas'][0]['pops']
        text = json_load2['text'].replace("\u3000", "").replace("\n", "")
        text_split = text[:204].rfind("。")
        text = text[:text_split+1] + "..."
        
        # Get weather from json file
        weather_code = json_load[0]["timeSeries"][0]["areas"][0]['weatherCodes'][0]
        weather_icon = ft.Image("./imgs/" + weather_code + ".png", width=70, height=70)
        # update weather icon
        container2.content.controls[1].content.controls[1].content.controls[0] = weather_icon
        # update max temperature and min temperature
        container2.content.controls[1].content.controls[1].content.controls[1].controls[1].value = f"{temp['max']}°C"
        container2.content.controls[1].content.controls[1].content.controls[2].controls[1].value = f"{temp['min']}°C"
        # update precipitation
        container2.content.controls[1].content.controls[1].content.controls[3].controls[1].value = f"{precip[0]}%"
        # update weather description
        container2.content.controls[1].content.controls[3].content.value = text
        
        container2.update()
    
    # ============================================================
    # Container 3 Top
    ct3_calendar_top = ft.Container(
        # heightはrowのexpand
        bgcolor=ft.Colors.TRANSPARENT,
        expand=3,
        alignment=ft.alignment.center,
        content=ft.Text(" ", size=25, color=ft.Colors.WHITE,),
    )
    # Container 3 Empty
    ct3_calendar_empty = ft.Container(
        # heightはrowのexpand
        bgcolor=ft.Colors.TRANSPARENT,
        expand=1,
        alignment=ft.alignment.center,
        content=ft.Text(" ", size=25, color=ft.Colors.WHITE,),
    )
    # 曜日
    ct3_calendar_header = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        controls=[
            ft.Container(
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.center,
                expand=1,
                border_radius=5,
                content=ft.Text("月", size=20, color=ft.Colors.WHITE),
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.center,
                expand=1,
                border_radius=5,
                content=ft.Text("火", size=20, color=ft.Colors.WHITE),
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.center,
                expand=1,
                border_radius=5,
                content=ft.Text("水", size=20, color=ft.Colors.WHITE),
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.center,
                expand=1,
                border_radius=5,
                content=ft.Text("木", size=20, color=ft.Colors.WHITE),
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.center,
                expand=1,
                border_radius=5,
                content=ft.Text("金", size=20, color=ft.Colors.WHITE),
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.center,
                expand=1,
                border_radius=5,
                content=ft.Text("土", size=20, color=ft.Colors.WHITE),
            ),
            ft.Container(
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.center,
                expand=1,
                border_radius=5,
                content=ft.Text("日", size=20, color=ft.Colors.WHITE),
            ),
        ]
    )
    # 日付 7x6
    ct3_calendar_days_0 = ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[])
    ct3_calendar_days_1 = ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[])
    ct3_calendar_days_2 = ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[])
    ct3_calendar_days_3 = ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[])
    ct3_calendar_days_4 = ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[])
    ct3_calendar_days_5 = ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[])
    
    for i in range(42):
        if 0 <= i < 7:
            ct3_calendar_days_0.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT, alignment=ft.alignment.center,
                    expand=1, border_radius=5,
                    content=ft.Text(f"{i}", size=20, color=ft.Colors.WHITE),
                )
            )
        elif 7 <= i < 14:
            ct3_calendar_days_1.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT, alignment=ft.alignment.center,
                    expand=1, border_radius=5,
                    content=ft.Text(f"{i}", size=20, color=ft.Colors.WHITE),
                )
            )
        elif 14 <= i < 21:
            ct3_calendar_days_2.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT, alignment=ft.alignment.center,
                    expand=1, border_radius=5,
                    content=ft.Text(f"{i}", size=20, color=ft.Colors.WHITE),
                )
            )
        elif 21 <= i < 28:
            ct3_calendar_days_3.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT, alignment=ft.alignment.center,
                    expand=1, border_radius=5,
                    content=ft.Text(f"{i}", size=20, color=ft.Colors.WHITE),
                )
            )
        elif 28 <= i < 35:
            ct3_calendar_days_4.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT, alignment=ft.alignment.center,
                    expand=1, border_radius=5,
                    content=ft.Text(f"{i}", size=20, color=ft.Colors.WHITE),
                )
            )
        elif 35 <= i < 42:
            ct3_calendar_days_5.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT, alignment=ft.alignment.center,
                    expand=1, border_radius=5,
                    content=ft.Text(f"{i}", size=20, color=ft.Colors.WHITE),
                )
            )
    
    # 日付
    ct3_calendar_mid = ft.Container(
        height= ct3_height,
        # widthはrowのexpand
        bgcolor=ft.Colors.TRANSPARENT,
        expand=18,
        alignment=ft.alignment.center,
        # 縦5行、横7列のカレンダー
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ct3_calendar_header,
                ct3_calendar_days_0,
                ct3_calendar_days_1,
                ct3_calendar_days_2,
                ct3_calendar_days_3,
                ct3_calendar_days_4,
                ct3_calendar_days_5,
            ]
        )
    )
    container3 = ft.Container(
        # widthはrowのexpand
        height=ct3_height,  # ページの高さの8割
        bgcolor="#1E1E1E",
        alignment=ft.alignment.center,
        expand=4,
        border_radius=10,
        content=ft.Column(
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ct3_calendar_empty,# [0]
                ct3_calendar_top, # [1]
                ct3_calendar_mid, # [2]
                ct3_calendar_empty, # [3]
                ct3_calendar_empty, # [4]
            ],
        ),
    )

    # カレンダーを更新する関数
    def update_calendar():
        """カレンダー上の情報を更新する関数

        カレンダー上部の年月を更新する
        今日の日付だけ背景色を変更する
        """
        # 現在時刻を取得
        now = datetime.datetime.now()
        # 今日の日付を更新
        ct3_calendar_top.content.value = f"{now.year}年 {now.month}月"
        calendar_values = calendar.month(now.year, now.month)
        calendar_list = calendar_values.split('\n')
        days_list = []
        for row in calendar_list[2:8]:
            days = row.split()
            days_list.append(days)
        
        for i, days in enumerate(days_list):
            result_list = []
            if i == 0: result_list += [" "] * (7 - len(days))
            for day in days:
                result_list.append(day)
            if i != 0 and len(days) < 7: result_list += [" "] * (7 - len(days))
            # 値を代入
            for j, day in enumerate(result_list):
                container3.content.controls[2].content.controls[i+1].controls[j].content.value = day
                if day == " ":
                    container3.content.controls[2].content.controls[i+1].controls[j].bgcolor = ft.Colors.TRANSPARENT
                if day == str(now.day):
                    container3.content.controls[2].content.controls[i+1].controls[j].content.color = "#8EE2E9"
                    container3.content.controls[2].content.controls[i+1].controls[j].bgcolor = "#232F32"
        container3.update()

    # ============================================================
    # ct4 analog clock
    clock_bg = cv.Canvas(width=400, height=400)
    clock = cv.Canvas(width=400, height=400)
    stroke_paint = ft.Paint(stroke_width=5, style=ft.PaintingStyle.STROKE, color=ft.Colors.WHITE)# "#4CE5FF")
    circle_paint = ft.Paint(stroke_width=5, style=ft.PaintingStyle.STROKE, color=ft.Colors.WHITE)
    hour_paint = ft.Paint(stroke_width=5, style=ft.PaintingStyle.STROKE, color=ft.Colors.WHITE)#"#4CE5FF")
    minute_paint = ft.Paint(stroke_width=6, style=ft.PaintingStyle.STROKE, color=ft.Colors.WHITE)#"#4CE5FF")
    second_paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE, color="#9A1816")
    # 時計の外枠を描画
    clock_bg.shapes.append(cv.Circle(200, 190, 180, stroke_paint))
    # 中心に円を描画
    clock_bg.shapes.append(cv.Circle(200, 190, 5, circle_paint))
    # 数字を追加
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = 200 + 160 * math.cos(angle)
        y = 190 + 160 * math.sin(angle)
        clock_bg.shapes.append(
            cv.Text(x, y, str(i), alignment=ft.alignment.center, 
                    style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20))
        )
    
    # 時計の盤と時計の針を重ねる
    clock_stack = ft.Stack(
        controls=[
            clock_bg,
            clock
        ]
    )

    # Container 4
    container4 = ft.Container(
        # widthはrowのexpand
        height=ct4_height,  # ページの高さの8割
        bgcolor="#1E1E1E",
        alignment=ft.alignment.center,
        expand=6,
        border_radius=10,
        content=clock_stack,
    )

    # 時計の針を更新する関数
    def update_clock():
        """時計盤の針のみを更新する関数

        時針の長さ : 120
        分針の長さ : 150
        秒針の長さ : 150
        """
        # 現在時刻を取得
        now = datetime.datetime.now()
        # 時計の針をリセット
        clock.clean()
    
        # 時針を描画
        hour_angle = (now.hour % 12 + now.minute / 60) * 30
        hour_x = 200 + 120 * math.cos(math.radians(hour_angle - 90))
        hour_y = 190 + 120 * math.sin(math.radians(hour_angle - 90))
        clock.shapes.append(cv.Line(200, 190, hour_x, hour_y, hour_paint))
        # 分針を描画
        minute_angle = now.minute * 6
        minute_x = 200 + 150 * math.cos(math.radians(minute_angle - 90))
        minute_y = 190 + 150 * math.sin(math.radians(minute_angle - 90))
        clock.shapes.append(cv.Line(200, 190, minute_x, minute_y, minute_paint))
        # 秒針を描画
        second_angle = now.second * 6
        second_x = 200 + 150 * math.cos(math.radians(second_angle - 90))
        second_y = 190 + 150 * math.sin(math.radians(second_angle - 90))
        clock.shapes.append(cv.Line(200, 190, second_x, second_y, second_paint))
        
        # 更新
        container4.update()
    
    # ============================================================
    # 更新するタイマーの設定
    # google calendarの予定(container1)を更新する設定
    google_calendar_timer = Timer(interval_s=3600, callback=update_google_calendar)
    # 天気情報(container2)を更新する設定
    weather_timer = Timer(interval_s=3600, callback=update_weather)
    # カレンダー(container3)を更新する設定
    calendar_timer = Timer(interval_s=3600, callback=update_calendar)
    # アナログ時計(container4)を更新する設定
    clock_timer = Timer(interval_s=1, callback=update_clock)

    # ============================================================
    # main content
    row = ft.Row(
        controls=[container1, container2],
    )
    row2 = ft.Row(
        controls=[container3, container4],
    )

    main_content = ft.Column(
        controls=[row, row2],
    )

    page.add(
        main_content, 
        google_calendar_timer,
        weather_timer,
        calendar_timer, 
        clock_timer
    )
    page.update()

ft.app(target=main)
