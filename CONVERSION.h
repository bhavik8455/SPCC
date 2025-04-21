#define BIN_TO_DEC(input) strtol(input,NULL,2) 
#define BIN_TO_HEX(input) strtol(input,NULL,2)

#define DEC_TO_BIN(input) ({ \
    int index = 0; \
    int temp[64]; \
    int num = input; \
    if (num == 0) { \
        printf("0"); \
    } else { \
        while (num > 0) { \
            temp[index++] = num % 2; \
            num = num / 2; \
        } \
        for( i = index - 1; i >= 0; i--) { \
            printf("%d", temp[i]); \
        } \
    } \
})


#define HEX_TO_BIN(input)({\
long num = strtol(input,NULL,16);\
int index = 0; \
    int temp[64]; \
    if (num == 0) { \
        printf("0"); \
    } else { \
        while (num > 0) { \
            temp[index++] = num % 2; \
            num /= 2; \
        } \
        for ( i = index - 1; i >= 0; i--) { \
            printf("%d", temp[i]); \
        } \
    } \
})




