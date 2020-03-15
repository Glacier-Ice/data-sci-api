package main

import (
	"encoding/json"
	"io/ioutil"

	"gopkg.in/ini.v1"
)

var (
	DB_USER, DB_PASSWD, DB_NAME string
	TRIGGER_HOUR, TRIGGER_MINUTE int
	globalCfg *ini.File
	CodeMap map[string]int
)

func loadConfig() error {
	var err error
	globalCfg, err = ini.Load("config.ini")
	if err != nil {
		return err
	}
	DB_USER = globalCfg.Section("mysql").Key("DB_USER").String()
	DB_PASSWD = globalCfg.Section("mysql").Key("DB_PASSWD").String()
	DB_NAME = globalCfg.Section("mysql").Key("DB_NAME").String()
	TRIGGER_HOUR, err = globalCfg.Section("trigger").Key("TRIGGER_HOUR").Int()
	if err != nil {
		return err
	}
	TRIGGER_MINUTE, err = globalCfg.Section("trigger").Key("TRIGGER_MINUTE").Int()
	if err != nil {
		return err
	}
	return nil
}

func loadJson() error {
	CodeMap = make(map[string]int)
	data, err := ioutil.ReadFile("code.json")
	if err != nil {
		return err
	}
	err = json.Unmarshal(data, &CodeMap)
	if err != nil {
		return err
	}
	return nil
}