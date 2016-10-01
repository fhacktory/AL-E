TARGET		= libdxl.a
OBJS		= dxl_hal.o dynamixel.o
SRCS		= $(OBJS:.o=.c)
INCLUDEDIRS	+=
LIBDIRS		+= 
CFLAGS		= $(INCLUDEDIRS) -W -Wall -O2

CC			= gcc
AR			= ar

$(TARGET): $(OBJS)
	$(AR) rs $@ $^
	mkdir -p ../bin
	mv $(TARGET) ../bin
	
.c.o:
	$(CC) -c $< $(CFLAGS)
	
clean:
	rm -f $(OBJS) $(TARGET)
	@echo "file deleted."

dep:
	gccmakedep $(SRCS)

