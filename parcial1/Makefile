CXX = g++

TARGET = main

all: $(TARGET)

$(TARGET): $(TARGET).o
	$(CXX) -o $@ $^

$(TARGET).o: $(TARGET).cpp
	$(CXX) -c $^

clean:
	rm -f $(TARGET) $(TARGET).o