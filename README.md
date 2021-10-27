# danger-alertness-test
## 怎麼跑起來?
1. 執行 server.py
2. 到 http://localhost:8000 即可進入測驗頁面
3. 測驗後資料將儲存在 result.csv
4. 執行 data-process.py 可以把受測者點擊的位置用紅色圈圈框住

## 資料格式 (result.csv)
### id, video1, video2, video3, video4
* id: 受測編號的欄位
* video1: 第1部影片的資料
* video2: 第2部影片的資料
依此類推

### 資料型態
* id: string
* video1 ~ video4: list (array) of string "x y t" or 'X' for no click events

### data form "x y t"
* each "x y z" string represents a click event
* x: the x coordinate of the click
    * type: float
    * value: 0 ~ 1
    * this is the value relative to the video width (i.e. the click position / the total width)
* y: the y coordinate of the click
    * type: float
    * value: 0 ~ 1
    * this is the value relative to the video height (i.e. the click position / the total height)
* t: the timestamp of the click
    * type: float
    * the time that the click event occurs in the video