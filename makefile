all: *.cpp
	g++ -std=c++11 -o main *.cpp && ./main
