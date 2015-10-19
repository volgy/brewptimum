TARGET=w1-00A0.dtbo

all: /lib/firmware/$(TARGET) 

/lib/firmware/$(TARGET) : $(TARGET)
	sudo cp $(TARGET) /lib/firmware/$(TARGET)

$(TARGET) : w1.dts
	dtc -O dtb -o $(TARGET) -b 0 -@ w1.dts

clean:
	rm $(TARGET)

