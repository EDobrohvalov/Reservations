package main

import (
	"fmt"
	"reservation/resource-service/internal/app"
	"reservation/resource-service/internal/config"
)

func main() {
	cfg := config.AppConfig{}
	err := config.LoadConfigFromYamlFile("./config/config.yml", &cfg)
	err = config.LoadConfigFromEnv(&cfg)
	if err != nil {
		_ = fmt.Errorf("config file not initialized")
	}
	app.Run(&cfg)
}
