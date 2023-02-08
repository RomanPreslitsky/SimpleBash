#include <ctype.h>
#include <getopt.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define SHORT_FLAGS "+EbenstvT"

typedef struct {
  int bflag;
  int eflag;
  int nflag;
  int sflag;
  int tflag;
  int vflag;
} flags_struct;

void mnote(int sym);
int get_flags(flags_struct *flags, int *err, int argc, char *argv[]);

int main(int argc, char *argv[]) {
  flags_struct flags = {0, 0, 0, 0, 0, 0};
  int err = 0;

  int current_file_number = get_flags(&flags, &err, argc, argv);

  int iteration = 0;
  while (current_file_number <= argc && err == 0) {
    FILE *fp = NULL;
    if (iteration == 0 && current_file_number == argc) {
      fp = stdin;
    }
    if (argv[current_file_number] != NULL) {
      if (strcmp(argv[current_file_number], "-") == 0) {
        fp = stdin;
      } else if (current_file_number != argc) {
        fp = fopen(argv[current_file_number], "r");
        if (fp == NULL) {
          fprintf(stderr, "s21_cat: %s: No such file or directory\n",
                  argv[current_file_number]);
        }
      }
    }
    if (fp != NULL) {
      char cur = '\0';
      int previous_blank = 0;
      int counter = 1;
      for (char prev = '\n'; (cur = getc(fp)) != EOF; prev = cur) {
        if (prev == '\n') {
          if (flags.sflag) {
            if (cur == '\n') {
              if (previous_blank == 1) {
                continue;
              }
              previous_blank = 1;
            } else {
              previous_blank = 0;
            }
          }
          if (flags.nflag == 1) {
            if (flags.bflag == 1 && cur == '\n') {
            } else {
              printf("%6d\t", counter);
              counter++;
            }
          }
        }
        if (!isprint(cur)) {
          if (cur == '\n') {
            if (flags.eflag == 1) {
              printf("$");
            }
            putchar(cur);
          } else if (cur == '\t') {
            if (flags.tflag == 1) {
              printf("^I");
            } else {
              putchar(cur);
            }
          } else if (flags.vflag == 1 && cur != 10 && cur != 9) {
            mnote(cur);
          } else {
            putchar(cur);
          }
        } else {
          putchar(cur);
        }
      }
      fclose(fp);
    }

    current_file_number++;
    iteration++;
  }
  return 0;
}

void mnote(int sym) {
  if ((sym < 0 || sym > 127) && !isprint(sym)) {
    printf("M-");
    sym = sym & 0x7F;
  }
  if (iscntrl(sym)) {
    if (sym == 127) {
      printf("^?");
    } else if (sym != 10 && sym != 9) {
      printf("^%c", sym + 64);
    }
  }
}

int get_flags(flags_struct *flags, int *err, int argc, char *argv[]) {
  char opt = '\0';
  const struct option long_flags[] = {
      {"number-nonblank", no_argument, &flags->bflag, 1},
      {"number", no_argument, &flags->nflag, 1},
      {"squeeze-blank", no_argument, &flags->sflag, 1},
      {NULL, 0, NULL, 0}};

  while ((opt = getopt_long(argc, argv, SHORT_FLAGS, long_flags, NULL)) != -1) {
    switch (opt) {
      case 'E':
        flags->eflag = 1;
        break;
      case 'b':
        flags->bflag = 1;
        flags->nflag = 1;
        break;
      case 'e':
        flags->eflag = 1;
        flags->vflag = 1;
        break;
      case 'n':
        flags->nflag = 1;
        break;
      case 's':
        flags->sflag = 1;
        break;
      case 't':
        flags->tflag = 1;
        flags->vflag = 1;
        break;
      case 'T':
        flags->tflag = 1;
        break;
      case 'v':
        flags->vflag = 1;
        break;
      case '?':
        fprintf(stderr, "usage: ./s21_cat [-EbenstvT] [file ...]\n");
        *err = -1;
        break;
    }
  }
  return optind;
}
