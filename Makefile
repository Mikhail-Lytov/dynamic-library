build:
	@gcc -fPIC -c pushkin.c -o pushkin.o
	@gcc -shared -o pushkin.so pushkin.o
run: 
	@python3 main_1.py
clean:
	@rm -rf  *.o *.so