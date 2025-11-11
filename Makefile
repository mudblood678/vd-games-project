# VD Games Project - Makefile
# Practical Work #2

# Install project dependencies
install:
	uv sync

# Run the VD-games application
run:
	uv run vd-games

# Build the package
build:
	uv build

# Install package globally
package-install:
	uv tool install dist/*.whl

# Clean build files
clean:
	rm -rf dist

# Test everything
test-all: install build package-install
	echo "All tasks completed successfully!"

# Help information
help:
	@echo "=== VD GAMES PROJECT COMMANDS ==="
	@echo "make install      - Install dependencies"
	@echo "make run          - Run the application"
	@echo "make build        - Build package"
	@echo "make package-install - Install globally"
	@echo "make clean        - Clean build files"
	@echo "make test-all     - Run all tasks"
	@echo "make help         - Show this help"
