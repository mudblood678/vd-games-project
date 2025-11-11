install:
	uv sync

VD-games:
	uv run vd-games

build:
	uv build

package-install:
	uv tool install dist/*.whl
