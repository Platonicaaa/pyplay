release: bin/rails db:migrate
web: daphne pyplayy.asgi:application  --port $PORT --bind 0.0.0.0 -v2