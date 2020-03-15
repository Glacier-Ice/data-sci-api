package main

import (
	"encoding/json"
	"fmt"
	"log"
	"time"

	"github.com/asmcos/requests"
)

func init() {
	err := loadConfig()
	if err != nil {
		log.Fatalf("Fail to load config file: %s\n", err.Error())
	}
	err = loadJson()
	if err != nil {
		log.Fatalf("Fail to load json file: %s\n", err.Error())
	}
}

func doWork() {
	// url := "https://lab.isaaclin.cn/nCoV/api/area?latest=1"
	url := "https://lab.isaaclin.cn/nCoV/api/area?latest=0"
	resp, err := requests.Get(url)
	if err != nil {
		panic(err)
	}

	var results AreaResult
	err = json.Unmarshal([]byte(resp.Text()), &results)
	if err != nil {
		panic(err)
	}
	if results.Success {
		fmt.Println("获取数据成功！")
	} else {
		fmt.Println("获取数据失败！")
	}

	// 数据库操作
	engine := PostgreEngine{}
	err = engine.Start()
	if err != nil {
		panic(err)
	}
	defer engine.Close()

	// 存储数据
	for _, provinceInfo := range results.Results {
		provinceName := provinceInfo.ProvinceName
		confirmedProvince := provinceInfo.ConfirmedCount
		curedProvince := provinceInfo.CuredCount
		deadProvince := provinceInfo.DeadCount
		suspectedProvince := provinceInfo.SuspectedCount
		curday := time.Unix(provinceInfo.UpdateTime/1e3, 0).Format("2006-01-02")
		if provinceCode, ok := CodeMap[provinceName]; ok {
			err := engine.InsertProvince(curday, provinceName, provinceCode, confirmedProvince, curedProvince, deadProvince, suspectedProvince)
			if err != nil {
				fmt.Println("插入省数据失败：", err.Error())
				break
			}
		} else {
			log.Printf("省级编码为空：%s\n", provinceName)
		}
		for _, cityInfo := range provinceInfo.Cities {
			cityName := cityInfo.CityName
			confirmedCtiy := cityInfo.ConfirmedCount
			curedCtiy := cityInfo.CuredCount
			deadCtiy := cityInfo.DeadCount
			suspectedCtiy := cityInfo.SuspectedCount
			// cityCode := cityInfo.LocationId
			if cityCode, ok := CodeMap[cityName]; ok {
				err := engine.InsertCity(curday, cityName, cityCode, confirmedCtiy, curedCtiy, deadCtiy, suspectedCtiy)
				if err != nil {
					fmt.Println("插入城市数据失败：", err.Error())
					break
				}
			} else {
				log.Printf("城市编码为空：%s\n", cityName)
			}

		}
	}
}

func main() {
	doWork()
	var delay, repeat, hour, minute int
	repeat = 24*60*60

	hour = TRIGGER_HOUR
	minute = TRIGGER_MINUTE
	now := time.Now()
	fmt.Println(now.Hour())
	fmt.Println(now.Minute())
	delay = (hour-now.Hour())*3600 + (minute-now.Minute())*60
	if delay < 0 {
		delay += 24 * 3600
	}
	fmt.Println("delay =", delay, "repeat =", repeat)

	// 定时任务
	ticker := time.NewTicker(time.Duration(delay) * time.Second)
	defer ticker.Stop()
	isStart := false
	for {
		select {
		case <- ticker.C:
			// fmt.Println("start")
			doWork()
			isStart = true
			ticker.Stop()
		case <- time.After(time.Duration(repeat) * time.Second):
			if isStart {
				// fmt.Println("working")
				doWork()
			}
		}
	}
}
