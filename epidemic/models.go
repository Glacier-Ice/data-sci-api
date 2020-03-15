package main

type AreaResult struct {
	Results []ProvinceInfo `json:"results"`
	Success bool `json:"success"`
}

type ProvinceInfo struct {
	Country string `json:"country"`
	ProvinceName string `json:"provinceName"`
	ProvinceShortName string `json:"provinceShortName"`
	ConfirmedCount int64 `json:"confirmedCount"`
	SuspectedCount int64 `json:"suspectedCount"`
	CuredCount int64 `json:"curedCount"`
	DeadCount int64 `json:"deadCount"`
	Cities []CityInfo `json:"cities"`
	UpdateTime int64 `json:"updateTime"` // 13位时间戳
}

type CityInfo struct {
	CityName string `json:"cityName"`
	ConfirmedCount int64 `json:"confirmedCount"`
	SuspectedCount int64 `json:"suspectedCount"`
	CuredCount int64 `json:"curedCount"`
	DeadCount int64 `json:"deadCount"`
	LocationId int `json:"locationId"`
}