# Placeholder Makefile

all: pre-processing/initilize.c learned\ indexing/main.py
	@echo "Compiling Pre-processor..."
	@gcc pre-processing/initilize.c -o pre-processing/init.out
	@echo "Running..."
	@python learned\ indexing/main.py
	@echo "Completed, Cleaning"
	@rm pre-processing/*.out # TODO: Bucket
	@echo "Done"

clean:
	@echo "Cleaning..."
	@rm pre-processing/*.out # TODO: Bucket
	@echo "Done"
