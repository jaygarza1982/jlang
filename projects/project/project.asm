segment .data
	hello_str db "Hello, World!"


segment .bss


segment .text
	global main

jmp main

print:

push ebp
mov ebp, esp

mov eax, 4
mov ebx, 1
mov ecx, DWORD [ebp + 8]
mov edx, 32
int 0x80

mov esp, ebp
pop ebp
ret

print_end:
main:

push ebp
mov ebp, esp

push hello_str
call print
mov esp, ebp
pop ebp
ret

main_end:

