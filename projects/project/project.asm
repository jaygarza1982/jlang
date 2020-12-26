segment .data
	hello_new_line db "Hello, World!",10
	jlang_message db "I think JLang is pretty neat!",10


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

push 14
push hello_new_line
call print
add esp, 8
push 30
push jlang_message
call print
add esp, 8

mov esp, ebp
pop ebp
ret

main_end:

