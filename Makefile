# Placeholder Makefile

all: learned\ indexing/main.py
	@echo "Running..."
	@python3 learned\ indexing/main.py
	@echo "Completed"
	@echo "Cleaning..." #TODO
	@echo "Done"

clean:
	@echo "Cleaning..."
	@rm bucket/out.csv
	@echo "Done"
