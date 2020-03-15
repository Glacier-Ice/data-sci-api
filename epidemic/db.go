package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

type PostgreEngine struct {
	db *sql.DB
}

func (e *PostgreEngine) Start() error {
	var err error
	driveSource := fmt.Sprintf("user=%s password=%s dbname=%s sslmode=disable", DB_USER, DB_PASSWD, DB_NAME)
	e.db, err = sql.Open("postgres", driveSource)
	if err != nil {
		return err
	}
	return e.CreateTable()
}

func (e *PostgreEngine) Close() error {
	err := e.db.Close()
	if err != nil {
		return err
	}
	return nil
}

func (e *PostgreEngine) CreateTable() error {
	sqlT := `CREATE TABLE IF NOT EXISTS public.area_province(
			id serial primary key, 
			curday date, 
			province_name varchar(255), 
			province_code int,
			confirmed_count bigint, 
			cured_count bigint, 
			dead_count bigint,
			suspected_count bigint
		);
		CREATE TABLE IF NOT EXISTS public.area_city(
			id serial primary key, 
			curday date, 
			city_name varchar(255), 
			city_code int,
			confirmed_count bigint, 
			cured_count bigint, 
			dead_count bigint,
			suspected_count bigint
		);
		CREATE TABLE IF NOT EXISTS public.area_relation( 
			area_type varchar(255), 
			area_name varchar(255), 
			code int
		);`
	_, err := e.db.Exec(sqlT)
	if err != nil {
		return err
	}
	return nil
}

func (e *PostgreEngine) InsertProvince(curday, provinceName string, provinceCode int, confirmedCount, curedCount, deadCount, suspectedCount int64) error {
	// insertSql := `INSERT INTO public.area_info (
	// 	curday, province, city, confirmed_count,cured_count, dead_count
	// 	) VALUES ($1, $2, $3, $4, $5, $6)`
	insertSql := `INSERT INTO public.area_province (curday, province_name, province_code, confirmed_count, cured_count, dead_count, suspected_count)
	SELECT $1, $2, $3, $4, $5, $6, $7
	WHERE NOT EXISTS(select 1 from public.area_province t where t.curday = $1 and t.province_code = $3)`
	stmt, err := e.db.Prepare(insertSql)
	if err != nil {
		return err
	}
	result, err := stmt.Exec(curday, provinceName, provinceCode, confirmedCount, curedCount, deadCount, suspectedCount)
	if err != nil {
		return err
	}
	_, err = result.RowsAffected()
	if err != nil {
		return err
	}
	// fmt.Printf("InsertProvince RowsAffected: %+v\n", affected)
	defer stmt.Close()
	return nil
}

func (e *PostgreEngine) InsertCity(curday, cityName string, cityCode int, confirmedCount, curedCount, deadCount, suspectedCount int64) error {
	insertSql := `INSERT INTO public.area_city (curday, city_name, city_code, confirmed_count, cured_count, dead_count, suspected_count)
	SELECT $1, $2, $3, $4, $5, $6, $7 
	WHERE NOT EXISTS(select 1 from public.area_city t where t.curday = $1 and t.city_code = $3)`
	stmt, err := e.db.Prepare(insertSql)
	if err != nil {
		return err
	}
	result, err := stmt.Exec(curday, cityName, cityCode, confirmedCount, curedCount, deadCount, suspectedCount)
	if err != nil {
		return err
	}
	_, err = result.RowsAffected()
	if err != nil {
		return err
	}
	// fmt.Printf("InsertCity RowsAffected: %+v\n", affected)
	defer stmt.Close()
	return nil
}