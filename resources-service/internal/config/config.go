package config

import (
	"fmt"
	"github.com/kelseyhightower/envconfig"
	"gopkg.in/yaml.v2"
	"os"
)

type (
	AppConfig struct {
		Database Database `json:"database" yaml:"database"`
	}

	Database struct {
		Host     string `json:"host" yaml:"host" envconfig:"DB_HOST"`
		Port     int    `json:"port" yaml:"port" envconfig:"DB_PORT"`
		User     string `json:"user" yaml:"user" envconfig:"DB_USER"`
		Password string `json:"password" yaml:"password" envconfig:"DB_PASS"`
		Options  string `json:"options" yaml:"options" envconfig:"DB_OPTIONS"`
	}
)

func LoadConfigFromYamlFile(configPath string, cfg *AppConfig) error {
	f, err := os.OpenFile(configPath, os.O_RDONLY|os.O_SYNC, 0)
	if err != nil {
		return fmt.Errorf("config file can not be opened: %s", err.Error())
	}
	defer func(f *os.File) {
		_ = f.Close()
	}(f)

	err = yaml.NewDecoder(f).Decode(&cfg)
	if err != nil {
		return fmt.Errorf("config file parsing error: %s", err.Error())
	}
	return nil
}

func LoadConfigFromEnv(cfg *AppConfig) error {
	err := envconfig.Process("", cfg)
	if err != nil {
		return fmt.Errorf("cannot read config values from enviroment: %s", err.Error())
	}
	return nil
}
