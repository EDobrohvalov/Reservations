-- +goose Up
CREATE TABLE resource
(
    resource_id   bigint not null,
    resource_name text   not null,
    is_disabled   bool   not null,
    primary key (resource_id)
);

-- +goose Down
DROP TABLE resource;
