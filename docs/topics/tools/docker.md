# Docker

# Dockerfile
> [Ref](https://docs.docker.com/reference/dockerfile/)
- `WORKDIR`
Create and cd target dir
# docker-compose.yml
- `ADD create.sql /docker-entrypoint-initdb.d`
`.sh` `.sql` file would be executed under this dir at the moment the container start.

- [`build`](https://docs.docker.com/reference/compose-file/build/)
The path is used as the Docker context to execute a Docker build, looking for a canonical `Dockerfile` at the root of the dir.

- `expose`
Expose the port to other services within the Docker network without publishing to the host machine.

# `docker-compose`
- `--build`

Force build(rebuild)
# Error
###
