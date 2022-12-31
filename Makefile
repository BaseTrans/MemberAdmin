all: pack

pack:
	pipreqs ./src --force


db-create:
	set PGPASSWORD=23322335&&psql -h localhost -U postgres -c "create database \"TransBase\";"

db-migrate:
	echo database migration