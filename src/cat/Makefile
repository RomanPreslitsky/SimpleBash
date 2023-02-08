CFLAGS=-Wall -Werror -Wextra -std=c11
CSFLAG=-fsanitize=address -g
all: s21_cat

s21_cat: clean
	gcc  $(CFLAGS) s21_cat.c -o s21_cat

clean:
	rm -rf s21_cat

sanitize: clean
	gcc $(CFLAGS) $(CSFLAG) s21_cat.c -o s21_cat