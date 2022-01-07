drop table if exists items;
    create table items (
        id integer primary key autoincrement,
        name text not null,
        amount integer not null
);