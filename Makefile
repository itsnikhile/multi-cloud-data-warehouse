install:
	pip install -r requirements.txt

test:
	pytest tests/ -v

demo:
	python main.py demo
