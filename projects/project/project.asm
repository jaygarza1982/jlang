segment .data
	hello_str db "Hello, World!"
	hello_new_line db "Hello",10


segment .bss


segment .text
	global main

jmp main

print:

push ebp
mov ebp, esp

mov eax, 4 ;sys_write
mov ebx, 1 ;stdout
mov ecx, DWORD [ebp + 8] ;First item on stack is address to string
mov edx, DWORD [ebp + 12] ;Second item on stack is length of string
int 0x80 ;Call kernel

mov esp, ebp
pop ebp
ret

print_end:
main:

push ebp
mov ebp, esp

push 32
push hello_str
call print
add esp, 2
push 6
push hello_new_line
call print
add esp, 2

mov esp, ebp
pop ebp
ret

main_end:

