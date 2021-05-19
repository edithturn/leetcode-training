#include <stdio.h>
#include <fcntl.h>

int	read4(char[] buf4)
{

	return 0;
}

int main(int argc, char **argv)
{
	int r, fd;
	r = 0;
	char *line;
	char[] buf4 = 2400;

	if (argc == 2)
	{
		fd = open("file", O_RDONLY);
		while ((r = read4(buf4)) > 0)
		{
			
		}
	}
	return (0);
}
