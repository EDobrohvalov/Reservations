# Сервис бронирования

Учебный проект, целью которого является использование Golang в качестве основного языка разработки микросервисного приложения.

Какие аспекты распределенных придложений хотелось бы реализовать и интегрировать:

* Service discovery
* Logging
* Tracing
* Cron jobs
* Persistence
* Kafka consumers
* Kafra producers
* Metrics (Prometheus)
* Observability (Grafana)

## Задача

Создать сервис позволяющий бронировать доступный ресурс (рабочее место, переговорку, столик в кафе и т.п.) на произвольный промежуток времени. А так же предоставлять возможность создавать\удалять бронируемые ресурсы

### Пользовательские сценарии (Пользователь может)

* Создавать ресурс
* Удалить ресурс
* Заблокировать\разблокировать ресурс для бронирования
* Забронировать ресурс на любой промежуток времени
* В любой момент снять бронь с ресурса

### Условия и ограничения

* Пересечения по времени бронирования недопустимы на одном ресурсе
* Бронирование доступно только на время в будущем
* При блокировании ресурса для бронирования - бронь снимается автоматически
* По истечению времени бронирования - бронь снимается автоматически
* При удалении ресурса бронь удаляется вместе с ресурсом
  