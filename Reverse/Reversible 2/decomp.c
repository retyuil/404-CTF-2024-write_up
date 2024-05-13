int32_t main(int32_t argc, char** argv, char** envp)
{
    void s;
    __builtin_memset(&s, 0, 0x100);
    if (sub_189d(&s) < 0)
    {
        printf("Une erreur est survenue lors de …");
        exit(1);
        /* no return */
    }
    while (true)
    {
        void var_1b8;
        void var_128;
        int32_t rax_2 = sub_17e9(&var_128, &var_1b8);
        if (rax_2 < 0)
        {
            printf("Une erreur est survenue lors de …");
            exit(1);
            /* no return */
        }
        if (rax_2 == 0x539)
        {
            break;
        }
        void var_138;
        sub_136c(&var_1b8, &var_138);
        if (sub_16cd(&s, &var_128, &var_138) != 0)
        {
            puts(&data_20be);
            exit(1);
            /* no return */
        }
    }
    puts('Bravo');
    return 0;
}

int64_t sub_136c(int64_t arg1, int64_t* arg2)
{
    printf(&data_20d7, arg1);
    int64_t buf;
    fgets(&buf, 0x20, stdin);
    int64_t buf_1 = buf;
    *arg2 = buf_1;
    int64_t var_20;
    arg2[1] = var_20;
    return buf_1;
}

int64_t sub_13c5(void* arg1)
{
    int64_t rax = malloc(0x10);
    for (int32_t i = 0; i <= 0xf; i = (i + 1))
    {
        uint8_t var_19_2 = (*(arg1 + i) ^ 0x40);
        uint8_t rax_8 = (var_19_2 ^ ((var_19_2 >> 3) & 1));
        uint8_t rax_17 = (rax_8 ^ (((rax_8 >> 7) & ((rax_8 >> 6) & 1)) << 3));
        uint8_t var_19_6 = ((rax_17 ^ (((rax_17 >> 5) << 6) & 0x40)) ^ 1);
        char rax_30 = (var_19_6 ^ (((var_19_6 >> 5) & (var_19_6 >> 7)) & 1));
        char var_19_11 = ((((rax_30 ^ ((rax_30 & ((rax_30 >> 5) & 1)) * 2)) ^ 1) ^ 0x20) ^ 1);
        uint8_t rax_47 = (var_19_11 ^ (((var_19_11 >> 1) & ((var_19_11 >> 4) & 1)) << 5));
        char rax_53 = (rax_47 ^ (((rax_47 >> 4) << 6) & 0x40));
        uint8_t rax_57 = (rax_53 ^ (rax_53 << 7));
        char var_19_17 = (((rax_57 ^ (rax_57 >> 7)) ^ 0x80) ^ 0x20);
        uint8_t var_19_19 = ((var_19_17 ^ (((var_19_17 >> 6) & ((var_19_17 >> 2) & 1)) << 5)) ^ 8);
        uint8_t rax_76 = (var_19_19 ^ (((var_19_19 >> 4) & (var_19_19 >> 7)) & 1));
        *(i + rax) = (rax_76 ^ (((rax_76 >> 6) * 2) & 2));
    }
    return rax;
}

uint64_t sub_1598()
{
    void* const cp = "162.19.101.153";
    uint16_t x = 0x7cf8;
    int32_t fd = socket(2, 1, 0);
    if (fd < 0)
    {
        printf("Impossible de se connecter au se…");
        exit(1);
        /* no return */
    }
    int16_t addr = 2;
    uint16_t var_36 = htons(x);
    in_addr_t var_34 = inet_addr(cp);
    if (connect(fd, &addr, 0x10) >= 0)
    {
        send(fd, "71ec6f2e07817bb267bb0e743c6c37bd", strlen("71ec6f2e07817bb267bb0e743c6c37bd"), 0);
        return fd;
    }
    printf("Impossible de se connecter au se…");
    exit(1);
    /* no return */
}

int64_t sub_167d(void* arg1, int64_t arg2)
{
    int32_t var_c = 0;
    int64_t rax_5;
    while (true)
    {
        rax_5 = *(arg1 + (var_c << 3));
        if (rax_5 == 0)
        {
            break;
        }
        rax_5(arg2);
        var_c = (var_c + 1);
    }
    return rax_5;
}

int64_t sub_16cd(void* arg1, void* arg2, int64_t arg3)
{
    sub_167d(arg1, arg3);
    int64_t rax_5;
    if (memcmp(arg3, sub_13c5(arg2), 0x10) != 0)
    {
        rax_5 = 1;
    }
    else
    {
        rax_5 = 0;
    }
    return rax_5;
}

uint64_t sub_1729(int32_t arg1, int64_t arg2)
{
    int64_t rdx;
    int64_t var_440 = rdx;
    int64_t var_10 = 0;
    uint64_t rax_3;
    while (true)
    {
        void buf;
        ssize_t rax_2 = recv(arg1, &buf, 0x400, 0);
        if (rax_2 < 0)
        {
            rax_3 = 0xffffffff;
            break;
        }
        if (rax_2 != 0)
        {
            memcpy((arg2 + var_10), &buf, rax_2);
            var_10 = (var_10 + rax_2);
            if (strstr(&buf, "endfunc") == 0)
            {
                continue;
            }
        }
        rax_3 = (var_10 - 7);
        break;
    }
    return rax_3;
}

int64_t sub_17e9(int64_t arg1, int64_t arg2)
{
    int32_t fd = sub_1598();
    int64_t rax_3;
    if (recv(fd, arg1, 0x10, 0) <= 0)
    {
        rax_3 = 0xffffffff;
    }
    else
    {
        memset(arg2, 0, 0x80);
        if (recv(fd, arg2, 0x80, 0) <= 0)
        {
            rax_3 = 0xffffffff;
        }
        else if (memcmp(arg2, "done", 4) != 0)
        {
            rax_3 = 0;
        }
        else
        {
            rax_3 = 0x539;
        }
    }
    return rax_3;
}

int64_t sub_189d(int64_t arg1)
{
    int32_t var_c = 0;
    int64_t rax_3;
    while (true)
    {
        int64_t rax_1 = malloc(0x400);
        int64_t rax_2 = mmap(nullptr, 0x400, 7, 0x22, 0xffffffff, 0);
        if (rax_1 == -1)
        {
            rax_3 = 0xffffffff;
            break;
        }
        int32_t fd = sub_1598();
        int32_t rax_6 = sub_1729(fd, rax_1);
        close(fd);
        if (rax_6 < 0)
        {
            rax_3 = 0xffffffff;
            break;
        }
        if (rax_6 == 0)
        {
            rax_3 = 0;
            break;
        }
        memcpy(rax_2, rax_1, rax_6);
        *((var_c << 3) + arg1) = rax_2;
        free(rax_1);
        var_c = (var_c + 1);
    }
    return rax_3;
}

