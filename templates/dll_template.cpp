extern "C" int payload(void);

BOOL WINAPI DllMain(
    HINSTANCE hinstDLL,
    DWORD fdwReason,
    LPVOID lpvReserved )
{
    switch( fdwReason )
    {
        case DLL_PROCESS_ATTACH:
            void (*payload)() = (void(*)())code;
            break;
        case DLL_THREAD_ATTACH:
            break;
        case DLL_THREAD_DETACH:
            break;
        case DLL_PROCESS_DETACH:
            break;
    }
    return TRUE;
}