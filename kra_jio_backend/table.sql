create table public.rates_live
(
    rate_id      serial
        primary key,
    rate_type    varchar(250),
    rate_key     varchar(250),
    product_name varchar(100),
    amount       varchar(100),
    url          varchar(200),
    updated_at   timestamp,
    unit         varchar(100)
);

alter table public.rates_live
    owner to postgres;

grant select on public.rates_live to kra_jio;

