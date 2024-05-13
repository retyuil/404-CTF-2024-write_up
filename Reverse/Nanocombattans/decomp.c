int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    int64_t s;
    __builtin_memset(&s, 0, 0x100);
    puts("================================…");
    puts(&data_b18);
    puts("_____                           …");
    puts(&data_938);
    puts(" |||                            …");
    puts(" |||          ~Qu'est-ce que tu …");
    puts(&data_a38);
    puts(" |||                            …");
    puts(&data_b70);
    puts(&data_d48);
    __printf_chk(1, "              >>> ");
    __isoc99_scanf("%255s", &s);
    if (strlen(&s) != 0x13)
    {
        fail();
    }
    sub_2647(&s);
    return 0;
}

void sub_2298(int64_t arg1, int64_t arg2) __noreturn
{
    if (ptrace(PTRACE_TRACEME, 0, 0, 0) == 0xffffffff)
    {
        puts(&data_a18);
        exit(0x42);
        /* no return */
    }
    arg1(arg2);
    exit(0);
    /* no return */
}

void sub_22f5(int64_t arg1) __noreturn
{
    if (ptrace(PTRACE_TRACEME, 0, 0, 0) == 0xffffffff)
    {
        puts(&data_a18);
        exit(0x42);
        /* no return */
    }
    arg1();
    exit(0);
    /* no return */
}

void fail() __noreturn
{
    puts("Crois-tu pouvoir me fumister si …");
    exit(0x69);
    /* no return */
}

int64_t sub_2367()
{
    return puts(&data_d00);
}

pid_t sub_2380(pid_t arg1, int64_t arg2, int32_t arg3)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    pid_t stat_loc_1;
    while (true)
    {
        pid_t stat_loc;
        stat_loc_1 = waitpid(arg1, &stat_loc, 0);
        if (stat_loc_1 == 0xffffffff)
        {
            break;
        }
        stat_loc_1 = stat_loc;
        if ((stat_loc_1 & 0x7f) == 0)
        {
            break;
        }
        if (stat_loc_1 == 0x7f)
        {
            if (*stat_loc_1[1] == 5)
            {
                void var_108;
                ptrace(PTRACE_GETREGS, arg1, 0, &var_108);
                stat_loc_1 = -1;
                char var_78;
                if ((var_78 & 0x40) != 0)
                {
                    int64_t var_88_1 = (arg2 + *(&data_4d40 + (*(&data_4c80 + ((arg3 + 1) << 2)) << 2)));
                    ptrace(PTRACE_SETREGS, arg1, 0, &var_108);
                    stat_loc_1 = 0;
                }
                break;
            }
        }
    }
    *(fsbase + 0x28);
    if (rax != *(fsbase + 0x28))
    {
        __stack_chk_fail();
        /* no return */
    }
    return stat_loc_1;
}

int64_t sub_2473(pid_t arg1, int64_t arg2, int32_t arg3, int64_t arg4)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    while (true)
    {
        int32_t stat_loc;
        if (waitpid(arg1, &stat_loc, 0) == 0xffffffff)
        {
            break;
        }
        int16_t stat_loc_1 = stat_loc;
        if ((stat_loc_1 & 0x7f) == 0)
        {
            break;
        }
        if ((stat_loc_1 == 0x7f && *stat_loc_1[1] == 5))
        {
            void var_118;
            ptrace(PTRACE_GETREGS, arg1, 0, &var_118);
            int64_t var_98;
            if (var_98 != (arg2 + 1))
            {
                int64_t var_98_1 = arg2;
                ptrace(PTRACE_SETREGS, arg1, 0, &var_118);
                ptrace(PTRACE_CONT, arg1, 0, 0);
                break;
            }
            int32_t rdx = *(&data_4c80 + (arg3 << 2));
            int64_t rax_9 = (*(&data_4d40 + (rdx << 2)) + 1);
            int64_t var_a8_1 = (arg4 + rax_9);
            if ((arg3 <= 5 || arg3 == 0x12))
            {
                void* var_b0_2 = (&data_4f60 + rax_9);
            }
            if ((arg3 - 6) <= 5)
            {
                void* var_b0_1 = (rax_9 + &data_4e20);
            }
            else if (arg3 > 0xb)
            {
                void* var_b0_3 = (rax_9 + &data_4d80);
            }
            int64_t var_b8_1 = (*(&data_4d10 + (rdx << 2)) - 1);
            ptrace(PTRACE_SETREGS, arg1, 0, &var_118);
            ptrace(PTRACE_CONT, arg1, 0, 0);
        }
    }
    if (rax != *(fsbase + 0x28))
    {
        __stack_chk_fail();
        /* no return */
    }
    return (rax - *(fsbase + 0x28));
}

int64_t sub_2647(int64_t arg1)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    int64_t rax_2 = mmap(nullptr, data_4d60, 7, 0x21, 0xffffffff, 0);
    memcpy(rax_2, &data_4ec0, data_4d60);
    int64_t rax_3 = mmap(nullptr, data_4cd0, 7, 0x22, 0xffffffff, 0);
    memcpy(rax_3, &data_4ce0, data_4cd0);
    pid_t pid = fork();
    if (pid < 0)
    {
        __printf_chk(1, "ERREUR : TRAVAIL TERMI");
        exit(1);
        /* no return */
    }
    if (pid == 0)
    {
        sub_2298(rax_2, arg1);
        /* no return */
    }
    pid_t rax_4 = fork();
    if (rax_4 < 0)
    {
        __printf_chk(1, "ERREUR : TRAVAIL TERMI");
        exit(1);
        /* no return */
    }
    if (rax_4 == 0)
    {
        sub_22f5(rax_3);
        /* no return */
    }
    int32_t rbp_1 = 0;
    while (true)
    {
        int32_t stat_loc;
        if (waitpid(pid, &stat_loc, 0) == 0xffffffff)
        {
            break;
        }
        int16_t stat_loc_1 = stat_loc;
        if ((stat_loc_1 & 0x7f) == 0)
        {
            break;
        }
        if ((stat_loc_1 == 0x7f && *stat_loc_1[1] == 5))
        {
            sub_2473(rax_4, rax_3, rbp_1, rax_2);
            ptrace(PTRACE_CONT, pid, 0, 0);
            pid_t rax_10 = sub_2380(pid, rax_2, rbp_1);
            rbp_1 = (rbp_1 + 1);
            if (rax_10 == 0xffffffff)
            {
                fail();
                /* no return */
            }
            ptrace(PTRACE_CONT, pid, 0, 0);
        }
        if (rbp_1 == 0x13)
        {
            sub_2367();
            break;
        }
    }
    if (rax != *(fsbase + 0x28))
    {
        __stack_chk_fail();
        /* no return */
    }
    return (rax - *(fsbase + 0x28));
}