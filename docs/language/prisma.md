# Prisma 
# Data Mapper 
传统ORM中，对象内部包含数据库操作，DM中，schema中只有数据结构定义，没有操作，数据库操作在其他代码中；
## Cmds
```shell 
npx prisma db push 
# directly pushes schema changes to the db without creating migration files
npx prisma migrate dev/deploy 
# creates and applies versioned SQL migration files to evolve the schema incrementally.
# generates SQL files in prisma/migrations for each change
npx prisma generate
# just generate Prisma Client from schema.prisma 
```

