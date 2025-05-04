# [aerich](https://tortoise.github.io/migration.html#initialization)
# Procedure: how the steps to use aerich
1. config models in `TORTOISE_ORM`
used by tortoise init(register `aerich` a table managed by ORM) aerich init(tells aerich to create `aerich` table), `aerich migrate` use it the connect db and compare schema.

2. `aerich init ` init aerich and create migration folder


# How `aerich` works
## Aerich use a dedicated table called `aerich` to maintain history of applied migrations
`aerich.models` module defines the schema of this table.
## aerich commands (`aerich init/migrate`) depend on the `aerich` table to compare current state of your db schema and generate or apply migrations.

so `aerich.models` should be in the configuration to create at init.
## what `aerich.models` is?
`from aerich import models` it's module defined by `aerich`
