PYTHON = python3

SCRIPT = a_maze_ing.py config.txt

# Run main script
run:
	@${PYTHON} ${SCRIPT}

# Install dependencies
install:
	${PYTHON} -m pip install --upgrade pip --user
	${PYTHON} -m pip install --user flake8 mypy 
	${PYTHON} -m pip install readchar


# Debug mode with pdb
debug:
	${PYTHON} -m pdb ${SCRIPT}

# Clean caches
clean:
	@rm -rf __pycache__ .mypy_cache .pytest_cache  mazegen/__pycache__  mazegen/.mypy_cache mazegen/.pytest_cache
	


# Lint (standard)
lint:
	@${PYTHON} -m flake8 ${PWD}
	@${PYTHON} -m mypy ${PWD} --warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

# Lint strict - optional
lint-strict:
	${PYTHON} -m flake8 ${PWD}
	${PYTHON} -m mypy ${PWD} --strict