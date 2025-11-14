.PHONY: lint format install build test check-syntax

install:
	uv sync

build:
	uv build

lint:
	uv run ruff check VD_games

format:
	uv run ruff format VD_games
	uv run ruff check --fix VD_games

check-syntax:
	@echo "Checking Python syntax..."
	@uv run python -m py_compile VD_games/scripts/VD_calc.py && echo "VD_calc.py: OK"
	@uv run python -m py_compile VD_games/scripts/VD_gcd.py && echo "VD_gcd.py: OK"
	@uv run python -m py_compile VD_games/scripts/VD_even.py && echo "VD_even.py: OK"
	@uv run python -m py_compile VD_games/scripts/VD_games.py && echo "VD_games.py: OK"
	@uv run python -m py_compile VD_games/games/calc.py && echo "calc.py: OK"
	@uv run python -m py_compile VD_games/games/gcd.py && echo "gcd.py: OK"
	@uv run python -m py_compile VD_games/games/even.py && echo "even.py: OK"
	@uv run python -m py_compile VD_games/engine/game_engine.py && echo "game_engine.py: OK"

test:
	uv run python -c "import VD_games; print('Package imports successfully')"

all: check-syntax build
