package app

import (
	"encoding/json"
	"fmt"
	"reservation/resource-service/internal/config"
)

func Run(conf *config.AppConfig) {
	cfg, err := json.Marshal(conf)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(cfg))
}
