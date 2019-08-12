SELECT
  pg_terminate_backend(pid)
FROM
  pg_stat_activity
WHERE
    pid <> pg_backend_pid()
  AND datname = 'sinar_harian'
;

-- postgres
DROP DATABASE IF EXISTS sinar_harian;
DROP USER IF EXISTS sinar_harian;
CREATE USER sinar_harian WITH PASSWORD 'sinar_harian';
CREATE DATABASE sinar_harian;
GRANT ALL PRIVILEGES ON DATABASE sinar_harian to sinar_harian;



